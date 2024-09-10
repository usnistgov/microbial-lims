MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

# environment variables
.EXPORT_ALL_VARIABLES:
ifdef LINKML_ENVIRONMENT_FILENAME
include ${LINKML_ENVIRONMENT_FILENAME}
else
include .env.public
endif

RUN = poetry run
SCHEMA_NAME = $(LINKML_SCHEMA_NAME)
SOURCE_SCHEMA_PATH = $(LINKML_SCHEMA_SOURCE_PATH)
SOURCE_SCHEMA_DIR = $(dir $(SOURCE_SCHEMA_PATH))
LINKML_CONFIG = .linkmllint.yaml
SRC = src
DEST = project
PYMODEL = $(SRC)/$(LINKML_SCHEMA_FOLDER_NAME)/datamodel
DOCDIR = docs
SITEDIR = site
EXAMPLEDIR = examples
# SHEET_MODULE = personinfo_enums
# SHEET_ID = $(LINKML_SCHEMA_GOOGLE_SHEET_ID)
# SHEET_TABS = $(LINKML_SCHEMA_GOOGLE_SHEET_TABS)
# SHEET_MODULE_PATH = $(SOURCE_SCHEMA_DIR)/$(SHEET_MODULE).yaml
TEMPLATEDIR = doc-templates

CONFIG_YAML =
ifdef LINKML_GENERATORS_CONFIG_YAML
CONFIG_YAML = ${LINKML_GENERATORS_CONFIG_YAML}
endif

GEN_DOC_ARGS =
ifdef LINKML_GENERATORS_DOC_ARGS
GEN_DOC_ARGS = ${LINKML_GENERATORS_DOC_ARGS}
endif

GEN_OWL_ARGS =
ifdef LINKML_GENERATORS_OWL_ARGS
GEN_OWL_ARGS = ${LINKML_GENERATORS_OWL_ARGS}
endif

GEN_JAVA_ARGS =
ifdef LINKML_GENERATORS_JAVA_ARGS
GEN_JAVA_ARGS = ${LINKML_GENERATORS_JAVA_ARGS}
endif

GEN_TS_ARGS =
ifdef LINKML_GENERATORS_TYPESCRIPT_ARGS
GEN_TS_ARGS = ${LINKML_GENERATORS_TYPESCRIPT_ARGS}
endif


# basename of a YAML file in model/
.PHONY: all clean setup gen-project gen-examples gen-doc git-init-add git-init git-add git-commit git-status

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
help: status
	@echo ""
	@echo "make setup -- initial setup (run this first)"
	@echo "make site -- makes site locally"
	@echo "make install -- install dependencies"
	@echo "make test -- runs tests"
	@echo "make lint -- perform linting"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo "make gen-doc -- build markdown documentation in \"$(DOCDIR)\" folder"
	@echo "make build-site -- build html pages from markdown"
	@echo "make update -- updates linkml version"
	@echo "make spell -- check spelling with codespell"
	@echo "make help -- show this help"
	@echo ""

status: check-config
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

# generate products and add everything to github
setup: check-config git-init install gen-project gen-examples gen-doc git-add git-commit

# install any dependencies required for building
install:
	poetry install
.PHONY: install

# ---
# Project Synchronization
# ---
#
# check we are up to date
check: cruft-check
cruft-check:
	cruft check
cruft-diff:
	cruft diff

update: update-template update-linkml
update-template:
	cruft update

# todo: consider pinning to template
update-linkml:
	poetry add -D linkml@latest

# EXPERIMENTAL
create-data-harmonizer:
	npm init data-harmonizer $(SOURCE_SCHEMA_PATH)

all: site
site: gen-project gen-doc
%.yaml: gen-project
deploy: all mkd-gh-deploy

compile-sheets:
	$(RUN) sheets2linkml --gsheet-id $(SHEET_ID) $(SHEET_TABS) > $(SHEET_MODULE_PATH).tmp && mv $(SHEET_MODULE_PATH).tmp $(SHEET_MODULE_PATH)

# In future this will be done by conversion
gen-examples:
	cp src/data/examples/* $(EXAMPLEDIR)



spell:
	poetry run codespell

# generates all project files

gen-project-and-pydantic: gen-project gen-pydantic

# use `linkml generate project` to generate jsonschema and jsonld
# generate pydantic separately since `project` doesn't include pydantic (as of Sept. '24)
gen-project: $(PYMODEL)
	$(RUN) linkml generate project \
		${CONFIG_YAML} -d $(DEST) $(SOURCE_SCHEMA_PATH)
	mkdir -p $(DEST)/pydantic

# non-empty arg triggers owl (workaround https://github.com/linkml/linkml/issues/1453)
ifneq ($(strip ${GEN_OWL_ARGS}),)
	mkdir -p ${DEST}/owl || true
	$(RUN) gen-owl ${GEN_OWL_ARGS} $(SOURCE_SCHEMA_PATH) >${DEST}/owl/${SCHEMA_NAME}.owl.ttl
endif
# non-empty arg triggers java
ifneq ($(strip ${GEN_JAVA_ARGS}),)
	$(RUN) gen-java ${GEN_JAVA_ARGS} --output-directory ${DEST}/java/ $(SOURCE_SCHEMA_PATH)
endif
# non-empty arg triggers typescript
ifneq ($(strip ${GEN_TS_ARGS}),)
	mkdir -p ${DEST}/typescript || true
	$(RUN) gen-typescript ${GEN_TS_ARGS} $(SOURCE_SCHEMA_PATH) >${DEST}/typescript/${SCHEMA_NAME}.ts
endif

gen-pydantic:
	$(RUN) linkml generate pydantic $(SOURCE_SCHEMA_PATH) > $(DEST)/pydantic/$(SCHEMA_NAME).py
	cp $(DEST)/pydantic/$(SCHEMA_NAME).py $(PYMODEL)/

# test: test-schema test-python test-examples lint spell
test: test-schema lint gen-doc spell

test-schema:
	$(RUN) linkml generate project ${CONFIG_YAML} -d tmp $(SOURCE_SCHEMA_PATH)

test-python:
	$(RUN) python -m unittest discover

lint:
	$(RUN) linkml-lint --config $(LINKML_CONFIG) $(SOURCE_SCHEMA_PATH)

check-config:
ifndef LINKML_SCHEMA_NAME
	$(error **Project not configured**:\n\n - See '.env.public'\n\n)
else
	$(info Ok)
endif

convert-examples-to-%:
	$(patsubst %, $(RUN) linkml-convert  % -s $(SOURCE_SCHEMA_PATH) -C Person, $(shell ${SHELL} find src/data/examples -name "*.yaml"))

examples/%.yaml: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.json: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.ttl: src/data/examples/%.yaml
	$(RUN) linkml-convert -P EXAMPLE=http://example.org/ -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@

test-examples: examples/output

examples/output: src/microbial_experiment_schema/schema/microbial_experiment_schema.yaml
	mkdir -p $@
	$(RUN) linkml-run-examples \
		--output-formats json \
		--output-formats yaml \
		--counter-example-input-directory src/data/examples/invalid \
		--input-directory src/data/examples/valid \
		--output-directory $@ \
		--schema $< > $@/README.md

# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@


$(DOCDIR):
	mkdir -p $@

gen-doc: $(DOCDIR)
	cp -rf $(SRC)/docs/* $(DOCDIR) ; \
	# generate the JSON data for the d3 visualization:
	$(RUN) generate_viz_json ; \
	cp $(SRC)/docs/*.json $(DOCDIR) ; \
	cp $(SRC)/docs/*.html $(DOCDIR) ; \
	cp $(SRC)/docs/*.js $(DOCDIR) ; \
	$(RUN) linkml generate doc -d $(DOCDIR) --template-directory $(SRC)/$(TEMPLATEDIR) $(SOURCE_SCHEMA_PATH)

build-site: gen-doc
	$(MKDOCS) build -f mkdocs.yml -d $(SITEDIR)

testdoc: gen-doc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

git-init-add: git-init git-add git-commit git-status
git-init:
	git init
git-add: .cruft.json
	git add .
git-commit:
	git commit -m 'chore: make setup was run' -a
git-status:
	git status

# only necessary if setting up via cookiecutter
.cruft.json:
	echo "creating a stub for .cruft.json. IMPORTANT: setup via cruft not cookiecutter recommended!" ; \
	touch $@

clean:
	rm -rf $(DEST)
	rm -rf tmp
	rm -fr docs
	rm -fr $(PYMODEL)/*
	rm -rf site
	rm -rf dist

include project.Makefile

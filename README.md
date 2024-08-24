# Microbial LIMS Metadata Models

This repository holds files that define a metadata schema for the terms collected during
various research tasks in the Microbial Strain team. The primary use case for these schemata
are to validate the metadata entered into eLabFTW (https://elab.nist.gov) experiment records
and prepare bundles for export into LabCAS. In the future, they may be used to programatically
generate the ["extra fields" definitions](https://doc.elabftw.net/metadata.html) of eLabFTW
experiment templates.

## Implementation

Currently, @jat is using [LinkML](https://linkml.io/) to implement the data model in the file
[`microbial_experiment.yaml`](microbial_experiment.yaml), which allows for validation and
generation of JSONSchema outputs via that tool's ["generators"](https://linkml.io/linkml/generators/json-schema.html)
feature. Ther eis no GUI for this directly, but @jat uses Visual Studio Code with the following
directive at the top of the file to make use of VSCode's YAML validation feature:

```
# yaml-language-server: $schema=https://linkml.io/linkml-model/linkml_model/jsonschema/meta.schema.json
```

The resulting schema will be used with the work in the 
[ELabFTW Python API](https://***REMOVED***/gitlab/mml-lims/elabftw-python-api) and the scripts
in the `validation` folder to validate and export experiments generated in ELabFTW (still a WIP). 

## Documentation

Documentation for a LinkML model can be built using the `linkml generate doc` command.
The custom template definitions in the `docgen_templates` folder will be used to generate
the markdown that is then translated into HTML pages by `mkdocs`. 
The following command will also use [mkdocs](https://www.mkdocs.org/) to serve the 
site for local browsing:

```bash
$ linkml generate doc microbial_experiment.yaml -d docs --template-directory docgen_templates && mkdocs serve
```

## Contributors:

- ODI (641):
	- Josh Taillon (@jat)
	- Arlin Stoltzfus (@arlin)
- BBD (644):
	- Kirsten Parratt (@khp)
	- Stephanie Servetas (@sls8)
	- Sierra Miller (@sdm8) 
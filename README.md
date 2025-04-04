# Microbial LIMS Metadata Models

This repository holds files that define a metadata schema for the terms collected during
various research tasks in the Microbial Strain team. The primary use case for these schemata
are to validate the metadata entered into eLabFTW experiment records
and prepare bundles for export into LabCAS. In the future, they may be used to programmatically
generate the ["extra fields" definitions](https://doc.elabftw.net/metadata.html) of eLabFTW
experiment templates.

## Implementation

Currently, we are using [LinkML](https://linkml.io/) to implement the data model in the file
[`microbial_experiment.yaml`](microbial_experiment.yaml), which allows for validation and
generation of JSONSchema outputs via that tool's ["generators"](https://linkml.io/linkml/generators/json-schema.html)
feature. There is no GUI for this directly, but @jat uses Visual Studio Code with the following
directive at the top of the file to make use of VSCode's YAML validation feature:

```
# yaml-language-server: $schema=https://linkml.io/linkml-model/linkml_model/jsonschema/meta.schema.json
```

The resulting schema will be used with the work in the 
[ELabFTW Python API](https://github.com/usnistgov/elabftw-python-api) and the scripts
in the `validation` folder to validate and export experiments generated in ELabFTW (still a WIP). 

## Website/Documentation (WIP)

[https://pages.nist.gov/microbial-lims](https://pages.nist.gov/microbial-lims)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - auto-generated project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [microbial_experiment_schema](src/microbial_experiment_schema)
    * [schema](src/microbial_experiment_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/microbial_experiment_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).


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
	- [Josh Taillon](https://orcid.org/0000-0002-5185-4503) (joshua.taillon@nist.gov)
	- [Arlin Stoltzfus](https://orcid.org/0000-0002-0963-1357) (arlin.stoltzfus@nist.gov)
- BBD (644):
	- [Kirsten Parratt](https://orcid.org/0000-0002-2640-3276) (kirsten.parratt@nist.gov)
	- [Stephanie Servetas](https://orcid.org/0000-0002-4924-4511) (stephanie.servetas@nist.gov)
	- [Sierra Miller](https://orcid.org/0000-0002-3200-428X) (sierra.miller@nist.gov) 
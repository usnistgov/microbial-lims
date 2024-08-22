# Microbial LIMS Metadata Models

This repository holds files that define a metadata schema for the terms collected during
various research tasks in the Microbial Strain team. The primary use case for these schemata
are to validate the metadata entered into eLabFTW (https://elab.nist.gov) experiment records
and prepare bundles for export into LabCAS. In the future, they may be used to programatically
generate the ["extra fields" definitions](https://doc.elabftw.net/metadata.html) of eLabFTW
experiment templates.

## Implementation

Currently, @jat is using [Hackolade Studio](https://hackolade.com/) to design the data model in the file
[`Microbial Strain ELabFTW Model.hck.json`](Microbial Strain ELabFTW Model.hck.json) to
generate the JSONSchema outputs via that tool's ["forward engineering"](https://hackolade.com/help/JSONSchema.html)
feature. Tools such as Visual Studio Code or XML Developer also support JSON Schema modeling
directly.

The resulting JSON Schema files are used with the work in the 
[ELabFTW Python API](https://***REMOVED***/gitlab/mml-lims/elabftw-python-api) and the scripts
in the `validation` folder to validate and export experiments generated in ELabFTW (still a WIP). 

## Documentation

There are various tools that can be used to generate documentation from JSONSchema. Eventually
this section should describe how to generate that documentation and where it can be viewed.

Some options:

- [`json-schema-for-humans`](https://blog.programster.org/generating-html-docs-for-json-schemas) (static HTML) 
	- ![](_static/json-schema-for-humans1.jpg)
	- ![](_static/json-schema-for-humans2.jpg)
- [`jsonschema2md`](https://github.com/adobe/jsonschema2md) (generates markdown, output with jekyll shown below)
	- ![](_static/jsonschema2md-1.jpg)
	- ![](_static/jsonschema2md-2.jpg)
	- ![](_static/jsonschema2md-3.jpg)
- [`wetzel`](https://github.com/CesiumGS/wetzel) (generates markdown or asciidoc)
	- ![](_static/wetzel-md-1.jpg)
	- ![](_static/wetzel-md-2.jpg)
	- ![](_static/wetzel-md-3.jpg)
- [`json-schema-static-docs`](https://tomcollins.github.io/json-schema-static-docs/) (markdown) ([does not currently support 2020-12](https://github.com/tomcollins/json-schema-static-docs/issues/124)) - result after converting to HTML with `jekyll` and `beautiful-jekyll-theme`:
	- ![](_static/json-schema-static-docs-jekyll.jpg)
- [`docusaurus-json-schema-plugin`](https://jy95.github.io/docusaurus-json-schema-plugin/docs/quick-start) (HTML):
	- ![](_static/docusaurus_example.jpg)
- [Hackolade](https://hackolade.com/help/Generatedocumentationandpictures.html) (HTML, markdown, or PDF - can't use as part of pipeline)
	- ![](_static/hackolade_1.jpg)
	- ![](_static/hackolade_2.jpg)
- [Oxygen XML Developer](https://www.oxygenxml.com/json_editor/json_schema_tools.html#generate-json-schema-documentation) (can't use as part of pipeline)
	- ![](_static/xml_developer.png)

## Contributors:

- ODI (641):
	- Josh Taillon (@jat)
	- Arlin Stoltzfus (@arlin)
- BBD (644):
	- Kirsten Parratt (@khp)
	- Stephanie Servetas (@sls8)
	- Sierra Miller (@sdm8) 
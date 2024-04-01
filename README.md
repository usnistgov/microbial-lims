# Microbial LIMS Metadata Models

This repository holds files that define a metadata schema for the terms collected during
various research tasks in the Microbial Strain team. The primary use case for these schemata
are to validate the metadata entered into eLabFTW (https://elab.nist.gov) experiment records
and prepare bundles for export into LabCAS. In the future, they may be used to programatically
generate the ["extra fields" definitions](https://doc.elabftw.net/metadata.html) of eLabFTW
experiment templates.

## Implementation

Currently, @jat is using Hackolade Studio to design the data model in the file
[`Microbial Strain ELabFTW Model.hck.json`](Microbial Strain ELabFTW Model.hck.json) to
generate the JSONSchema outputs via that tool's ["forward engineering"](https://hackolade.com/help/JSONSchema.html)
feature. Tools such as Visual Studio Code or XML Developer also support JSON Schema modeling
directly.

The resulting JSON Schema files are used with the work in the 
[ELabFTW Python API](https://***REMOVED***/gitlab/mml-lims/elabftw-python-api) and the scripts
in the `validation` folder to validate and export experiments generated in ELabFTW (still a WIP). 

## Documentation

There are various tools that can be used to generate documentation from JSONSchema. Eventually
this section should describe 

## Contributors:

- ODI (641):
	- Josh Taillon (@jat)
	- Arlin Stoltzfus (@arlin)
- BBD (644):
	- Kirsten Parratt (@khp)
	- Stephanie Servetas (@sls8)
	- Sierra Miller (@sdm8) 
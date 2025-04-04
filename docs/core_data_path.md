

# Slot: CoreDataPath (core_data_path)




_Portion of the data pathway that will not change as the template is used to generate experimental records (should be network-resolvable)_







URI: [microbial_experiment_schema:core_data_path](https://w3id.org/usnistgov/microbial-experiment-schema/core_data_path)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [CFU](CFU.md) | Metadata describing a colony forming unit counting experiment |  no  |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | Metadata describing a nucleic acid extraction experiment |  no  |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | Metadata describing a data acquisition experiment using the BactoBox |  no  |
| [ExperimentWithInstrument](ExperimentWithInstrument.md) | Holds information about a specific type of Microbial Strain experiment that uses an instrument. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [ExperimentWithData](ExperimentWithData.md) | Holds information about a specific type of Microbial Strain experiment that results in the collection of data. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [CoulterAcquisition](CoulterAcquisition.md) | Metadata describing a Coulter counter acquisition experiment |  no  |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |







## Properties

* Range: [StringValue](StringValue.md)

* Required: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| elabftw_group | LabCAS || elabftw_user_input | True || read_only | True |



### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:core_data_path |
| native | microbial_experiment_schema:core_data_path |




## LinkML Source

<details>
```yaml
name: core_data_path
annotations:
  elabftw_group:
    tag: elabftw_group
    value: LabCAS
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
  read_only:
    tag: read_only
    value: true
description: Portion of the data pathway that will not change as the template is used
  to generate experimental records (should be network-resolvable)
title: CoreDataPath
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: core_data_path
domain_of:
- ExperimentWithData
range: StringValue
required: true

```
</details>
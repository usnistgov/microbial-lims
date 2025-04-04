

# Slot: FixationMethod (fixation_method)




_Specific treatment applied to cells to prevent future changes_







URI: [microbial_experiment_schema:fixation_method](https://w3id.org/usnistgov/microbial-experiment-schema/fixation_method)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [CFU](CFU.md) | Metadata describing a colony forming unit counting experiment |  no  |
| [CoulterAcquisition](CoulterAcquisition.md) | Metadata describing a Coulter counter acquisition experiment |  no  |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | Metadata describing a data acquisition experiment using the BactoBox |  no  |
| [FormaldehydeFixation](FormaldehydeFixation.md) | Metadata describing a formaldehyde fixation experiment |  no  |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |
| [LogCOMETSamplePrep](LogCOMETSamplePrep.md) | Metadata describing a sample preparation process for a LOGComet experiment |  no  |







## Properties

* Range: [FixationMethodValue](FixationMethodValue.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| elabftw_group | Generic Microbial || elabftw_user_input | True |



### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:fixation_method |
| native | microbial_experiment_schema:fixation_method |




## LinkML Source

<details>
```yaml
name: fixation_method
annotations:
  elabftw_group:
    tag: elabftw_group
    value: Generic Microbial
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
description: Specific treatment applied to cells to prevent future changes
title: FixationMethod
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
ifabsent: None
alias: fixation_method
domain_of:
- CytoFLEXAcquisition
- GenericTemplateDeprecated
- FormaldehydeFixation
- MicroscopyAcquisition
- GenericTemplate
- CoulterAcquisition
- BactoBoxAcquisition
- LogCOMETSamplePrep
- CFU
range: FixationMethodValue
required: false

```
</details>
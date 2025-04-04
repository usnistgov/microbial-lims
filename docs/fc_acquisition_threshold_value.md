

# Slot: FCAcquisitionThresholdValue (fc_acquisition_threshold_value)




_Threshold value in arbitrary units that defines the lower limit of data acquisition in flow cytometry_







URI: [microbial_experiment_schema:fc_acquisition_threshold_value](https://w3id.org/usnistgov/microbial-experiment-schema/fc_acquisition_threshold_value)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |







## Properties

* Range: [NumberValue](NumberValue.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| elabftw_group | Fluorescence FC || elabftw_user_input | True |



### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:fc_acquisition_threshold_value |
| native | microbial_experiment_schema:fc_acquisition_threshold_value |




## LinkML Source

<details>
```yaml
name: fc_acquisition_threshold_value
annotations:
  elabftw_group:
    tag: elabftw_group
    value: Fluorescence FC
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
description: Threshold value in arbitrary units that defines the lower limit of data
  acquisition in flow cytometry
title: FCAcquisitionThresholdValue
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: fc_acquisition_threshold_value
domain_of:
- CytoFLEXAcquisition
- GenericTemplateDeprecated
- GenericTemplate
range: NumberValue
required: false

```
</details>
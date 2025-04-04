

# Slot: FCAcquisitionThresholdChannel (fc_acquisition_threshold_channel)




_Which channel as named by the manufacturer was used to threshold the data acquisition_







URI: [microbial_experiment_schema:fc_acquisition_threshold_channel](https://w3id.org/usnistgov/microbial-experiment-schema/fc_acquisition_threshold_channel)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |







## Properties

* Range: [StringValue](StringValue.md)





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
| self | microbial_experiment_schema:fc_acquisition_threshold_channel |
| native | microbial_experiment_schema:fc_acquisition_threshold_channel |




## LinkML Source

<details>
```yaml
name: fc_acquisition_threshold_channel
annotations:
  elabftw_group:
    tag: elabftw_group
    value: Fluorescence FC
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
description: Which channel as named by the manufacturer was used to threshold the
  data acquisition
title: FCAcquisitionThresholdChannel
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: fc_acquisition_threshold_channel
domain_of:
- CytoFLEXAcquisition
- GenericTemplateDeprecated
- GenericTemplate
range: StringValue
required: false

```
</details>
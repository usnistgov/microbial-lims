

# Slot: FCFlowRateSetting (fc_flow_rate_setting)




_Set flow rate of data acquisition on flow cytometer_







URI: [microbial_experiment_schema:fc_flow_rate_setting](https://w3id.org/usnistgov/microbial-experiment-schema/fc_flow_rate_setting)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | Metadata describing a volume calibration using the CytoFLEX instrument |  no  |







## Properties

* Range: [FlowRateValue](FlowRateValue.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| elabftw_group | Fluorescence FC || elabftw_user_input | True || elabftw_default_unit | µL/min |



### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:fc_flow_rate_setting |
| native | microbial_experiment_schema:fc_flow_rate_setting |




## LinkML Source

<details>
```yaml
name: fc_flow_rate_setting
annotations:
  elabftw_group:
    tag: elabftw_group
    value: Fluorescence FC
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
  elabftw_default_unit:
    tag: elabftw_default_unit
    value: µL/min
description: Set flow rate of data acquisition on flow cytometer
title: FCFlowRateSetting
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: fc_flow_rate_setting
domain_of:
- CytoFLEXAcquisition
- CytoFLEXVolumeCalibration
- GenericTemplateDeprecated
- GenericTemplate
range: FlowRateValue
required: false

```
</details>
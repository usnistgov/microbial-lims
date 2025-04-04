

# Slot: FCInjectionMode (fc_injection_mode)




_Sample acquisition format in flow cytometer_







URI: [microbial_experiment_schema:fc_injection_mode](https://w3id.org/usnistgov/microbial-experiment-schema/fc_injection_mode)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | Metadata describing a volume calibration using the CytoFLEX instrument |  no  |







## Properties

* Range: [FCInjectionModeValue](FCInjectionModeValue.md)





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
| self | microbial_experiment_schema:fc_injection_mode |
| native | microbial_experiment_schema:fc_injection_mode |




## LinkML Source

<details>
```yaml
name: fc_injection_mode
annotations:
  elabftw_group:
    tag: elabftw_group
    value: Fluorescence FC
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
description: Sample acquisition format in flow cytometer
title: FCInjectionMode
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
ifabsent: Tube
alias: fc_injection_mode
domain_of:
- CytoFLEXAcquisition
- CytoFLEXVolumeCalibration
- GenericTemplateDeprecated
- GenericTemplate
range: FCInjectionModeValue
required: false

```
</details>
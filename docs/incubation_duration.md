

# Slot: IncubationDuration (incubation_duration)




_Length of time that cells were incubated during an experiment_







URI: [microbial_experiment_schema:incubation_duration](https://w3id.org/usnistgov/microbial-experiment-schema/incubation_duration)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [CFU](CFU.md) | Metadata describing a colony forming unit counting experiment |  no  |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [CellCultureInBroth](CellCultureInBroth.md) | Metadata describing a cell culture experiment |  no  |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | Metadata describing an initiate growth experiment of B. spizizenii |  no  |
| [FormaldehydeFixation](FormaldehydeFixation.md) | Metadata describing a formaldehyde fixation experiment |  no  |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |







## Properties

* Range: [DurationValue](DurationValue.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| elabftw_group | Generic Microbial || elabftw_user_input | True || elabftw_default_unit | hr |



### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:incubation_duration |
| native | microbial_experiment_schema:incubation_duration |




## LinkML Source

<details>
```yaml
name: incubation_duration
annotations:
  elabftw_group:
    tag: elabftw_group
    value: Generic Microbial
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
  elabftw_default_unit:
    tag: elabftw_default_unit
    value: hr
description: Length of time that cells were incubated during an experiment
title: IncubationDuration
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: incubation_duration
domain_of:
- CytoFLEXAcquisition
- CellCultureInBroth
- GenericTemplateDeprecated
- FormaldehydeFixation
- MicroscopyAcquisition
- GenericTemplate
- CFU
- InitiateGrowthOfBSpizizenii
range: DurationValue
required: false

```
</details>
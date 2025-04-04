

# Slot: IncubationAtmosphere (incubation_atmosphere)




_Atmosphere that cells were incubated in to encourage growth_







URI: [microbial_experiment_schema:incubation_atmosphere](https://w3id.org/usnistgov/microbial-experiment-schema/incubation_atmosphere)



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

* Range: [IncubationAtmosphereValue](IncubationAtmosphereValue.md)





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
| self | microbial_experiment_schema:incubation_atmosphere |
| native | microbial_experiment_schema:incubation_atmosphere |




## LinkML Source

<details>
```yaml
name: incubation_atmosphere
annotations:
  elabftw_group:
    tag: elabftw_group
    value: Generic Microbial
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
description: Atmosphere that cells were incubated in to encourage growth
title: IncubationAtmosphere
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: incubation_atmosphere
domain_of:
- CytoFLEXAcquisition
- CellCultureInBroth
- GenericTemplateDeprecated
- FormaldehydeFixation
- MicroscopyAcquisition
- GenericTemplate
- CFU
- InitiateGrowthOfBSpizizenii
range: IncubationAtmosphereValue
required: false

```
</details>
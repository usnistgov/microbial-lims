

# Slot: IncubationAgitation (incubation_agitation)




_Speed of agitation that cells were incubated during an experiment_







URI: [microbial_experiment_schema:incubation_agitation](https://w3id.org/usnistgov/microbial-experiment-schema/incubation_agitation)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [CellCultureInBroth](CellCultureInBroth.md) | Metadata describing a cell culture experiment |  no  |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | Metadata describing an initiate growth experiment of B. spizizenii |  no  |
| [FormaldehydeFixation](FormaldehydeFixation.md) | Metadata describing a formaldehyde fixation experiment |  no  |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |







## Properties

* Range: [AgitationValue](AgitationValue.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| elabftw_group | Generic Microbial || elabftw_user_input | True || elabftw_default_unit | rpm |



### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:incubation_agitation |
| native | microbial_experiment_schema:incubation_agitation |




## LinkML Source

<details>
```yaml
name: incubation_agitation
annotations:
  elabftw_group:
    tag: elabftw_group
    value: Generic Microbial
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
  elabftw_default_unit:
    tag: elabftw_default_unit
    value: rpm
description: Speed of agitation that cells were incubated during an experiment
title: IncubationAgitation
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: incubation_agitation
domain_of:
- CytoFLEXAcquisition
- CellCultureInBroth
- GenericTemplateDeprecated
- FormaldehydeFixation
- MicroscopyAcquisition
- GenericTemplate
- InitiateGrowthOfBSpizizenii
range: AgitationValue
required: false

```
</details>
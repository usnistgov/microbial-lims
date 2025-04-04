

# Slot: GrowthMediaName (growth_media_name)




_Name of media used to culture cells (linked item from ELabFTW)_







URI: [microbial_experiment_schema:growth_media_name](https://w3id.org/usnistgov/microbial-experiment-schema/growth_media_name)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [CFU](CFU.md) | Metadata describing a colony forming unit counting experiment |  no  |
| [CellCultureInBroth](CellCultureInBroth.md) | Metadata describing a cell culture experiment |  no  |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | Metadata describing an initiate growth experiment of B. spizizenii |  no  |







## Properties

* Range: [ELabItemValue](ELabItemValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:growth_media_name |
| native | microbial_experiment_schema:growth_media_name |




## LinkML Source

<details>
```yaml
name: growth_media_name
description: Name of media used to culture cells (linked item from ELabFTW)
title: GrowthMediaName
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: growth_media_name
domain_of:
- CellCultureInBroth
- GenericTemplateDeprecated
- GenericTemplate
- CFU
- InitiateGrowthOfBSpizizenii
range: ELabItemValue
required: false

```
</details>
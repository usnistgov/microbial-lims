

# Slot: CFUMethod (cfu_method)




_Describes deposition format of cells on agar plate_







URI: [microbial_experiment_schema:cfu_method](https://w3id.org/usnistgov/microbial-experiment-schema/cfu_method)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [CFU](CFU.md) | Metadata describing a colony forming unit counting experiment |  no  |







## Properties

* Range: [CFUMethodValue](CFUMethodValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:cfu_method |
| native | microbial_experiment_schema:cfu_method |




## LinkML Source

<details>
```yaml
name: cfu_method
description: Describes deposition format of cells on agar plate
title: CFUMethod
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: cfu_method
domain_of:
- GenericTemplateDeprecated
- GenericTemplate
- CFU
range: CFUMethodValue
required: false

```
</details>
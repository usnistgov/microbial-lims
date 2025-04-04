

# Slot: KitLotNumber (kit_lot_number)




_The lot number of any relevant kits (linked item from ELabFTW)_







URI: [microbial_experiment_schema:kit_lot_number](https://w3id.org/usnistgov/microbial-experiment-schema/kit_lot_number)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | Metadata describing a nucleic acid extraction experiment |  no  |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |







## Properties

* Range: [ELabItemValue](ELabItemValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:kit_lot_number |
| native | microbial_experiment_schema:kit_lot_number |




## LinkML Source

<details>
```yaml
name: kit_lot_number
description: The lot number of any relevant kits (linked item from ELabFTW)
title: KitLotNumber
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: kit_lot_number
domain_of:
- NucleicAcidExtraction
- GenericTemplateDeprecated
- GenericTemplate
range: ELabItemValue
required: false

```
</details>
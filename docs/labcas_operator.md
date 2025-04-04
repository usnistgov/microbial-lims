

# Slot: ~~LabCAS-Operator (labcas_operator)~~<span style="color: #ff5252;"><strong> (DEPRECATED) </strong></span>




_Instrument operator during an experiment (a linked item from ELabFTW)_






* __NOTE__ this element has been deprecated with the following note:
    * *(2024 June) this is too specific, use operator_id instead*
    * Element has been replaced by [operator_id](operator_id.md)


URI: [microbial_experiment_schema:labcas_operator](https://w3id.org/usnistgov/microbial-experiment-schema/labcas_operator)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |







## Properties

* Range: [LabCASOperatorValue](LabCASOperatorValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:labcas_operator |
| native | microbial_experiment_schema:labcas_operator |




## LinkML Source

<details>
```yaml
name: labcas_operator
description: Instrument operator during an experiment (a linked item from ELabFTW)
title: LabCAS-Operator
deprecated: (2024 June) this is too specific, use operator_id instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: operator_id
rank: 1000
alias: labcas_operator
domain_of:
- GenericTemplateDeprecated
range: LabCASOperatorValue
required: false

```
</details>
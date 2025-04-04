

# Slot: ~~LabCAS-MicrobialMaterialID (labcas_microbial_material_id)~~<span style="color: #ff5252;"><strong> (DEPRECATED) </strong></span>




_Cell material(s) used in experiment as named in the eLabFTW database (linked items)_






* __NOTE__ this element has been deprecated with the following note:
    * *(2024 June) this is too specific, use microbial_material_id instead*
    * Element has been replaced by [microbial_material_id](microbial_material_id.md)


URI: [microbial_experiment_schema:labcas_microbial_material_id](https://w3id.org/usnistgov/microbial-experiment-schema/labcas_microbial_material_id)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |







## Properties

* Range: [LabCASMicrobialMaterialIDValue](LabCASMicrobialMaterialIDValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:labcas_microbial_material_id |
| native | microbial_experiment_schema:labcas_microbial_material_id |




## LinkML Source

<details>
```yaml
name: labcas_microbial_material_id
description: Cell material(s) used in experiment as named in the eLabFTW database
  (linked items)
title: LabCAS-MicrobialMaterialID
deprecated: (2024 June) this is too specific, use microbial_material_id instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: microbial_material_id
rank: 1000
alias: labcas_microbial_material_id
domain_of:
- GenericTemplateDeprecated
range: LabCASMicrobialMaterialIDValue
required: false

```
</details>
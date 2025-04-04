

# Class: ~~LabCAS-MicrobialMaterialIDValue (LabCASMicrobialMaterialIDValue)~~<span style="color: #ff5252;"><strong> (DEPRECATED) </strong></span>




_A named sub-class of ArrayValue to hold a list of microbial material links_






* __NOTE__ this element has been deprecated with the following note:
    * *(2024 June) this is too specific, use MicrobialMaterialIDValue instead*
    * Element has been replaced by [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md)


URI: [microbial_experiment_schema:LabCASMicrobialMaterialIDValue](https://w3id.org/usnistgov/microbial-experiment-schema/LabCASMicrobialMaterialIDValue)






```mermaid
 classDiagram
    class LabCASMicrobialMaterialIDValue
    click LabCASMicrobialMaterialIDValue href "../LabCASMicrobialMaterialIDValue"
      ArrayValue <|-- LabCASMicrobialMaterialIDValue
        click ArrayValue href "../ArrayValue"
      
      LabCASMicrobialMaterialIDValue : value
        
          
    
    
    LabCASMicrobialMaterialIDValue --> "1..*" ELabItem : value
    click ELabItem href "../ELabItem"

        
      
```





## Inheritance
* [ArrayValue](ArrayValue.md)
    * **LabCASMicrobialMaterialIDValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1..* <br/> [ELabItem](ELabItem.md) | The actual metadata value for an attribute | [ArrayValue](ArrayValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [labcas_microbial_material_id](labcas_microbial_material_id.md) | range | [LabCASMicrobialMaterialIDValue](LabCASMicrobialMaterialIDValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:LabCASMicrobialMaterialIDValue |
| native | microbial_experiment_schema:LabCASMicrobialMaterialIDValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LabCASMicrobialMaterialIDValue
description: A named sub-class of ArrayValue to hold a list of microbial material
  links
title: LabCAS-MicrobialMaterialIDValue
deprecated: (2024 June) this is too specific, use MicrobialMaterialIDValue instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: MicrobialMaterialIDValue
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: ELabItem
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: LabCASMicrobialMaterialIDValue
description: A named sub-class of ArrayValue to hold a list of microbial material
  links
title: LabCAS-MicrobialMaterialIDValue
deprecated: (2024 June) this is too specific, use MicrobialMaterialIDValue instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: MicrobialMaterialIDValue
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: ELabItem
    inlined: true
    inlined_as_list: true
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: LabCASMicrobialMaterialIDValue
    domain_of:
    - BooleanValue
    - NumberValue
    - StringValue
    - UriValue
    - DateValue
    - ArrayValue
    - ELabItemValue
    - FCInjectionModeValue
    - IncubationAtmosphereValue
    range: ELabItem
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>
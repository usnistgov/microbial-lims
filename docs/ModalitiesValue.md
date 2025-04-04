

# Class: Modalities Value (ModalitiesValue)




_A named sub-class of ArrayValue to hold a list of modality types_







URI: [microbial_experiment_schema:ModalitiesValue](https://w3id.org/usnistgov/microbial-experiment-schema/ModalitiesValue)






```mermaid
 classDiagram
    class ModalitiesValue
    click ModalitiesValue href "../ModalitiesValue"
      ArrayValue <|-- ModalitiesValue
        click ArrayValue href "../ArrayValue"
      
      ModalitiesValue : value
        
          
    
    
    ModalitiesValue --> "1..*" MicroscopyModalitiesEnum : value
    click MicroscopyModalitiesEnum href "../MicroscopyModalitiesEnum"

        
      
```





## Inheritance
* [ArrayValue](ArrayValue.md)
    * **ModalitiesValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1..* <br/> [MicroscopyModalitiesEnum](MicroscopyModalitiesEnum.md) | The actual metadata value for an attribute | [ArrayValue](ArrayValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [modalities](modalities.md) | range | [ModalitiesValue](ModalitiesValue.md) |
| [GenericTemplate](GenericTemplate.md) | [modalities](modalities.md) | range | [ModalitiesValue](ModalitiesValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:ModalitiesValue |
| native | microbial_experiment_schema:ModalitiesValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModalitiesValue
description: A named sub-class of ArrayValue to hold a list of modality types
title: Modalities Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: MicroscopyModalitiesEnum

```
</details>

### Induced

<details>
```yaml
name: ModalitiesValue
description: A named sub-class of ArrayValue to hold a list of modality types
title: Modalities Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: MicroscopyModalitiesEnum
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: ModalitiesValue
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
    range: MicroscopyModalitiesEnum
    required: true
    multivalued: true
    inlined: false

```
</details>


# Class: ~~Transmission Mode Value (TransmissionModeValue)~~<span style="color: #ff5252;"><strong> (DEPRECATED) </strong></span>




_An override of ArrayValue allowing only values from the TransmissionModeEnum enum_






* __NOTE__ this element has been deprecated with the following note:
    * *(2024 June) this is too specific, use ModalitiesValue instead*
    * Element has been replaced by [ModalitiesValue](ModalitiesValue.md)


URI: [microbial_experiment_schema:TransmissionModeValue](https://w3id.org/usnistgov/microbial-experiment-schema/TransmissionModeValue)






```mermaid
 classDiagram
    class TransmissionModeValue
    click TransmissionModeValue href "../TransmissionModeValue"
      ArrayValue <|-- TransmissionModeValue
        click ArrayValue href "../ArrayValue"
      
      TransmissionModeValue : value
        
          
    
    
    TransmissionModeValue --> "1..*" TransmissionModeEnum : value
    click TransmissionModeEnum href "../TransmissionModeEnum"

        
      
```





## Inheritance
* [ArrayValue](ArrayValue.md)
    * **TransmissionModeValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1..* <br/> [TransmissionModeEnum](TransmissionModeEnum.md) | The actual metadata value for an attribute | [ArrayValue](ArrayValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [transmission_mode](transmission_mode.md) | range | [TransmissionModeValue](TransmissionModeValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:TransmissionModeValue |
| native | microbial_experiment_schema:TransmissionModeValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TransmissionModeValue
description: An override of ArrayValue allowing only values from the TransmissionModeEnum
  enum
title: Transmission Mode Value
deprecated: (2024 June) this is too specific, use ModalitiesValue instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: ModalitiesValue
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: TransmissionModeEnum

```
</details>

### Induced

<details>
```yaml
name: TransmissionModeValue
description: An override of ArrayValue allowing only values from the TransmissionModeEnum
  enum
title: Transmission Mode Value
deprecated: (2024 June) this is too specific, use ModalitiesValue instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: ModalitiesValue
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: TransmissionModeEnum
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: TransmissionModeValue
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
    range: TransmissionModeEnum
    required: true
    multivalued: true
    inlined: false

```
</details>
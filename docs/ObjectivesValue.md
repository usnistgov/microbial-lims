

# Class: Objectives Value (ObjectivesValue)




_An override of ArrayValue allowing only values from the ObjectivesEnum enum_







URI: [microbial_experiment_schema:ObjectivesValue](https://w3id.org/usnistgov/microbial-experiment-schema/ObjectivesValue)






```mermaid
 classDiagram
    class ObjectivesValue
    click ObjectivesValue href "../ObjectivesValue"
      ArrayValue <|-- ObjectivesValue
        click ArrayValue href "../ArrayValue"
      
      ObjectivesValue : value
        
          
    
    
    ObjectivesValue --> "1..*" ObjectivesEnum : value
    click ObjectivesEnum href "../ObjectivesEnum"

        
      
```





## Inheritance
* [ArrayValue](ArrayValue.md)
    * **ObjectivesValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1..* <br/> [ObjectivesEnum](ObjectivesEnum.md) | The actual metadata value for an attribute | [ArrayValue](ArrayValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [objective](objective.md) | range | [ObjectivesValue](ObjectivesValue.md) |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [objective](objective.md) | range | [ObjectivesValue](ObjectivesValue.md) |
| [GenericTemplate](GenericTemplate.md) | [objective](objective.md) | range | [ObjectivesValue](ObjectivesValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:ObjectivesValue |
| native | microbial_experiment_schema:ObjectivesValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ObjectivesValue
description: An override of ArrayValue allowing only values from the ObjectivesEnum
  enum
title: Objectives Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: ObjectivesEnum

```
</details>

### Induced

<details>
```yaml
name: ObjectivesValue
description: An override of ArrayValue allowing only values from the ObjectivesEnum
  enum
title: Objectives Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: ObjectivesEnum
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: ObjectivesValue
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
    range: ObjectivesEnum
    required: true
    multivalued: true
    inlined: false

```
</details>
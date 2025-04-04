

# Class: Volume Value (VolumeValue)




_A class to hold a numerical value representing a volumetric measurement_







URI: [microbial_experiment_schema:VolumeValue](https://w3id.org/usnistgov/microbial-experiment-schema/VolumeValue)






```mermaid
 classDiagram
    class VolumeValue
    click VolumeValue href "../VolumeValue"
      NumberValue <|-- VolumeValue
        click NumberValue href "../NumberValue"
      
      VolumeValue : unit
        
          
    
    
    VolumeValue --> "1" VolumeUnitEnum : unit
    click VolumeUnitEnum href "../VolumeUnitEnum"

        
      VolumeValue : value
        
      
```





## Inheritance
* [NumberValue](NumberValue.md)
    * **VolumeValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [Decimal](Decimal.md) | The actual metadata value for an attribute | [NumberValue](NumberValue.md) |
| [unit](unit.md) | 1 <br/> [VolumeUnitEnum](VolumeUnitEnum.md) | The volume unit corresponding to a metadata value | [NumberValue](NumberValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [acquisition_volume](acquisition_volume.md) | range | [VolumeValue](VolumeValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [cell_volume](cell_volume.md) | range | [VolumeValue](VolumeValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [diluent_volume](diluent_volume.md) | range | [VolumeValue](VolumeValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:VolumeValue |
| native | microbial_experiment_schema:VolumeValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VolumeValue
description: A class to hold a numerical value representing a volumetric measurement
title: Volume Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The volume unit corresponding to a metadata value
    range: VolumeUnitEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: VolumeValue
description: A class to hold a numerical value representing a volumetric measurement
title: Volume Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The volume unit corresponding to a metadata value
    range: VolumeUnitEnum
    required: true
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: VolumeValue
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
    range: decimal
    required: true
  unit:
    name: unit
    description: The volume unit corresponding to a metadata value
    title: unit
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: unit
    owner: VolumeValue
    domain_of:
    - NumberValue
    range: VolumeUnitEnum
    required: true

```
</details>
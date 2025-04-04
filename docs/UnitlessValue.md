

# Class: Unitless Value (UnitlessValue)




_A class to hold an explicitly unitless numerical value_







URI: [microbial_experiment_schema:UnitlessValue](https://w3id.org/usnistgov/microbial-experiment-schema/UnitlessValue)






```mermaid
 classDiagram
    class UnitlessValue
    click UnitlessValue href "../UnitlessValue"
      NumberValue <|-- UnitlessValue
        click NumberValue href "../NumberValue"
      
      UnitlessValue : unit
        
          
    
    
    UnitlessValue --> "1" UnitlessEnum : unit
    click UnitlessEnum href "../UnitlessEnum"

        
      UnitlessValue : value
        
      
```





## Inheritance
* [NumberValue](NumberValue.md)
    * **UnitlessValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [Decimal](Decimal.md) | The actual metadata value for an attribute | [NumberValue](NumberValue.md) |
| [unit](unit.md) | 1 <br/> [UnitlessEnum](UnitlessEnum.md) | The word "Unitless" corresponding to a unitless metadata value | [NumberValue](NumberValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | [percent_volume_deviation](percent_volume_deviation.md) | range | [UnitlessValue](UnitlessValue.md) |
| [GenericTemplate](GenericTemplate.md) | [percent_volume_deviation](percent_volume_deviation.md) | range | [UnitlessValue](UnitlessValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:UnitlessValue |
| native | microbial_experiment_schema:UnitlessValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnitlessValue
description: A class to hold an explicitly unitless numerical value
title: Unitless Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The word "Unitless" corresponding to a unitless metadata value
    range: UnitlessEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: UnitlessValue
description: A class to hold an explicitly unitless numerical value
title: Unitless Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The word "Unitless" corresponding to a unitless metadata value
    range: UnitlessEnum
    required: true
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: UnitlessValue
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
    description: The word "Unitless" corresponding to a unitless metadata value
    title: unit
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: unit
    owner: UnitlessValue
    domain_of:
    - NumberValue
    range: UnitlessEnum
    required: true

```
</details>
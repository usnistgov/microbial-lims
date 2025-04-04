

# Class: Temperature Value (TemperatureValue)




_A class to hold a numerical value representing a temperature measurement_







URI: [microbial_experiment_schema:TemperatureValue](https://w3id.org/usnistgov/microbial-experiment-schema/TemperatureValue)






```mermaid
 classDiagram
    class TemperatureValue
    click TemperatureValue href "../TemperatureValue"
      NumberValue <|-- TemperatureValue
        click NumberValue href "../NumberValue"
      
      TemperatureValue : unit
        
          
    
    
    TemperatureValue --> "1" TemperatureUnitEnum : unit
    click TemperatureUnitEnum href "../TemperatureUnitEnum"

        
      TemperatureValue : value
        
      
```





## Inheritance
* [NumberValue](NumberValue.md)
    * **TemperatureValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [Decimal](Decimal.md) | The actual metadata value for an attribute | [NumberValue](NumberValue.md) |
| [unit](unit.md) | 1 <br/> [TemperatureUnitEnum](TemperatureUnitEnum.md) | The temperature unit corresponding to a metadata value | [NumberValue](NumberValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | [incubation_temperature](incubation_temperature.md) | range | [TemperatureValue](TemperatureValue.md) |
| [CellCultureInBroth](CellCultureInBroth.md) | [incubation_temperature](incubation_temperature.md) | range | [TemperatureValue](TemperatureValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [incubation_temperature](incubation_temperature.md) | range | [TemperatureValue](TemperatureValue.md) |
| [FormaldehydeFixation](FormaldehydeFixation.md) | [incubation_temperature](incubation_temperature.md) | range | [TemperatureValue](TemperatureValue.md) |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [incubation_temperature](incubation_temperature.md) | range | [TemperatureValue](TemperatureValue.md) |
| [GenericTemplate](GenericTemplate.md) | [incubation_temperature](incubation_temperature.md) | range | [TemperatureValue](TemperatureValue.md) |
| [CFU](CFU.md) | [incubation_temperature](incubation_temperature.md) | range | [TemperatureValue](TemperatureValue.md) |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | [incubation_temperature](incubation_temperature.md) | range | [TemperatureValue](TemperatureValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:TemperatureValue |
| native | microbial_experiment_schema:TemperatureValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TemperatureValue
description: A class to hold a numerical value representing a temperature measurement
title: Temperature Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The temperature unit corresponding to a metadata value
    range: TemperatureUnitEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: TemperatureValue
description: A class to hold a numerical value representing a temperature measurement
title: Temperature Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The temperature unit corresponding to a metadata value
    range: TemperatureUnitEnum
    required: true
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: TemperatureValue
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
    description: The temperature unit corresponding to a metadata value
    title: unit
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: unit
    owner: TemperatureValue
    domain_of:
    - NumberValue
    range: TemperatureUnitEnum
    required: true

```
</details>
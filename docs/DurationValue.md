

# Class: Duration Value (DurationValue)




_A class to hold a numerical value representing a time duration measurement_







URI: [microbial_experiment_schema:DurationValue](https://w3id.org/usnistgov/microbial-experiment-schema/DurationValue)






```mermaid
 classDiagram
    class DurationValue
    click DurationValue href "../DurationValue"
      NumberValue <|-- DurationValue
        click NumberValue href "../NumberValue"
      
      DurationValue : unit
        
          
    
    
    DurationValue --> "1" DurationUnitEnum : unit
    click DurationUnitEnum href "../DurationUnitEnum"

        
      DurationValue : value
        
      
```





## Inheritance
* [NumberValue](NumberValue.md)
    * **DurationValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [Decimal](Decimal.md) | The actual metadata value for an attribute | [NumberValue](NumberValue.md) |
| [unit](unit.md) | 1 <br/> [DurationUnitEnum](DurationUnitEnum.md) | The time duration unit corresponding to a metadata value | [NumberValue](NumberValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | [incubation_duration](incubation_duration.md) | range | [DurationValue](DurationValue.md) |
| [CellCultureInBroth](CellCultureInBroth.md) | [incubation_duration](incubation_duration.md) | range | [DurationValue](DurationValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [acquisition_time](acquisition_time.md) | range | [DurationValue](DurationValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [growth_duration](growth_duration.md) | range | [DurationValue](DurationValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [incubation_duration](incubation_duration.md) | range | [DurationValue](DurationValue.md) |
| [FormaldehydeFixation](FormaldehydeFixation.md) | [incubation_duration](incubation_duration.md) | range | [DurationValue](DurationValue.md) |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [incubation_duration](incubation_duration.md) | range | [DurationValue](DurationValue.md) |
| [GenericTemplate](GenericTemplate.md) | [incubation_duration](incubation_duration.md) | range | [DurationValue](DurationValue.md) |
| [CFU](CFU.md) | [incubation_duration](incubation_duration.md) | range | [DurationValue](DurationValue.md) |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | [incubation_duration](incubation_duration.md) | range | [DurationValue](DurationValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:DurationValue |
| native | microbial_experiment_schema:DurationValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DurationValue
description: A class to hold a numerical value representing a time duration measurement
title: Duration Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The time duration unit corresponding to a metadata value
    range: DurationUnitEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: DurationValue
description: A class to hold a numerical value representing a time duration measurement
title: Duration Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The time duration unit corresponding to a metadata value
    range: DurationUnitEnum
    required: true
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: DurationValue
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
    description: The time duration unit corresponding to a metadata value
    title: unit
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: unit
    owner: DurationValue
    domain_of:
    - NumberValue
    range: DurationUnitEnum
    required: true

```
</details>
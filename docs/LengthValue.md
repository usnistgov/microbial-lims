

# Class: Length Value (LengthValue)




_A class to hold a numerical value representing a linear measurement_







URI: [microbial_experiment_schema:LengthValue](https://w3id.org/usnistgov/microbial-experiment-schema/LengthValue)






```mermaid
 classDiagram
    class LengthValue
    click LengthValue href "../LengthValue"
      NumberValue <|-- LengthValue
        click NumberValue href "../NumberValue"
      
      LengthValue : unit
        
          
    
    
    LengthValue --> "1" LengthUnitEnum : unit
    click LengthUnitEnum href "../LengthUnitEnum"

        
      LengthValue : value
        
      
```





## Inheritance
* [NumberValue](NumberValue.md)
    * **LengthValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [Decimal](Decimal.md) | The actual metadata value for an attribute | [NumberValue](NumberValue.md) |
| [unit](unit.md) | 1 <br/> [LengthUnitEnum](LengthUnitEnum.md) | The length unit corresponding to a metadata value | [NumberValue](NumberValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [coulter_aperture_size](coulter_aperture_size.md) | range | [LengthValue](LengthValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:LengthValue |
| native | microbial_experiment_schema:LengthValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LengthValue
description: A class to hold a numerical value representing a linear measurement
title: Length Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The length unit corresponding to a metadata value
    range: LengthUnitEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: LengthValue
description: A class to hold a numerical value representing a linear measurement
title: Length Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The length unit corresponding to a metadata value
    range: LengthUnitEnum
    required: true
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: LengthValue
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
    description: The length unit corresponding to a metadata value
    title: unit
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: unit
    owner: LengthValue
    domain_of:
    - NumberValue
    range: LengthUnitEnum
    required: true

```
</details>
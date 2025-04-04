

# Class: Count Value (CountValue)




_A class to hold a numerical value representing a counting measurement_







URI: [microbial_experiment_schema:CountValue](https://w3id.org/usnistgov/microbial-experiment-schema/CountValue)






```mermaid
 classDiagram
    class CountValue
    click CountValue href "../CountValue"
      NumberValue <|-- CountValue
        click NumberValue href "../NumberValue"
      
      CountValue : unit
        
          
    
    
    CountValue --> "1" CountUnitEnum : unit
    click CountUnitEnum href "../CountUnitEnum"

        
      CountValue : value
        
      
```





## Inheritance
* [NumberValue](NumberValue.md)
    * **CountValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [Decimal](Decimal.md) | The actual metadata value for an attribute | [NumberValue](NumberValue.md) |
| [unit](unit.md) | 1 <br/> [CountUnitEnum](CountUnitEnum.md) | The count unit corresponding to a metadata value | [NumberValue](NumberValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [fc_acquisition_count_target](fc_acquisition_count_target.md) | range | [CountValue](CountValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:CountValue |
| native | microbial_experiment_schema:CountValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CountValue
description: A class to hold a numerical value representing a counting measurement
title: Count Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The count unit corresponding to a metadata value
    range: CountUnitEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: CountValue
description: A class to hold a numerical value representing a counting measurement
title: Count Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The count unit corresponding to a metadata value
    range: CountUnitEnum
    required: true
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: CountValue
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
    description: The count unit corresponding to a metadata value
    title: unit
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: unit
    owner: CountValue
    domain_of:
    - NumberValue
    range: CountUnitEnum
    required: true

```
</details>
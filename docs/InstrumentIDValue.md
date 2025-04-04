

# Class: Instrument ID Value (InstrumentIDValue)




_A named sub-class of ELabItemValue to hold an instrument identifier value_







URI: [microbial_experiment_schema:InstrumentIDValue](https://w3id.org/usnistgov/microbial-experiment-schema/InstrumentIDValue)






```mermaid
 classDiagram
    class InstrumentIDValue
    click InstrumentIDValue href "../InstrumentIDValue"
      ELabItemValue <|-- InstrumentIDValue
        click ELabItemValue href "../ELabItemValue"
      
      InstrumentIDValue : value
        
          
    
    
    InstrumentIDValue --> "1" ELabItem : value
    click ELabItem href "../ELabItem"

        
      
```





## Inheritance
* [ELabItemValue](ELabItemValue.md)
    * **InstrumentIDValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [ELabItem](ELabItem.md) | The actual metadata value for an attribute | [ELabItemValue](ELabItemValue.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:InstrumentIDValue |
| native | microbial_experiment_schema:InstrumentIDValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InstrumentIDValue
description: A named sub-class of ELabItemValue to hold an instrument identifier value
title: Instrument ID Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ELabItemValue

```
</details>

### Induced

<details>
```yaml
name: InstrumentIDValue
description: A named sub-class of ELabItemValue to hold an instrument identifier value
title: Instrument ID Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ELabItemValue
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: InstrumentIDValue
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
    inlined: true

```
</details>
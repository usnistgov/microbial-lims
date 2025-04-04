

# Class: Agitation Value (AgitationValue)




_A class to hold a numerical value representing an agitation speed_







URI: [microbial_experiment_schema:AgitationValue](https://w3id.org/usnistgov/microbial-experiment-schema/AgitationValue)






```mermaid
 classDiagram
    class AgitationValue
    click AgitationValue href "../AgitationValue"
      NumberValue <|-- AgitationValue
        click NumberValue href "../NumberValue"
      
      AgitationValue : unit
        
          
    
    
    AgitationValue --> "1" AgitationEnum : unit
    click AgitationEnum href "../AgitationEnum"

        
      AgitationValue : value
        
      
```





## Inheritance
* [NumberValue](NumberValue.md)
    * **AgitationValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [Decimal](Decimal.md) | The actual metadata value for an attribute | [NumberValue](NumberValue.md) |
| [unit](unit.md) | 1 <br/> [AgitationEnum](AgitationEnum.md) | The agitation speed unit corresponding to a metadata value | [NumberValue](NumberValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | [incubation_agitation](incubation_agitation.md) | range | [AgitationValue](AgitationValue.md) |
| [CellCultureInBroth](CellCultureInBroth.md) | [incubation_agitation](incubation_agitation.md) | range | [AgitationValue](AgitationValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [incubation_agitation](incubation_agitation.md) | range | [AgitationValue](AgitationValue.md) |
| [FormaldehydeFixation](FormaldehydeFixation.md) | [incubation_agitation](incubation_agitation.md) | range | [AgitationValue](AgitationValue.md) |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [incubation_agitation](incubation_agitation.md) | range | [AgitationValue](AgitationValue.md) |
| [GenericTemplate](GenericTemplate.md) | [incubation_agitation](incubation_agitation.md) | range | [AgitationValue](AgitationValue.md) |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | [incubation_agitation](incubation_agitation.md) | range | [AgitationValue](AgitationValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:AgitationValue |
| native | microbial_experiment_schema:AgitationValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AgitationValue
description: A class to hold a numerical value representing an agitation speed
title: Agitation Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The agitation speed unit corresponding to a metadata value
    range: AgitationEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: AgitationValue
description: A class to hold a numerical value representing an agitation speed
title: Agitation Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: NumberValue
slot_usage:
  unit:
    name: unit
    description: The agitation speed unit corresponding to a metadata value
    range: AgitationEnum
    required: true
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: AgitationValue
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
    description: The agitation speed unit corresponding to a metadata value
    title: unit
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: unit
    owner: AgitationValue
    domain_of:
    - NumberValue
    range: AgitationEnum
    required: true

```
</details>
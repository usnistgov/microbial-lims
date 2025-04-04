

# Class: Fixation Method Value (FixationMethodValue)




_An override of ArrayValue allowing only values from the FixationMethodEnum enum_







URI: [microbial_experiment_schema:FixationMethodValue](https://w3id.org/usnistgov/microbial-experiment-schema/FixationMethodValue)






```mermaid
 classDiagram
    class FixationMethodValue
    click FixationMethodValue href "../FixationMethodValue"
      ArrayValue <|-- FixationMethodValue
        click ArrayValue href "../ArrayValue"
      
      FixationMethodValue : value
        
          
    
    
    FixationMethodValue --> "1..*" FixationMethodEnum : value
    click FixationMethodEnum href "../FixationMethodEnum"

        
      
```





## Inheritance
* [ArrayValue](ArrayValue.md)
    * **FixationMethodValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1..* <br/> [FixationMethodEnum](FixationMethodEnum.md) | The value attribute for FixationMethod | [ArrayValue](ArrayValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | [fixation_method](fixation_method.md) | range | [FixationMethodValue](FixationMethodValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [fixation_method](fixation_method.md) | range | [FixationMethodValue](FixationMethodValue.md) |
| [FormaldehydeFixation](FormaldehydeFixation.md) | [fixation_method](fixation_method.md) | range | [FixationMethodValue](FixationMethodValue.md) |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [fixation_method](fixation_method.md) | range | [FixationMethodValue](FixationMethodValue.md) |
| [GenericTemplate](GenericTemplate.md) | [fixation_method](fixation_method.md) | range | [FixationMethodValue](FixationMethodValue.md) |
| [CoulterAcquisition](CoulterAcquisition.md) | [fixation_method](fixation_method.md) | range | [FixationMethodValue](FixationMethodValue.md) |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | [fixation_method](fixation_method.md) | range | [FixationMethodValue](FixationMethodValue.md) |
| [LogCOMETSamplePrep](LogCOMETSamplePrep.md) | [fixation_method](fixation_method.md) | range | [FixationMethodValue](FixationMethodValue.md) |
| [CFU](CFU.md) | [fixation_method](fixation_method.md) | range | [FixationMethodValue](FixationMethodValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:FixationMethodValue |
| native | microbial_experiment_schema:FixationMethodValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FixationMethodValue
description: An override of ArrayValue allowing only values from the FixationMethodEnum
  enum
title: Fixation Method Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    description: The value attribute for FixationMethod
    range: FixationMethodEnum

```
</details>

### Induced

<details>
```yaml
name: FixationMethodValue
description: An override of ArrayValue allowing only values from the FixationMethodEnum
  enum
title: Fixation Method Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    description: The value attribute for FixationMethod
    range: FixationMethodEnum
attributes:
  value:
    name: value
    description: The value attribute for FixationMethod
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: FixationMethodValue
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
    range: FixationMethodEnum
    required: true
    multivalued: true
    inlined: false

```
</details>
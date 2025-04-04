

# Class: ~~LabCAS-OperatorValue (LabCASOperatorValue)~~<span style="color: #ff5252;"><strong> (DEPRECATED) </strong></span>




_A named sub-class of ELabItemValue to hold the operator identifier_






* __NOTE__ this element has been deprecated with the following note:
    * *(2024 June) this is too specific, use OperatorIDValue instead*
    * Element has been replaced by [OperatorIDValue](OperatorIDValue.md)


URI: [microbial_experiment_schema:LabCASOperatorValue](https://w3id.org/usnistgov/microbial-experiment-schema/LabCASOperatorValue)






```mermaid
 classDiagram
    class LabCASOperatorValue
    click LabCASOperatorValue href "../LabCASOperatorValue"
      ELabItemValue <|-- LabCASOperatorValue
        click ELabItemValue href "../ELabItemValue"
      
      LabCASOperatorValue : value
        
          
    
    
    LabCASOperatorValue --> "1" ELabItem : value
    click ELabItem href "../ELabItem"

        
      
```





## Inheritance
* [ELabItemValue](ELabItemValue.md)
    * **LabCASOperatorValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [ELabItem](ELabItem.md) | The actual metadata value for an attribute | [ELabItemValue](ELabItemValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [labcas_operator](labcas_operator.md) | range | [LabCASOperatorValue](LabCASOperatorValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:LabCASOperatorValue |
| native | microbial_experiment_schema:LabCASOperatorValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LabCASOperatorValue
description: A named sub-class of ELabItemValue to hold the operator identifier
title: LabCAS-OperatorValue
deprecated: (2024 June) this is too specific, use OperatorIDValue instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: OperatorIDValue
is_a: ELabItemValue

```
</details>

### Induced

<details>
```yaml
name: LabCASOperatorValue
description: A named sub-class of ELabItemValue to hold the operator identifier
title: LabCAS-OperatorValue
deprecated: (2024 June) this is too specific, use OperatorIDValue instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: OperatorIDValue
is_a: ELabItemValue
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: LabCASOperatorValue
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


# Class: ~~LabCAS-InstrumentValue (LabCASInstrumentValue)~~<span style="color: #ff5252;"><strong> (DEPRECATED) </strong></span>




_A named sub-class of ELabItemValue to hold the instrument identifier_






* __NOTE__ this element has been deprecated with the following note:
    * *(2024 June) this is too specific, use InstrumentIDValue instead*
    * Element has been replaced by [InstrumentIDValue](InstrumentIDValue.md)


URI: [microbial_experiment_schema:LabCASInstrumentValue](https://w3id.org/usnistgov/microbial-experiment-schema/LabCASInstrumentValue)






```mermaid
 classDiagram
    class LabCASInstrumentValue
    click LabCASInstrumentValue href "../LabCASInstrumentValue"
      ELabItemValue <|-- LabCASInstrumentValue
        click ELabItemValue href "../ELabItemValue"
      
      LabCASInstrumentValue : value
        
          
    
    
    LabCASInstrumentValue --> "1" ELabItem : value
    click ELabItem href "../ELabItem"

        
      
```





## Inheritance
* [ELabItemValue](ELabItemValue.md)
    * **LabCASInstrumentValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [ELabItem](ELabItem.md) | The actual metadata value for an attribute | [ELabItemValue](ELabItemValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [labcas_instrument](labcas_instrument.md) | range | [LabCASInstrumentValue](LabCASInstrumentValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:LabCASInstrumentValue |
| native | microbial_experiment_schema:LabCASInstrumentValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LabCASInstrumentValue
description: A named sub-class of ELabItemValue to hold the instrument identifier
title: LabCAS-InstrumentValue
deprecated: (2024 June) this is too specific, use InstrumentIDValue instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: InstrumentIDValue
is_a: ELabItemValue

```
</details>

### Induced

<details>
```yaml
name: LabCASInstrumentValue
description: A named sub-class of ELabItemValue to hold the instrument identifier
title: LabCAS-InstrumentValue
deprecated: (2024 June) this is too specific, use InstrumentIDValue instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: InstrumentIDValue
is_a: ELabItemValue
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: LabCASInstrumentValue
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
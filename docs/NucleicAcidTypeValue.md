

# Class: Nucleic Acid Type Value (NucleicAcidTypeValue)




_An override of StringValue allowing only a value from the NucleicAcidTypeEnum enum_







URI: [microbial_experiment_schema:NucleicAcidTypeValue](https://w3id.org/usnistgov/microbial-experiment-schema/NucleicAcidTypeValue)






```mermaid
 classDiagram
    class NucleicAcidTypeValue
    click NucleicAcidTypeValue href "../NucleicAcidTypeValue"
      StringValue <|-- NucleicAcidTypeValue
        click StringValue href "../StringValue"
      
      NucleicAcidTypeValue : value
        
          
    
    
    NucleicAcidTypeValue --> "1" NucleicAcidTypeEnum : value
    click NucleicAcidTypeEnum href "../NucleicAcidTypeEnum"

        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **NucleicAcidTypeValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [NucleicAcidTypeEnum](NucleicAcidTypeEnum.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | [nucleic_acid_type](nucleic_acid_type.md) | range | [NucleicAcidTypeValue](NucleicAcidTypeValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [nucleic_acid_type](nucleic_acid_type.md) | range | [NucleicAcidTypeValue](NucleicAcidTypeValue.md) |
| [GenericTemplate](GenericTemplate.md) | [nucleic_acid_type](nucleic_acid_type.md) | range | [NucleicAcidTypeValue](NucleicAcidTypeValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:NucleicAcidTypeValue |
| native | microbial_experiment_schema:NucleicAcidTypeValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NucleicAcidTypeValue
description: An override of StringValue allowing only a value from the NucleicAcidTypeEnum
  enum
title: Nucleic Acid Type Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: NucleicAcidTypeEnum

```
</details>

### Induced

<details>
```yaml
name: NucleicAcidTypeValue
description: An override of StringValue allowing only a value from the NucleicAcidTypeEnum
  enum
title: Nucleic Acid Type Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: NucleicAcidTypeEnum
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: NucleicAcidTypeValue
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
    range: NucleicAcidTypeEnum
    required: true

```
</details>
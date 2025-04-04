

# Class: Nucleic Acid Extraction Template Name Value (NucleicAcidExtractionTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a Nucleic Acid Extraction experiment_







URI: [microbial_experiment_schema:NucleicAcidExtractionTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/NucleicAcidExtractionTemplateNameValue)






```mermaid
 classDiagram
    class NucleicAcidExtractionTemplateNameValue
    click NucleicAcidExtractionTemplateNameValue href "../NucleicAcidExtractionTemplateNameValue"
      StringValue <|-- NucleicAcidExtractionTemplateNameValue
        click StringValue href "../StringValue"
      
      NucleicAcidExtractionTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **NucleicAcidExtractionTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | [template_name](template_name.md) | range | [NucleicAcidExtractionTemplateNameValue](NucleicAcidExtractionTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:NucleicAcidExtractionTemplateNameValue |
| native | microbial_experiment_schema:NucleicAcidExtractionTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NucleicAcidExtractionTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Nucleic Acid Extraction experiment
title: Nucleic Acid Extraction Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Nucleic Acid Extraction$

```
</details>

### Induced

<details>
```yaml
name: NucleicAcidExtractionTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Nucleic Acid Extraction experiment
title: Nucleic Acid Extraction Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Nucleic Acid Extraction$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: NucleicAcidExtractionTemplateNameValue
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
    range: string
    required: true
    pattern: ^Nucleic Acid Extraction$

```
</details>
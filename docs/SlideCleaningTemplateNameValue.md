

# Class: Slide Cleaning Template Name Value (SlideCleaningTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a SlideCleaning experiment_







URI: [microbial_experiment_schema:SlideCleaningTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/SlideCleaningTemplateNameValue)






```mermaid
 classDiagram
    class SlideCleaningTemplateNameValue
    click SlideCleaningTemplateNameValue href "../SlideCleaningTemplateNameValue"
      StringValue <|-- SlideCleaningTemplateNameValue
        click StringValue href "../StringValue"
      
      SlideCleaningTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **SlideCleaningTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SlideCleaning](SlideCleaning.md) | [template_name](template_name.md) | range | [SlideCleaningTemplateNameValue](SlideCleaningTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:SlideCleaningTemplateNameValue |
| native | microbial_experiment_schema:SlideCleaningTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SlideCleaningTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a SlideCleaning experiment
title: Slide Cleaning Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^SlideCleaning$

```
</details>

### Induced

<details>
```yaml
name: SlideCleaningTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a SlideCleaning experiment
title: Slide Cleaning Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^SlideCleaning$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: SlideCleaningTemplateNameValue
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
    pattern: ^SlideCleaning$

```
</details>
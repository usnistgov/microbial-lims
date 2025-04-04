

# Class: CFU Template Name Value (CFUTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a CFU experiment_







URI: [microbial_experiment_schema:CFUTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/CFUTemplateNameValue)






```mermaid
 classDiagram
    class CFUTemplateNameValue
    click CFUTemplateNameValue href "../CFUTemplateNameValue"
      StringValue <|-- CFUTemplateNameValue
        click StringValue href "../StringValue"
      
      CFUTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **CFUTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CFU](CFU.md) | [template_name](template_name.md) | range | [CFUTemplateNameValue](CFUTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:CFUTemplateNameValue |
| native | microbial_experiment_schema:CFUTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CFUTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a CFU experiment
title: CFU Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^CFU$

```
</details>

### Induced

<details>
```yaml
name: CFUTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a CFU experiment
title: CFU Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^CFU$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: CFUTemplateNameValue
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
    pattern: ^CFU$

```
</details>
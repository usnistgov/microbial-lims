

# Class: Formaldehyde Fixation Template Name Value (FormaldehydeFixationTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a FormaldehydeFixation experiment_







URI: [microbial_experiment_schema:FormaldehydeFixationTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/FormaldehydeFixationTemplateNameValue)






```mermaid
 classDiagram
    class FormaldehydeFixationTemplateNameValue
    click FormaldehydeFixationTemplateNameValue href "../FormaldehydeFixationTemplateNameValue"
      StringValue <|-- FormaldehydeFixationTemplateNameValue
        click StringValue href "../StringValue"
      
      FormaldehydeFixationTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **FormaldehydeFixationTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [FormaldehydeFixation](FormaldehydeFixation.md) | [template_name](template_name.md) | range | [FormaldehydeFixationTemplateNameValue](FormaldehydeFixationTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:FormaldehydeFixationTemplateNameValue |
| native | microbial_experiment_schema:FormaldehydeFixationTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FormaldehydeFixationTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a FormaldehydeFixation experiment
title: Formaldehyde Fixation Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^FormaldehydeFixation$

```
</details>

### Induced

<details>
```yaml
name: FormaldehydeFixationTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a FormaldehydeFixation experiment
title: Formaldehyde Fixation Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^FormaldehydeFixation$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: FormaldehydeFixationTemplateNameValue
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
    pattern: ^FormaldehydeFixation$

```
</details>
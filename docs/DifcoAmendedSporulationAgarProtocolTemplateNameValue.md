

# Class: Difco Amended Sporulation Agar Protocol Template Name Value (DifcoAmendedSporulationAgarProtocolTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a Difco Amended Sporulation Agar Protocol experiment_







URI: [microbial_experiment_schema:DifcoAmendedSporulationAgarProtocolTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/DifcoAmendedSporulationAgarProtocolTemplateNameValue)






```mermaid
 classDiagram
    class DifcoAmendedSporulationAgarProtocolTemplateNameValue
    click DifcoAmendedSporulationAgarProtocolTemplateNameValue href "../DifcoAmendedSporulationAgarProtocolTemplateNameValue"
      StringValue <|-- DifcoAmendedSporulationAgarProtocolTemplateNameValue
        click StringValue href "../StringValue"
      
      DifcoAmendedSporulationAgarProtocolTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **DifcoAmendedSporulationAgarProtocolTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DifcoAmendedSporulationAgarProtocol](DifcoAmendedSporulationAgarProtocol.md) | [template_name](template_name.md) | range | [DifcoAmendedSporulationAgarProtocolTemplateNameValue](DifcoAmendedSporulationAgarProtocolTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:DifcoAmendedSporulationAgarProtocolTemplateNameValue |
| native | microbial_experiment_schema:DifcoAmendedSporulationAgarProtocolTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DifcoAmendedSporulationAgarProtocolTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Difco Amended Sporulation Agar Protocol experiment
title: Difco Amended Sporulation Agar Protocol Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Difco Amended Sporulation Agar Protocol$

```
</details>

### Induced

<details>
```yaml
name: DifcoAmendedSporulationAgarProtocolTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Difco Amended Sporulation Agar Protocol experiment
title: Difco Amended Sporulation Agar Protocol Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Difco Amended Sporulation Agar Protocol$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: DifcoAmendedSporulationAgarProtocolTemplateNameValue
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
    pattern: ^Difco Amended Sporulation Agar Protocol$

```
</details>


# Class: Cell Culture In Broth Template Name Value (CellCultureInBrothTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a Cell Culture in Broth experiment_







URI: [microbial_experiment_schema:CellCultureInBrothTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/CellCultureInBrothTemplateNameValue)






```mermaid
 classDiagram
    class CellCultureInBrothTemplateNameValue
    click CellCultureInBrothTemplateNameValue href "../CellCultureInBrothTemplateNameValue"
      StringValue <|-- CellCultureInBrothTemplateNameValue
        click StringValue href "../StringValue"
      
      CellCultureInBrothTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **CellCultureInBrothTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CellCultureInBroth](CellCultureInBroth.md) | [template_name](template_name.md) | range | [CellCultureInBrothTemplateNameValue](CellCultureInBrothTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:CellCultureInBrothTemplateNameValue |
| native | microbial_experiment_schema:CellCultureInBrothTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CellCultureInBrothTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Cell Culture in Broth experiment
title: Cell Culture In Broth Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Cell Culture in Broth$

```
</details>

### Induced

<details>
```yaml
name: CellCultureInBrothTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Cell Culture in Broth experiment
title: Cell Culture In Broth Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Cell Culture in Broth$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: CellCultureInBrothTemplateNameValue
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
    pattern: ^Cell Culture in Broth$

```
</details>
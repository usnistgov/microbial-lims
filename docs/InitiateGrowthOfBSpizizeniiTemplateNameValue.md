

# Class: Initiate Growth of B spizizenii Template Name Value (InitiateGrowthOfBSpizizeniiTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a Initiate Growth of B spizizenii experiment_







URI: [microbial_experiment_schema:InitiateGrowthOfBSpizizeniiTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/InitiateGrowthOfBSpizizeniiTemplateNameValue)






```mermaid
 classDiagram
    class InitiateGrowthOfBSpizizeniiTemplateNameValue
    click InitiateGrowthOfBSpizizeniiTemplateNameValue href "../InitiateGrowthOfBSpizizeniiTemplateNameValue"
      StringValue <|-- InitiateGrowthOfBSpizizeniiTemplateNameValue
        click StringValue href "../StringValue"
      
      InitiateGrowthOfBSpizizeniiTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **InitiateGrowthOfBSpizizeniiTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | [template_name](template_name.md) | range | [InitiateGrowthOfBSpizizeniiTemplateNameValue](InitiateGrowthOfBSpizizeniiTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:InitiateGrowthOfBSpizizeniiTemplateNameValue |
| native | microbial_experiment_schema:InitiateGrowthOfBSpizizeniiTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InitiateGrowthOfBSpizizeniiTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Initiate Growth of B spizizenii experiment
title: Initiate Growth of B spizizenii Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Initiate Growth of B spizizenii$

```
</details>

### Induced

<details>
```yaml
name: InitiateGrowthOfBSpizizeniiTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Initiate Growth of B spizizenii experiment
title: Initiate Growth of B spizizenii Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Initiate Growth of B spizizenii$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: InitiateGrowthOfBSpizizeniiTemplateNameValue
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
    pattern: ^Initiate Growth of B spizizenii$

```
</details>
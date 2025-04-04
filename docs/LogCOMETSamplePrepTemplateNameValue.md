

# Class: LogCOMET Sample Prep Template Name Value (LogCOMETSamplePrepTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a LogCOMET_SamplePrep experiment_







URI: [microbial_experiment_schema:LogCOMETSamplePrepTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/LogCOMETSamplePrepTemplateNameValue)






```mermaid
 classDiagram
    class LogCOMETSamplePrepTemplateNameValue
    click LogCOMETSamplePrepTemplateNameValue href "../LogCOMETSamplePrepTemplateNameValue"
      StringValue <|-- LogCOMETSamplePrepTemplateNameValue
        click StringValue href "../StringValue"
      
      LogCOMETSamplePrepTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **LogCOMETSamplePrepTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [LogCOMETSamplePrep](LogCOMETSamplePrep.md) | [template_name](template_name.md) | range | [LogCOMETSamplePrepTemplateNameValue](LogCOMETSamplePrepTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:LogCOMETSamplePrepTemplateNameValue |
| native | microbial_experiment_schema:LogCOMETSamplePrepTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LogCOMETSamplePrepTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a LogCOMET_SamplePrep experiment
title: LogCOMET Sample Prep Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^LogCOMET_SamplePrep$

```
</details>

### Induced

<details>
```yaml
name: LogCOMETSamplePrepTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a LogCOMET_SamplePrep experiment
title: LogCOMET Sample Prep Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^LogCOMET_SamplePrep$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: LogCOMETSamplePrepTemplateNameValue
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
    pattern: ^LogCOMET_SamplePrep$

```
</details>
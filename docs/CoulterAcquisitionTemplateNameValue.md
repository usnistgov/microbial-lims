

# Class: Coulter Acquisition Template Name Value (CoulterAcquisitionTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a Coulter_Acquisition experiment_







URI: [microbial_experiment_schema:CoulterAcquisitionTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/CoulterAcquisitionTemplateNameValue)






```mermaid
 classDiagram
    class CoulterAcquisitionTemplateNameValue
    click CoulterAcquisitionTemplateNameValue href "../CoulterAcquisitionTemplateNameValue"
      StringValue <|-- CoulterAcquisitionTemplateNameValue
        click StringValue href "../StringValue"
      
      CoulterAcquisitionTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **CoulterAcquisitionTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CoulterAcquisition](CoulterAcquisition.md) | [template_name](template_name.md) | range | [CoulterAcquisitionTemplateNameValue](CoulterAcquisitionTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:CoulterAcquisitionTemplateNameValue |
| native | microbial_experiment_schema:CoulterAcquisitionTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CoulterAcquisitionTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Coulter_Acquisition experiment
title: Coulter Acquisition Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Coulter_Acquisition$

```
</details>

### Induced

<details>
```yaml
name: CoulterAcquisitionTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Coulter_Acquisition experiment
title: Coulter Acquisition Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Coulter_Acquisition$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: CoulterAcquisitionTemplateNameValue
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
    pattern: ^Coulter_Acquisition$

```
</details>
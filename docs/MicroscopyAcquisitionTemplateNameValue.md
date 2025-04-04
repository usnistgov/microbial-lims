

# Class: Microscopy Acquisition Template Name Value (MicroscopyAcquisitionTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a Microscopy_Acquisition experiment_







URI: [microbial_experiment_schema:MicroscopyAcquisitionTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/MicroscopyAcquisitionTemplateNameValue)






```mermaid
 classDiagram
    class MicroscopyAcquisitionTemplateNameValue
    click MicroscopyAcquisitionTemplateNameValue href "../MicroscopyAcquisitionTemplateNameValue"
      StringValue <|-- MicroscopyAcquisitionTemplateNameValue
        click StringValue href "../StringValue"
      
      MicroscopyAcquisitionTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **MicroscopyAcquisitionTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [template_name](template_name.md) | range | [MicroscopyAcquisitionTemplateNameValue](MicroscopyAcquisitionTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:MicroscopyAcquisitionTemplateNameValue |
| native | microbial_experiment_schema:MicroscopyAcquisitionTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MicroscopyAcquisitionTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Microscopy_Acquisition experiment
title: Microscopy Acquisition Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Microscopy_Acquisition$

```
</details>

### Induced

<details>
```yaml
name: MicroscopyAcquisitionTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a Microscopy_Acquisition experiment
title: Microscopy Acquisition Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^Microscopy_Acquisition$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: MicroscopyAcquisitionTemplateNameValue
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
    pattern: ^Microscopy_Acquisition$

```
</details>


# Class: CytoFLEX Acquisition Template Name Value (CytoFLEXAcquisitionTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a CytoFLEX_Acquisition experiment_







URI: [microbial_experiment_schema:CytoFLEXAcquisitionTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/CytoFLEXAcquisitionTemplateNameValue)






```mermaid
 classDiagram
    class CytoFLEXAcquisitionTemplateNameValue
    click CytoFLEXAcquisitionTemplateNameValue href "../CytoFLEXAcquisitionTemplateNameValue"
      StringValue <|-- CytoFLEXAcquisitionTemplateNameValue
        click StringValue href "../StringValue"
      
      CytoFLEXAcquisitionTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **CytoFLEXAcquisitionTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | [template_name](template_name.md) | range | [CytoFLEXAcquisitionTemplateNameValue](CytoFLEXAcquisitionTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:CytoFLEXAcquisitionTemplateNameValue |
| native | microbial_experiment_schema:CytoFLEXAcquisitionTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CytoFLEXAcquisitionTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a CytoFLEX_Acquisition experiment
title: CytoFLEX Acquisition Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^CytoFLEX_Acquisition$

```
</details>

### Induced

<details>
```yaml
name: CytoFLEXAcquisitionTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a CytoFLEX_Acquisition experiment
title: CytoFLEX Acquisition Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: ^CytoFLEX_Acquisition$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: CytoFLEXAcquisitionTemplateNameValue
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
    pattern: ^CytoFLEX_Acquisition$

```
</details>
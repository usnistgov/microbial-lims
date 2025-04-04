

# Class: BactoBox Acquisition Template Name Value (BactoBoxAcquisitionTemplateNameValue)




_An override of StringValue specified an allowed value for the template_name for a BactoBox_Acquisition experiment_







URI: [microbial_experiment_schema:BactoBoxAcquisitionTemplateNameValue](https://w3id.org/usnistgov/microbial-experiment-schema/BactoBoxAcquisitionTemplateNameValue)






```mermaid
 classDiagram
    class BactoBoxAcquisitionTemplateNameValue
    click BactoBoxAcquisitionTemplateNameValue href "../BactoBoxAcquisitionTemplateNameValue"
      StringValue <|-- BactoBoxAcquisitionTemplateNameValue
        click StringValue href "../StringValue"
      
      BactoBoxAcquisitionTemplateNameValue : value
        
      
```





## Inheritance
* [StringValue](StringValue.md)
    * **BactoBoxAcquisitionTemplateNameValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The actual metadata value for an attribute | [StringValue](StringValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | [template_name](template_name.md) | range | [BactoBoxAcquisitionTemplateNameValue](BactoBoxAcquisitionTemplateNameValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:BactoBoxAcquisitionTemplateNameValue |
| native | microbial_experiment_schema:BactoBoxAcquisitionTemplateNameValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BactoBoxAcquisitionTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a BactoBox_Acquisition experiment
title: BactoBox Acquisition Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: BactoBox_Acquisition$

```
</details>

### Induced

<details>
```yaml
name: BactoBoxAcquisitionTemplateNameValue
description: An override of StringValue specified an allowed value for the template_name
  for a BactoBox_Acquisition experiment
title: BactoBox Acquisition Template Name Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: StringValue
slot_usage:
  value:
    name: value
    range: string
    required: true
    pattern: BactoBox_Acquisition$
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: BactoBoxAcquisitionTemplateNameValue
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
    pattern: BactoBox_Acquisition$

```
</details>


# Class: Series Image Types Value (SeriesImageTypesValue)




_An override of ArrayValue allowing only values from the ImageTypeEnum enum_







URI: [microbial_experiment_schema:SeriesImageTypesValue](https://w3id.org/usnistgov/microbial-experiment-schema/SeriesImageTypesValue)






```mermaid
 classDiagram
    class SeriesImageTypesValue
    click SeriesImageTypesValue href "../SeriesImageTypesValue"
      ArrayValue <|-- SeriesImageTypesValue
        click ArrayValue href "../ArrayValue"
      
      SeriesImageTypesValue : value
        
          
    
    
    SeriesImageTypesValue --> "1..*" ImageTypeEnum : value
    click ImageTypeEnum href "../ImageTypeEnum"

        
      
```





## Inheritance
* [ArrayValue](ArrayValue.md)
    * **SeriesImageTypesValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1..* <br/> [ImageTypeEnum](ImageTypeEnum.md) | The actual metadata value for an attribute | [ArrayValue](ArrayValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [series_image_types](series_image_types.md) | range | [SeriesImageTypesValue](SeriesImageTypesValue.md) |
| [GenericTemplate](GenericTemplate.md) | [series_image_types](series_image_types.md) | range | [SeriesImageTypesValue](SeriesImageTypesValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:SeriesImageTypesValue |
| native | microbial_experiment_schema:SeriesImageTypesValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SeriesImageTypesValue
description: An override of ArrayValue allowing only values from the ImageTypeEnum
  enum
title: Series Image Types Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: ImageTypeEnum

```
</details>

### Induced

<details>
```yaml
name: SeriesImageTypesValue
description: An override of ArrayValue allowing only values from the ImageTypeEnum
  enum
title: Series Image Types Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: ImageTypeEnum
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: SeriesImageTypesValue
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
    range: ImageTypeEnum
    required: true
    multivalued: true
    inlined: false

```
</details>
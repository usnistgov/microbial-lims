

# Class: Microbial Material ID Value (MicrobialMaterialIDValue)




_A named sub-class of ArrayValue to hold a list of microbial material links_







URI: [microbial_experiment_schema:MicrobialMaterialIDValue](https://w3id.org/usnistgov/microbial-experiment-schema/MicrobialMaterialIDValue)






```mermaid
 classDiagram
    class MicrobialMaterialIDValue
    click MicrobialMaterialIDValue href "../MicrobialMaterialIDValue"
      ArrayValue <|-- MicrobialMaterialIDValue
        click ArrayValue href "../ArrayValue"
      
      MicrobialMaterialIDValue : value
        
          
    
    
    MicrobialMaterialIDValue --> "1..*" ELabItem : value
    click ELabItem href "../ELabItem"

        
      
```





## Inheritance
* [ArrayValue](ArrayValue.md)
    * **MicrobialMaterialIDValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1..* <br/> [ELabItem](ELabItem.md) | The actual metadata value for an attribute | [ArrayValue](ArrayValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |
| [CellCultureInBroth](CellCultureInBroth.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |
| [FormaldehydeFixation](FormaldehydeFixation.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |
| [GenericTemplate](GenericTemplate.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |
| [CoulterAcquisition](CoulterAcquisition.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |
| [LogCOMETSamplePrep](LogCOMETSamplePrep.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |
| [CFU](CFU.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | [microbial_material_id](microbial_material_id.md) | range | [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:MicrobialMaterialIDValue |
| native | microbial_experiment_schema:MicrobialMaterialIDValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MicrobialMaterialIDValue
description: A named sub-class of ArrayValue to hold a list of microbial material
  links
title: Microbial Material ID Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: ELabItem
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: MicrobialMaterialIDValue
description: A named sub-class of ArrayValue to hold a list of microbial material
  links
title: Microbial Material ID Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    range: ELabItem
    inlined: true
    inlined_as_list: true
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: MicrobialMaterialIDValue
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
    range: ELabItem
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>
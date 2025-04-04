

# Class: Fluorescent Probe Value (FluorescentProbeValue)




_An override of ArrayValue allowing only ELabItem values_







URI: [microbial_experiment_schema:FluorescentProbeValue](https://w3id.org/usnistgov/microbial-experiment-schema/FluorescentProbeValue)






```mermaid
 classDiagram
    class FluorescentProbeValue
    click FluorescentProbeValue href "../FluorescentProbeValue"
      ArrayValue <|-- FluorescentProbeValue
        click ArrayValue href "../ArrayValue"
      
      FluorescentProbeValue : value
        
          
    
    
    FluorescentProbeValue --> "1..*" ELabItem : value
    click ELabItem href "../ELabItem"

        
      
```





## Inheritance
* [ArrayValue](ArrayValue.md)
    * **FluorescentProbeValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1..* <br/> [ELabItem](ELabItem.md) | The value attribute for FluorescentProbe | [ArrayValue](ArrayValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | [fluorescent_probe](fluorescent_probe.md) | range | [FluorescentProbeValue](FluorescentProbeValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [fluorescent_probe](fluorescent_probe.md) | range | [FluorescentProbeValue](FluorescentProbeValue.md) |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [fluorescent_probe](fluorescent_probe.md) | range | [FluorescentProbeValue](FluorescentProbeValue.md) |
| [GenericTemplate](GenericTemplate.md) | [fluorescent_probe](fluorescent_probe.md) | range | [FluorescentProbeValue](FluorescentProbeValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:FluorescentProbeValue |
| native | microbial_experiment_schema:FluorescentProbeValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FluorescentProbeValue
description: An override of ArrayValue allowing only ELabItem values
title: Fluorescent Probe Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    description: The value attribute for FluorescentProbe
    range: ELabItem
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: FluorescentProbeValue
description: An override of ArrayValue allowing only ELabItem values
title: Fluorescent Probe Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ArrayValue
slot_usage:
  value:
    name: value
    description: The value attribute for FluorescentProbe
    range: ELabItem
    inlined: true
    inlined_as_list: true
attributes:
  value:
    name: value
    description: The value attribute for FluorescentProbe
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: FluorescentProbeValue
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
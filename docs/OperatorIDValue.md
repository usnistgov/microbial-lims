

# Class: Operator ID Value (OperatorIDValue)




_A named sub-class of ELabItemValue to hold an operator identifier value_







URI: [microbial_experiment_schema:OperatorIDValue](https://w3id.org/usnistgov/microbial-experiment-schema/OperatorIDValue)






```mermaid
 classDiagram
    class OperatorIDValue
    click OperatorIDValue href "../OperatorIDValue"
      ELabItemValue <|-- OperatorIDValue
        click ELabItemValue href "../ELabItemValue"
      
      OperatorIDValue : value
        
          
    
    
    OperatorIDValue --> "1" ELabItem : value
    click ELabItem href "../ELabItem"

        
      
```





## Inheritance
* [ELabItemValue](ELabItemValue.md)
    * **OperatorIDValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [ELabItem](ELabItem.md) | The actual metadata value for an attribute | [ELabItemValue](ELabItemValue.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Experiment](Experiment.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [ExperimentWithData](ExperimentWithData.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [ExperimentWithInstrument](ExperimentWithInstrument.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [ExperimentWithInstrumentNoData](ExperimentWithInstrumentNoData.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [CellCultureInBroth](CellCultureInBroth.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [FormaldehydeFixation](FormaldehydeFixation.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [GenericTemplate](GenericTemplate.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [CoulterAcquisition](CoulterAcquisition.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [LogCOMETSamplePrep](LogCOMETSamplePrep.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [CFU](CFU.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [DifcoAmendedSporulationAgarProtocol](DifcoAmendedSporulationAgarProtocol.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |
| [SlideCleaning](SlideCleaning.md) | [operator_id](operator_id.md) | range | [OperatorIDValue](OperatorIDValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:OperatorIDValue |
| native | microbial_experiment_schema:OperatorIDValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OperatorIDValue
description: A named sub-class of ELabItemValue to hold an operator identifier value
title: Operator ID Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ELabItemValue

```
</details>

### Induced

<details>
```yaml
name: OperatorIDValue
description: A named sub-class of ELabItemValue to hold an operator identifier value
title: Operator ID Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ELabItemValue
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: OperatorIDValue
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
    inlined: true

```
</details>
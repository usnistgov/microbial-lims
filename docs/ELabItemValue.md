

# Class: ELabFTW Item Value (ELabItemValue)




_A class to hold a reference to an item record in ELabFTW_







URI: [microbial_experiment_schema:ELabItemValue](https://w3id.org/usnistgov/microbial-experiment-schema/ELabItemValue)






```mermaid
 classDiagram
    class ELabItemValue
    click ELabItemValue href "../ELabItemValue"
      ELabItemValue <|-- InstrumentIDValue
        click InstrumentIDValue href "../InstrumentIDValue"
      ELabItemValue <|-- LabCASInstrumentValue
        click LabCASInstrumentValue href "../LabCASInstrumentValue"
      ELabItemValue <|-- LabCASOperatorValue
        click LabCASOperatorValue href "../LabCASOperatorValue"
      ELabItemValue <|-- LabCASProjectValue
        click LabCASProjectValue href "../LabCASProjectValue"
      ELabItemValue <|-- OperatorIDValue
        click OperatorIDValue href "../OperatorIDValue"
      ELabItemValue <|-- ProjectIDValue
        click ProjectIDValue href "../ProjectIDValue"
      
      ELabItemValue : value
        
          
    
    
    ELabItemValue --> "1" ELabItem : value
    click ELabItem href "../ELabItem"

        
      
```





## Inheritance
* **ELabItemValue**
    * [InstrumentIDValue](InstrumentIDValue.md)
    * [LabCASInstrumentValue](LabCASInstrumentValue.md)
    * [LabCASOperatorValue](LabCASOperatorValue.md)
    * [LabCASProjectValue](LabCASProjectValue.md)
    * [OperatorIDValue](OperatorIDValue.md)
    * [ProjectIDValue](ProjectIDValue.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [ELabItem](ELabItem.md) | The actual metadata value for an attribute | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Experiment](Experiment.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [ExperimentWithData](ExperimentWithData.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [ExperimentWithInstrument](ExperimentWithInstrument.md) | [instrument_id](instrument_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [ExperimentWithInstrument](ExperimentWithInstrument.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [ExperimentWithInstrumentNoData](ExperimentWithInstrumentNoData.md) | [instrument_id](instrument_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [ExperimentWithInstrumentNoData](ExperimentWithInstrumentNoData.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | [instrument_id](instrument_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | [kit_lot_number](kit_lot_number.md) | range | [ELabItemValue](ELabItemValue.md) |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | [instrument_id](instrument_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [CellCultureInBroth](CellCultureInBroth.md) | [growth_media_name](growth_media_name.md) | range | [ELabItemValue](ELabItemValue.md) |
| [CellCultureInBroth](CellCultureInBroth.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | [instrument_id](instrument_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [diluent_name](diluent_name.md) | range | [ELabItemValue](ELabItemValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [growth_media_name](growth_media_name.md) | range | [ELabItemValue](ELabItemValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [kit_lot_number](kit_lot_number.md) | range | [ELabItemValue](ELabItemValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [instrument_id](instrument_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [FormaldehydeFixation](FormaldehydeFixation.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [instrument_id](instrument_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [GenericTemplate](GenericTemplate.md) | [growth_media_name](growth_media_name.md) | range | [ELabItemValue](ELabItemValue.md) |
| [GenericTemplate](GenericTemplate.md) | [kit_lot_number](kit_lot_number.md) | range | [ELabItemValue](ELabItemValue.md) |
| [GenericTemplate](GenericTemplate.md) | [instrument_id](instrument_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [GenericTemplate](GenericTemplate.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [CoulterAcquisition](CoulterAcquisition.md) | [instrument_id](instrument_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [CoulterAcquisition](CoulterAcquisition.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | [instrument_id](instrument_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [LogCOMETSamplePrep](LogCOMETSamplePrep.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [CFU](CFU.md) | [growth_media_name](growth_media_name.md) | range | [ELabItemValue](ELabItemValue.md) |
| [CFU](CFU.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [DifcoAmendedSporulationAgarProtocol](DifcoAmendedSporulationAgarProtocol.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | [growth_media_name](growth_media_name.md) | range | [ELabItemValue](ELabItemValue.md) |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |
| [SlideCleaning](SlideCleaning.md) | [project_id](project_id.md) | range | [ELabItemValue](ELabItemValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:ELabItemValue |
| native | microbial_experiment_schema:ELabItemValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ELabItemValue
description: A class to hold a reference to an item record in ELabFTW
title: ELabFTW Item Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
slots:
- value
slot_usage:
  value:
    name: value
    range: ELabItem
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: ELabItemValue
description: A class to hold a reference to an item record in ELabFTW
title: ELabFTW Item Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
slot_usage:
  value:
    name: value
    range: ELabItem
    inlined: true
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: ELabItemValue
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


# Slot: InstrumentID (instrument_id)




_The instrument used to acquire the data in an experiment (linked item from ELabFTW)_







URI: [microbial_experiment_schema:instrument_id](https://w3id.org/usnistgov/microbial-experiment-schema/instrument_id)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [ExperimentWithInstrumentNoData](ExperimentWithInstrumentNoData.md) | Holds information about a specific type of Microbial Strain experiment that uses an instrument but does not collect data. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | Metadata describing a nucleic acid extraction experiment |  no  |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | Metadata describing a data acquisition experiment using the BactoBox |  no  |
| [ExperimentWithInstrument](ExperimentWithInstrument.md) | Holds information about a specific type of Microbial Strain experiment that uses an instrument. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [CoulterAcquisition](CoulterAcquisition.md) | Metadata describing a Coulter counter acquisition experiment |  no  |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | Metadata describing a volume calibration using the CytoFLEX instrument |  no  |







## Properties

* Range: [ELabItemValue](ELabItemValue.md)

* Required: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| elabftw_group | LabCAS || elabftw_user_input | True |



### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:instrument_id |
| native | microbial_experiment_schema:instrument_id |




## LinkML Source

<details>
```yaml
name: instrument_id
annotations:
  elabftw_group:
    tag: elabftw_group
    value: LabCAS
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
description: The instrument used to acquire the data in an experiment (linked item
  from ELabFTW)
title: InstrumentID
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: instrument_id
domain_of:
- ExperimentWithInstrument
- ExperimentWithInstrumentNoData
range: ELabItemValue
required: true

```
</details>


# Slot: ProjectID (project_id)




_The project that an experiment supports (link to an ELabFTW item)_







URI: [microbial_experiment_schema:project_id](https://w3id.org/usnistgov/microbial-experiment-schema/project_id)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [SlideCleaning](SlideCleaning.md) | Metadata describing an experiment preparing microscopy slides for microbial work |  no  |
| [CFU](CFU.md) | Metadata describing a colony forming unit counting experiment |  no  |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | Metadata describing a nucleic acid extraction experiment |  no  |
| [ExperimentWithData](ExperimentWithData.md) | Holds information about a specific type of Microbial Strain experiment that results in the collection of data. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [Experiment](Experiment.md) | Holds information about a specific type of Microbial Strain experiment. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [CellCultureInBroth](CellCultureInBroth.md) | Metadata describing a cell culture experiment |  no  |
| [ExperimentWithInstrument](ExperimentWithInstrument.md) | Holds information about a specific type of Microbial Strain experiment that uses an instrument. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [DifcoAmendedSporulationAgarProtocol](DifcoAmendedSporulationAgarProtocol.md) | Metadata describing the preparation process for amended sporulation agar |  no  |
| [FormaldehydeFixation](FormaldehydeFixation.md) | Metadata describing a formaldehyde fixation experiment |  no  |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | Metadata describing a volume calibration using the CytoFLEX instrument |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [ExperimentWithInstrumentNoData](ExperimentWithInstrumentNoData.md) | Holds information about a specific type of Microbial Strain experiment that uses an instrument but does not collect data. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | Metadata describing an initiate growth experiment of B. spizizenii |  no  |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | Metadata describing a data acquisition experiment using the BactoBox |  no  |
| [CoulterAcquisition](CoulterAcquisition.md) | Metadata describing a Coulter counter acquisition experiment |  no  |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |
| [LogCOMETSamplePrep](LogCOMETSamplePrep.md) | Metadata describing a sample preparation process for a LOGComet experiment |  no  |







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
| self | microbial_experiment_schema:project_id |
| native | microbial_experiment_schema:project_id |




## LinkML Source

<details>
```yaml
name: project_id
annotations:
  elabftw_group:
    tag: elabftw_group
    value: LabCAS
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
description: The project that an experiment supports (link to an ELabFTW item)
title: ProjectID
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: project_id
domain_of:
- Experiment
range: ELabItemValue
required: true

```
</details>
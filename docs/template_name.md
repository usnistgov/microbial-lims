

# Slot: TemplateName (template_name)




_The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed._







URI: [microbial_experiment_schema:template_name](https://w3id.org/usnistgov/microbial-experiment-schema/template_name)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [SlideCleaning](SlideCleaning.md) | Metadata describing an experiment preparing microscopy slides for microbial work |  yes  |
| [CFU](CFU.md) | Metadata describing a colony forming unit counting experiment |  yes  |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | Metadata describing a nucleic acid extraction experiment |  yes  |
| [ExperimentWithData](ExperimentWithData.md) | Holds information about a specific type of Microbial Strain experiment that results in the collection of data. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [Experiment](Experiment.md) | Holds information about a specific type of Microbial Strain experiment. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [CellCultureInBroth](CellCultureInBroth.md) | Metadata describing a cell culture experiment |  yes  |
| [ExperimentWithInstrument](ExperimentWithInstrument.md) | Holds information about a specific type of Microbial Strain experiment that uses an instrument. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [DifcoAmendedSporulationAgarProtocol](DifcoAmendedSporulationAgarProtocol.md) | Metadata describing the preparation process for amended sporulation agar |  yes  |
| [FormaldehydeFixation](FormaldehydeFixation.md) | Metadata describing a formaldehyde fixation experiment |  yes  |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | Metadata describing a volume calibration using the CytoFLEX instrument |  yes  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [ExperimentWithInstrumentNoData](ExperimentWithInstrumentNoData.md) | Holds information about a specific type of Microbial Strain experiment that uses an instrument but does not collect data. The specific metadata for each type of experiment is controlled by "template data classes" |  no  |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | Metadata describing an initiate growth experiment of B. spizizenii |  yes  |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | Metadata describing a data acquisition experiment using the BactoBox |  yes  |
| [CoulterAcquisition](CoulterAcquisition.md) | Metadata describing a Coulter counter acquisition experiment |  yes  |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  yes  |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  yes  |
| [LogCOMETSamplePrep](LogCOMETSamplePrep.md) | Metadata describing a sample preparation process for a LOGComet experiment |  yes  |







## Properties

* Range: [StringValue](StringValue.md)

* Required: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| elabftw_group | LabCAS || read_only | True || elabftw_user_input | True |



### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:template_name |
| native | microbial_experiment_schema:template_name |




## LinkML Source

<details>
```yaml
name: template_name
annotations:
  elabftw_group:
    tag: elabftw_group
    value: LabCAS
  read_only:
    tag: read_only
    value: true
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
description: The name of the template used to collect metadata for an experiment in
  ELabFTW. This value controls what specific metadata fields are allowed.
title: TemplateName
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: template_name
domain_of:
- Experiment
range: StringValue
required: true

```
</details>
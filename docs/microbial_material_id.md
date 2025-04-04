

# Slot: MicrobialMaterialID (microbial_material_id)




_Cell material(s) used in experiment as named in the eLabFTW database (linked items)_







URI: [microbial_experiment_schema:microbial_material_id](https://w3id.org/usnistgov/microbial-experiment-schema/microbial_material_id)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [CFU](CFU.md) | Metadata describing a colony forming unit counting experiment |  no  |
| [CoulterAcquisition](CoulterAcquisition.md) | Metadata describing a Coulter counter acquisition experiment |  no  |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [CellCultureInBroth](CellCultureInBroth.md) | Metadata describing a cell culture experiment |  no  |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | Metadata describing an initiate growth experiment of B. spizizenii |  no  |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | Metadata describing a nucleic acid extraction experiment |  no  |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | Metadata describing a data acquisition experiment using the BactoBox |  no  |
| [FormaldehydeFixation](FormaldehydeFixation.md) | Metadata describing a formaldehyde fixation experiment |  no  |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |
| [LogCOMETSamplePrep](LogCOMETSamplePrep.md) | Metadata describing a sample preparation process for a LOGComet experiment |  no  |







## Properties

* Range: [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md)





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
| self | microbial_experiment_schema:microbial_material_id |
| native | microbial_experiment_schema:microbial_material_id |




## LinkML Source

<details>
```yaml
name: microbial_material_id
annotations:
  elabftw_group:
    tag: elabftw_group
    value: LabCAS
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
description: Cell material(s) used in experiment as named in the eLabFTW database
  (linked items)
title: MicrobialMaterialID
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: microbial_material_id
domain_of:
- CytoFLEXAcquisition
- NucleicAcidExtraction
- CellCultureInBroth
- GenericTemplateDeprecated
- FormaldehydeFixation
- MicroscopyAcquisition
- GenericTemplate
- CoulterAcquisition
- BactoBoxAcquisition
- LogCOMETSamplePrep
- CFU
- InitiateGrowthOfBSpizizenii
range: MicrobialMaterialIDValue
required: false

```
</details>
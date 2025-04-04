

# Slot: Modalities (modalities)




_The type (modality) of a microscopy acquisition experiment_







URI: [microbial_experiment_schema:modalities](https://w3id.org/usnistgov/microbial-experiment-schema/modalities)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |







## Properties

* Range: [ModalitiesValue](ModalitiesValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:modalities |
| native | microbial_experiment_schema:modalities |




## LinkML Source

<details>
```yaml
name: modalities
description: The type (modality) of a microscopy acquisition experiment
title: Modalities
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: modalities
domain_of:
- MicroscopyAcquisition
- GenericTemplate
range: ModalitiesValue
required: false

```
</details>
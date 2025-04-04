

# Slot: SingleImages (single_images)




_Whether single images were acquired in an experiment_







URI: [microbial_experiment_schema:single_images](https://w3id.org/usnistgov/microbial-experiment-schema/single_images)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |







## Properties

* Range: [BooleanValue](BooleanValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:single_images |
| native | microbial_experiment_schema:single_images |




## LinkML Source

<details>
```yaml
name: single_images
description: Whether single images were acquired in an experiment
title: SingleImages
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: single_images
domain_of:
- MicroscopyAcquisition
- GenericTemplate
range: BooleanValue
required: false

```
</details>
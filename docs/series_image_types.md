

# Slot: SeriesImageTypes (series_image_types)




_The types of series images acquired in an experiment_







URI: [microbial_experiment_schema:series_image_types](https://w3id.org/usnistgov/microbial-experiment-schema/series_image_types)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |







## Properties

* Range: [SeriesImageTypesValue](SeriesImageTypesValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:series_image_types |
| native | microbial_experiment_schema:series_image_types |




## LinkML Source

<details>
```yaml
name: series_image_types
description: The types of series images acquired in an experiment
title: SeriesImageTypes
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: series_image_types
domain_of:
- MicroscopyAcquisition
- GenericTemplate
range: SeriesImageTypesValue
required: false

```
</details>
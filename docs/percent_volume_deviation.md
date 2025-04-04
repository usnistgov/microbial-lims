

# Slot: PercentVolumeDeviation (percent_volume_deviation)




_The volume deviation (measured volume divided by target volume) from a calibration experiment_







URI: [microbial_experiment_schema:percent_volume_deviation](https://w3id.org/usnistgov/microbial-experiment-schema/percent_volume_deviation)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | Metadata describing a volume calibration using the CytoFLEX instrument |  no  |







## Properties

* Range: [UnitlessValue](UnitlessValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:percent_volume_deviation |
| native | microbial_experiment_schema:percent_volume_deviation |




## LinkML Source

<details>
```yaml
name: percent_volume_deviation
description: The volume deviation (measured volume divided by target volume) from
  a calibration experiment
title: PercentVolumeDeviation
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: percent_volume_deviation
domain_of:
- CytoFLEXVolumeCalibration
- GenericTemplate
range: UnitlessValue
required: false

```
</details>
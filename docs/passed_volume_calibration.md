

# Slot: PassedVolumeCalibration (passed_volume_calibration)




_(?) The volume that is passed during a volume calibration_







URI: [microbial_experiment_schema:passed_volume_calibration](https://w3id.org/usnistgov/microbial-experiment-schema/passed_volume_calibration)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | Metadata describing a volume calibration using the CytoFLEX instrument |  no  |







## Properties

* Range: [BooleanValue](BooleanValue.md)





## TODOs

* double check description

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:passed_volume_calibration |
| native | microbial_experiment_schema:passed_volume_calibration |




## LinkML Source

<details>
```yaml
name: passed_volume_calibration
description: (?) The volume that is passed during a volume calibration
title: PassedVolumeCalibration
todos:
- double check description
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: passed_volume_calibration
domain_of:
- CytoFLEXVolumeCalibration
- GenericTemplate
range: BooleanValue
required: false

```
</details>
# Enum: ~~Transmission Mode Enum (TransmissionModeEnum)~~<span style="color: #ff5252;"><strong> (DEPRECATED) </strong></span>




_Allowed microscopy transmission mode values_




* __NOTE__ this element has been deprecated with the following note:
    * *(2024 June) this is too specific, use MicroscopyModalitiesEnum instead*
    * Element has been replaced by [MicroscopyModalitiesEnum](MicroscopyModalitiesEnum.md)


URI: [TransmissionModeEnum](TransmissionModeEnum.md)

## Permissible Values

| Name | Value | Description |
| --- | --- | --- |
| DIC | `None` | Digital Image Correlation |
| Brightfield | `None` | Brightfield imaging |
| Phase Contrast | `None` | Phase contrast imaging |




## Slots

| Name | Description |
| ---  | --- |
| [value](value.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema






## LinkML Source

<details>
```yaml
name: TransmissionModeEnum
description: Allowed microscopy transmission mode values
title: Transmission Mode Enum
deprecated: (2024 June) this is too specific, use MicroscopyModalitiesEnum instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: MicroscopyModalitiesEnum
rank: 1000
permissible_values:
  DIC:
    text: DIC
    description: Digital Image Correlation
  Brightfield:
    text: Brightfield
    description: Brightfield imaging
  Phase Contrast:
    text: Phase Contrast
    description: Phase contrast imaging

```
</details>

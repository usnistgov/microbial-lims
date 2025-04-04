# Enum: Image Type Enum (ImageTypeEnum)




_Allowed microscopy image type values_





URI: [ImageTypeEnum](ImageTypeEnum.md)

## Permissible Values

| Name | Value | Description |
| --- | --- | --- |
| Time lapse | `None` | Time lapse imagery |
| Area scan | `None` | A scan of an area |
| z stack | `None` | Z (focal) stack |
| NA | `None` | Not applicable |




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
name: ImageTypeEnum
description: Allowed microscopy image type values
title: Image Type Enum
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
permissible_values:
  Time lapse:
    text: Time lapse
    description: Time lapse imagery
  Area scan:
    text: Area scan
    description: A scan of an area
  z stack:
    text: z stack
    description: Z (focal) stack
  NA:
    text: NA
    description: Not applicable

```
</details>

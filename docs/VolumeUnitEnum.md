# Enum: Volume Unit Enum (VolumeUnitEnum)




_Allowed volume unit type values_





URI: [VolumeUnitEnum](VolumeUnitEnum.md)

## Permissible Values

| Name | Value | Description |
| --- | --- | --- |
| mL | `None` | milliliters |
| µL | `None` | microliters |




## Slots

| Name | Description |
| ---  | --- |
| [unit](unit.md) | The volume unit corresponding to a metadata value |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema






## LinkML Source

<details>
```yaml
name: VolumeUnitEnum
description: Allowed volume unit type values
title: Volume Unit Enum
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
permissible_values:
  mL:
    text: mL
    description: milliliters
    exact_mappings:
    - qudt:MilliL
  µL:
    text: µL
    description: microliters
    exact_mappings:
    - qudt:microL

```
</details>

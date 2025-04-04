# Enum: Temperature Unit Enum (TemperatureUnitEnum)




_Allowed temperature unit type values_





URI: [TemperatureUnitEnum](TemperatureUnitEnum.md)

## Permissible Values

| Name | Value | Description |
| --- | --- | --- |
| oC | `°C` | degrees celsius |
| oF | `°F` | degrees fahrenheit |




## Slots

| Name | Description |
| ---  | --- |
| [unit](unit.md) | The temperature unit corresponding to a metadata value |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema






## LinkML Source

<details>
```yaml
name: TemperatureUnitEnum
description: Allowed temperature unit type values
title: Temperature Unit Enum
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
permissible_values:
  oC:
    text: oC
    description: degrees celsius
    title: °C
    exact_mappings:
    - qudt:DEG_C
  oF:
    text: oF
    description: degrees fahrenheit
    title: °F
    exact_mappings:
    - qudt:DEG_F

```
</details>

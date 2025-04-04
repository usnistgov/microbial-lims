# Enum: Duration Unit Enum (DurationUnitEnum)




_Allowed time duration unit type values_





URI: [DurationUnitEnum](DurationUnitEnum.md)

## Permissible Values

| Name | Value | Description |
| --- | --- | --- |
| sec | `None` | seconds |
| hr | `None` | hours |
| min | `None` | minutes |




## Slots

| Name | Description |
| ---  | --- |
| [unit](unit.md) | The time duration unit corresponding to a metadata value |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema






## LinkML Source

<details>
```yaml
name: DurationUnitEnum
description: Allowed time duration unit type values
title: Duration Unit Enum
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
permissible_values:
  sec:
    text: sec
    description: seconds
    exact_mappings:
    - qudt:SEC
  hr:
    text: hr
    description: hours
    exact_mappings:
    - qudt:HR
  min:
    text: min
    description: minutes
    exact_mappings:
    - qudt:MIN

```
</details>

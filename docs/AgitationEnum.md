# Enum: Agitation Enum (AgitationEnum)




_Allowed agitation speed unit type values_





URI: [AgitationEnum](AgitationEnum.md)

## Permissible Values

| Name | Value | Description |
| --- | --- | --- |
| rpm | `None` | revolutions per minute |
| x g | `None` | x g |




## Slots

| Name | Description |
| ---  | --- |
| [unit](unit.md) | The agitation speed unit corresponding to a metadata value |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema






## LinkML Source

<details>
```yaml
name: AgitationEnum
description: Allowed agitation speed unit type values
title: Agitation Enum
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
permissible_values:
  rpm:
    text: rpm
    description: revolutions per minute
  x g:
    text: x g
    description: x g
    todos:
    - Get better description of this value

```
</details>



# Slot: unit (unit)




_The unit corresponding to a metadata value_







URI: [microbial_experiment_schema:unit](https://w3id.org/usnistgov/microbial-experiment-schema/unit)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VolumeValue](VolumeValue.md) | A class to hold a numerical value representing a volumetric measurement |  yes  |
| [UnitlessValue](UnitlessValue.md) | A class to hold an explicitly unitless numerical value |  yes  |
| [FlowRateValue](FlowRateValue.md) | A class to hold a numerical value representing a flow rate measurement |  yes  |
| [AgitationValue](AgitationValue.md) | A class to hold a numerical value representing an agitation speed |  yes  |
| [LengthValue](LengthValue.md) | A class to hold a numerical value representing a linear measurement |  yes  |
| [TemperatureValue](TemperatureValue.md) | A class to hold a numerical value representing a temperature measurement |  yes  |
| [NumberValue](NumberValue.md) | A class to hold a numerical value with a free-text string as a unit |  yes  |
| [CountValue](CountValue.md) | A class to hold a numerical value representing a counting measurement |  yes  |
| [DurationValue](DurationValue.md) | A class to hold a numerical value representing a time duration measurement |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:unit |
| native | microbial_experiment_schema:unit |




## LinkML Source

<details>
```yaml
name: unit
description: The unit corresponding to a metadata value
title: unit
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: unit
domain_of:
- NumberValue
range: string
required: true

```
</details>


# Slot: ~~TransmissionMode (transmission_mode)~~<span style="color: #ff5252;"><strong> (DEPRECATED) </strong></span>




_The type (modality) of a microscopy acquisition experiment_






* __NOTE__ this element has been deprecated with the following note:
    * *(2024 June) this is too specific, use modalities instead*
    * Element has been replaced by [modalities](modalities.md)


URI: [microbial_experiment_schema:transmission_mode](https://w3id.org/usnistgov/microbial-experiment-schema/transmission_mode)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |







## Properties

* Range: [TransmissionModeValue](TransmissionModeValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:transmission_mode |
| native | microbial_experiment_schema:transmission_mode |




## LinkML Source

<details>
```yaml
name: transmission_mode
description: The type (modality) of a microscopy acquisition experiment
title: TransmissionMode
deprecated: (2024 June) this is too specific, use modalities instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: modalities
rank: 1000
alias: transmission_mode
domain_of:
- GenericTemplateDeprecated
range: TransmissionModeValue
required: false

```
</details>
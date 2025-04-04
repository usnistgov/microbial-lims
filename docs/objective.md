

# Slot: Objective (objective)




_The microscope objectives used in a microscopy acquisition experiment_







URI: [microbial_experiment_schema:objective](https://w3id.org/usnistgov/microbial-experiment-schema/objective)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |







## Properties

* Range: [ObjectivesValue](ObjectivesValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:objective |
| native | microbial_experiment_schema:objective |




## LinkML Source

<details>
```yaml
name: objective
description: The microscope objectives used in a microscopy acquisition experiment
title: Objective
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: objective
domain_of:
- GenericTemplateDeprecated
- MicroscopyAcquisition
- GenericTemplate
range: ObjectivesValue
required: false

```
</details>
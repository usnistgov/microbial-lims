

# Slot: StatusTitle (status_title)




_The status title of an ELabFTW resource_







URI: [microbial_experiment_schema:status_title](https://w3id.org/usnistgov/microbial-experiment-schema/status_title)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ELabRecord](ELabRecord.md) | An abstract data type representing a link to an record (experiment or resource/item) in an eLabFTW instance. Use one of the ELabItem or ELabRecord classes that implement this one rather than using it directly. |  no  |
| [ELabExperiment](ELabExperiment.md) | A class to hold metadata sufficient to reference an experiment record in an ELabFTW instance. |  no  |
| [ELabItem](ELabItem.md) | A class to hold metadata sufficient to reference a resource (database item) record in an ELabFTW instance. |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:status_title |
| native | microbial_experiment_schema:status_title |




## LinkML Source

<details>
```yaml
name: status_title
description: The status title of an ELabFTW resource
title: StatusTitle
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: status_title
domain_of:
- ELabRecord
range: string
required: true

```
</details>
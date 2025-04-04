

# Slot: id (id)




_The integer identifier for this item used by this eLabFTW instance_







URI: [microbial_experiment_schema:id](https://w3id.org/usnistgov/microbial-experiment-schema/id)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ELabRecord](ELabRecord.md) | An abstract data type representing a link to an record (experiment or resource/item) in an eLabFTW instance. Use one of the ELabItem or ELabRecord classes that implement this one rather than using it directly. |  no  |
| [ELabExperiment](ELabExperiment.md) | A class to hold metadata sufficient to reference an experiment record in an ELabFTW instance. |  no  |
| [ELabItem](ELabItem.md) | A class to hold metadata sufficient to reference a resource (database item) record in an ELabFTW instance. |  no  |







## Properties

* Range: [Integer](Integer.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:id |
| native | microbial_experiment_schema:id |




## LinkML Source

<details>
```yaml
name: id
description: The integer identifier for this item used by this eLabFTW instance
title: id
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
identifier: true
alias: id
owner: ELabRecord
domain_of:
- ELabRecord
range: integer
required: true

```
</details>


# Slot: API url (api_url)




_A URL for accessing this item via the eLabFTW API_







URI: [microbial_experiment_schema:api_url](https://w3id.org/usnistgov/microbial-experiment-schema/api_url)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ELabRecord](ELabRecord.md) | An abstract data type representing a link to an record (experiment or resource/item) in an eLabFTW instance. Use one of the ELabItem or ELabRecord classes that implement this one rather than using it directly. |  no  |
| [ELabExperiment](ELabExperiment.md) | A class to hold metadata sufficient to reference an experiment record in an ELabFTW instance. |  no  |
| [ELabItem](ELabItem.md) | A class to hold metadata sufficient to reference a resource (database item) record in an ELabFTW instance. |  no  |







## Properties

* Range: [Uri](Uri.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:api_url |
| native | microbial_experiment_schema:api_url |




## LinkML Source

<details>
```yaml
name: api_url
description: A URL for accessing this item via the eLabFTW API
title: API url
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: api_url
owner: ELabRecord
domain_of:
- ELabRecord
range: uri
required: true

```
</details>


# Slot: url (url)




_A (resolvable) URL for accessing this item via a web browser_







URI: [microbial_experiment_schema:url](https://w3id.org/usnistgov/microbial-experiment-schema/url)



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
| self | microbial_experiment_schema:url |
| native | microbial_experiment_schema:url |




## LinkML Source

<details>
```yaml
name: url
description: A (resolvable) URL for accessing this item via a web browser
title: url
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: url
owner: ELabRecord
domain_of:
- ELabRecord
range: uri
required: true

```
</details>
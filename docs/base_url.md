

# Slot: ELabFTW Base URL (base_url)




_The URL of the ELabFTW instance in which the user is registered_







URI: [microbial_experiment_schema:base_url](https://w3id.org/usnistgov/microbial-experiment-schema/base_url)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ELabUser](ELabUser.md) | A data type representing a link to a user in an eLabFTW instance |  no  |







## Properties

* Range: [Uri](Uri.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:base_url |
| native | microbial_experiment_schema:base_url |




## LinkML Source

<details>
```yaml
name: base_url
description: The URL of the ELabFTW instance in which the user is registered
title: ELabFTW Base URL
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: base_url
owner: ELabUser
domain_of:
- ELabUser
range: uri
required: true

```
</details>
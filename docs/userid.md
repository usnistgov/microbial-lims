

# Slot: User ID (userid)




_The "local" identifier number for this user in the eLabFTW instance_







URI: [microbial_experiment_schema:userid](https://w3id.org/usnistgov/microbial-experiment-schema/userid)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ELabUser](ELabUser.md) | A data type representing a link to a user in an eLabFTW instance |  no  |







## Properties

* Range: [Integer](Integer.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:userid |
| native | microbial_experiment_schema:userid |




## LinkML Source

<details>
```yaml
name: userid
description: The "local" identifier number for this user in the eLabFTW instance
title: User ID
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
identifier: true
alias: userid
owner: ELabUser
domain_of:
- ELabUser
range: integer
required: true

```
</details>
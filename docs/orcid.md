

# Slot: ORCID (orcid)




_The user's ORCID (if defined)_







URI: [microbial_experiment_schema:orcid](https://w3id.org/usnistgov/microbial-experiment-schema/orcid)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ELabUser](ELabUser.md) | A data type representing a link to a user in an eLabFTW instance |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:orcid |
| native | microbial_experiment_schema:orcid |




## LinkML Source

<details>
```yaml
name: orcid
description: The user's ORCID (if defined)
title: ORCID
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: orcid
owner: ELabUser
domain_of:
- ELabUser
range: string
required: false
pattern: ^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$

```
</details>
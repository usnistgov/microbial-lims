

# Slot: Email (email)




_The user's email address_







URI: [microbial_experiment_schema:email](https://w3id.org/usnistgov/microbial-experiment-schema/email)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ELabUser](ELabUser.md) | A data type representing a link to a user in an eLabFTW instance |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^\S+@[\S+\.]+\S+`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:email |
| native | microbial_experiment_schema:email |




## LinkML Source

<details>
```yaml
name: email
description: The user's email address
title: Email
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: email
owner: ELabUser
domain_of:
- ELabUser
range: string
required: true
pattern: ^\S+@[\S+\.]+\S+

```
</details>
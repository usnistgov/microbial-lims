

# Slot: LibraryPrep (library_prep)




_The name of a specific kit used for sequencing preparation steps_







URI: [microbial_experiment_schema:library_prep](https://w3id.org/usnistgov/microbial-experiment-schema/library_prep)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |







## Properties

* Range: [StringValue](StringValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:library_prep |
| native | microbial_experiment_schema:library_prep |




## LinkML Source

<details>
```yaml
name: library_prep
description: The name of a specific kit used for sequencing preparation steps
title: LibraryPrep
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: library_prep
domain_of:
- GenericTemplateDeprecated
- GenericTemplate
range: StringValue
required: false

```
</details>
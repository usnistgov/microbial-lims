

# Slot: NucleicAcidType (nucleic_acid_type)




_The type of nucleic acid used in an extraction experiment_







URI: [microbial_experiment_schema:nucleic_acid_type](https://w3id.org/usnistgov/microbial-experiment-schema/nucleic_acid_type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | Metadata describing a nucleic acid extraction experiment |  no  |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |







## Properties

* Range: [NucleicAcidTypeValue](NucleicAcidTypeValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:nucleic_acid_type |
| native | microbial_experiment_schema:nucleic_acid_type |




## LinkML Source

<details>
```yaml
name: nucleic_acid_type
description: The type of nucleic acid used in an extraction experiment
title: NucleicAcidType
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: nucleic_acid_type
domain_of:
- NucleicAcidExtraction
- GenericTemplateDeprecated
- GenericTemplate
range: NucleicAcidTypeValue
required: false

```
</details>
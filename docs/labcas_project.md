

# Slot: ~~LabCAS-Project (labcas_project)~~<span style="color: #ff5252;"><strong> (DEPRECATED) </strong></span>




_The project that an experiment supports (link to an ELabFTW item)_






* __NOTE__ this element has been deprecated with the following note:
    * *(2024 June) this is too specific, use project_id instead*
    * Element has been replaced by [project_id](project_id.md)


URI: [microbial_experiment_schema:labcas_project](https://w3id.org/usnistgov/microbial-experiment-schema/labcas_project)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |







## Properties

* Range: [LabCASProjectValue](LabCASProjectValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:labcas_project |
| native | microbial_experiment_schema:labcas_project |




## LinkML Source

<details>
```yaml
name: labcas_project
description: The project that an experiment supports (link to an ELabFTW item)
title: LabCAS-Project
deprecated: (2024 June) this is too specific, use project_id instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: project_id
rank: 1000
alias: labcas_project
domain_of:
- GenericTemplateDeprecated
range: LabCASProjectValue
required: false

```
</details>
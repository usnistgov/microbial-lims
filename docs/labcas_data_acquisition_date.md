

# Slot: ~~LabCAS-DataAcquisitionDate (labcas_data_acquisition_date)~~<span style="color: #ff5252;"><strong> (DEPRECATED) </strong></span>




_Date on which data were acquired according to eLabFTW record_






* __NOTE__ this element has been deprecated with the following note:
    * *(2024 June) this is too specific, use data_acquisition_date instead*
    * Element has been replaced by [data_acquisition_date](data_acquisition_date.md)


URI: [microbial_experiment_schema:labcas_data_acquisition_date](https://w3id.org/usnistgov/microbial-experiment-schema/labcas_data_acquisition_date)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |







## Properties

* Range: [DateValue](DateValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:labcas_data_acquisition_date |
| native | microbial_experiment_schema:labcas_data_acquisition_date |




## LinkML Source

<details>
```yaml
name: labcas_data_acquisition_date
description: Date on which data were acquired according to eLabFTW record
title: LabCAS-DataAcquisitionDate
deprecated: (2024 June) this is too specific, use data_acquisition_date instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: data_acquisition_date
rank: 1000
alias: labcas_data_acquisition_date
domain_of:
- GenericTemplateDeprecated
range: DateValue
required: false

```
</details>
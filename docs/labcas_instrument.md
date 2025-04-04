

# Slot: ~~LabCAS-Instrument (labcas_instrument)~~<span style="color: #ff5252;"><strong> (DEPRECATED) </strong></span>




_Date on which data were acquired according to eLabFTW record_






* __NOTE__ this element has been deprecated with the following note:
    * *(2024 June) this is too specific, use instrument_id instead*
    * Element has been replaced by [instrument_id](instrument_id.md)


URI: [microbial_experiment_schema:labcas_instrument](https://w3id.org/usnistgov/microbial-experiment-schema/labcas_instrument)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |







## Properties

* Range: [LabCASInstrumentValue](LabCASInstrumentValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:labcas_instrument |
| native | microbial_experiment_schema:labcas_instrument |




## LinkML Source

<details>
```yaml
name: labcas_instrument
description: Date on which data were acquired according to eLabFTW record
title: LabCAS-Instrument
deprecated: (2024 June) this is too specific, use instrument_id instead
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
deprecated_element_has_exact_replacement: instrument_id
rank: 1000
alias: labcas_instrument
domain_of:
- GenericTemplateDeprecated
range: LabCASInstrumentValue
required: false

```
</details>
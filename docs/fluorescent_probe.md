

# Slot: FluorescentProbe (fluorescent_probe)




_Fluorescent probe(s) used in the experiment, as linked item(s) from ELabFTW_







URI: [microbial_experiment_schema:fluorescent_probe](https://w3id.org/usnistgov/microbial-experiment-schema/fluorescent_probe)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |  no  |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |  no  |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | A retired version of a generic experiment template used to create other templates |  no  |
| [GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |  no  |







## Properties

* Range: [FluorescentProbeValue](FluorescentProbeValue.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| elabftw_group | Generic Microbial || elabftw_user_input | True |



### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:fluorescent_probe |
| native | microbial_experiment_schema:fluorescent_probe |




## LinkML Source

<details>
```yaml
name: fluorescent_probe
annotations:
  elabftw_group:
    tag: elabftw_group
    value: Generic Microbial
  elabftw_user_input:
    tag: elabftw_user_input
    value: true
description: Fluorescent probe(s) used in the experiment, as linked item(s) from ELabFTW
title: FluorescentProbe
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
rank: 1000
alias: fluorescent_probe
domain_of:
- CytoFLEXAcquisition
- GenericTemplateDeprecated
- MicroscopyAcquisition
- GenericTemplate
range: FluorescentProbeValue
required: false

```
</details>
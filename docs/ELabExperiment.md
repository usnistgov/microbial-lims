

# Class: ELabFTW Experiment (ELabExperiment)




_A class to hold metadata sufficient to reference an experiment record in an ELabFTW instance._







URI: [microbial_experiment_schema:ELabExperiment](https://w3id.org/usnistgov/microbial-experiment-schema/ELabExperiment)






```mermaid
 classDiagram
    class ELabExperiment
    click ELabExperiment href "../ELabExperiment"
      ELabRecord <|-- ELabExperiment
        click ELabRecord href "../ELabRecord"
      
      ELabExperiment : api_url
        
      ELabExperiment : category_title
        
      ELabExperiment : elabid
        
      ELabExperiment : id
        
      ELabExperiment : status_title
        
      ELabExperiment : title
        
      ELabExperiment : type
        
          
    
    
    ELabExperiment --> "1" ELabExperimentType : type
    click ELabExperimentType href "../ELabExperimentType"

        
      ELabExperiment : url
        
      
```





## Inheritance
* [ELabRecord](ELabRecord.md)
    * **ELabExperiment**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1 <br/> [ELabExperimentType](ELabExperimentType.md) | Whether this item is a resource (database item) or an experiment | direct |
| [status_title](status_title.md) | 1 <br/> [String](String.md) | The status title of an ELabFTW resource | [ELabRecord](ELabRecord.md) |
| [id](id.md) | 1 <br/> [Integer](Integer.md) | The integer identifier for this item used by this eLabFTW instance | [ELabRecord](ELabRecord.md) |
| [elabid](elabid.md) | 1 <br/> [String](String.md) | The unique "eLabID" for this item | [ELabRecord](ELabRecord.md) |
| [url](url.md) | 1 <br/> [Uri](Uri.md) | A (resolvable) URL for accessing this item via a web browser | [ELabRecord](ELabRecord.md) |
| [api_url](api_url.md) | 1 <br/> [Uri](Uri.md) | A URL for accessing this item via the eLabFTW API | [ELabRecord](ELabRecord.md) |
| [title](title.md) | 1 <br/> [String](String.md) | A short description of this item | [ELabRecord](ELabRecord.md) |
| [category_title](category_title.md) | 1 <br/> [String](String.md) | The name of the category for this item (called an "item type") in eLabFTW | [ELabRecord](ELabRecord.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Experiment](Experiment.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [ExperimentWithData](ExperimentWithData.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [ExperimentWithInstrument](ExperimentWithInstrument.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [ExperimentWithInstrumentNoData](ExperimentWithInstrumentNoData.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [CytoFLEXAcquisition](CytoFLEXAcquisition.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [NucleicAcidExtraction](NucleicAcidExtraction.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [CellCultureInBroth](CellCultureInBroth.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [GenericTemplateDeprecated](GenericTemplateDeprecated.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [FormaldehydeFixation](FormaldehydeFixation.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [MicroscopyAcquisition](MicroscopyAcquisition.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [GenericTemplate](GenericTemplate.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [CoulterAcquisition](CoulterAcquisition.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [BactoBoxAcquisition](BactoBoxAcquisition.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [LogCOMETSamplePrep](LogCOMETSamplePrep.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [CFU](CFU.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [DifcoAmendedSporulationAgarProtocol](DifcoAmendedSporulationAgarProtocol.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |
| [SlideCleaning](SlideCleaning.md) | [elab_experiment](elab_experiment.md) | range | [ELabExperiment](ELabExperiment.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:ELabExperiment |
| native | microbial_experiment_schema:ELabExperiment |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ELabExperiment
description: A class to hold metadata sufficient to reference an experiment record
  in an ELabFTW instance.
title: ELabFTW Experiment
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ELabRecord
attributes:
  type:
    name: type
    description: Whether this item is a resource (database item) or an experiment
    title: Type
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    domain_of:
    - ELabItem
    - ELabExperiment
    range: ELabExperimentType
    required: true

```
</details>

### Induced

<details>
```yaml
name: ELabExperiment
description: A class to hold metadata sufficient to reference an experiment record
  in an ELabFTW instance.
title: ELabFTW Experiment
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ELabRecord
attributes:
  type:
    name: type
    description: Whether this item is a resource (database item) or an experiment
    title: Type
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    alias: type
    owner: ELabExperiment
    domain_of:
    - ELabItem
    - ELabExperiment
    range: ELabExperimentType
    required: true
  status_title:
    name: status_title
    description: The status title of an ELabFTW resource
    title: StatusTitle
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: status_title
    owner: ELabExperiment
    domain_of:
    - ELabRecord
    range: string
    required: true
  id:
    name: id
    description: The integer identifier for this item used by this eLabFTW instance
    title: id
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    identifier: true
    alias: id
    owner: ELabExperiment
    domain_of:
    - ELabRecord
    range: integer
    required: true
  elabid:
    name: elabid
    description: The unique "eLabID" for this item
    title: eLabID
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: elabid
    owner: ELabExperiment
    domain_of:
    - ELabRecord
    range: string
    required: true
  url:
    name: url
    description: A (resolvable) URL for accessing this item via a web browser
    title: url
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: url
    owner: ELabExperiment
    domain_of:
    - ELabRecord
    range: uri
    required: true
  api_url:
    name: api_url
    description: A URL for accessing this item via the eLabFTW API
    title: API url
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: api_url
    owner: ELabExperiment
    domain_of:
    - ELabRecord
    range: uri
    required: true
  title:
    name: title
    description: A short description of this item
    title: Title
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: title
    owner: ELabExperiment
    domain_of:
    - ELabRecord
    range: string
    required: true
  category_title:
    name: category_title
    description: The name of the category for this item (called an "item type") in
      eLabFTW
    title: Category Title
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: category_title
    owner: ELabExperiment
    domain_of:
    - ELabRecord
    range: string
    required: true

```
</details>


# Class: Experiment (Experiment) <span style="color: pink;"><strong><small> (Abstract) </small></strong></span> 




_Holds information about a specific type of Microbial Strain experiment. The specific metadata for each type of experiment is controlled by "template data classes"_




* __NOTE__: this is an abstract class and should not be instantiated directly




URI: [microbial_experiment_schema:Experiment](https://w3id.org/usnistgov/microbial-experiment-schema/Experiment)






```mermaid
 classDiagram
    class Experiment
    click Experiment href "../Experiment"
      Experiment <|-- ExperimentWithData
        click ExperimentWithData href "../ExperimentWithData"
      Experiment <|-- ExperimentWithInstrumentNoData
        click ExperimentWithInstrumentNoData href "../ExperimentWithInstrumentNoData"
      Experiment <|-- CellCultureInBroth
        click CellCultureInBroth href "../CellCultureInBroth"
      Experiment <|-- FormaldehydeFixation
        click FormaldehydeFixation href "../FormaldehydeFixation"
      Experiment <|-- LogCOMETSamplePrep
        click LogCOMETSamplePrep href "../LogCOMETSamplePrep"
      Experiment <|-- DifcoAmendedSporulationAgarProtocol
        click DifcoAmendedSporulationAgarProtocol href "../DifcoAmendedSporulationAgarProtocol"
      Experiment <|-- InitiateGrowthOfBSpizizenii
        click InitiateGrowthOfBSpizizenii href "../InitiateGrowthOfBSpizizenii"
      Experiment <|-- SlideCleaning
        click SlideCleaning href "../SlideCleaning"
      
      Experiment : data_acquisition_date
        
          
    
    
    Experiment --> "1" DateValue : data_acquisition_date
    click DateValue href "../DateValue"

        
      Experiment : elab_experiment
        
          
    
    
    Experiment --> "1" ELabExperiment : elab_experiment
    click ELabExperiment href "../ELabExperiment"

        
      Experiment : operator_id
        
          
    
    
    Experiment --> "1" OperatorIDValue : operator_id
    click OperatorIDValue href "../OperatorIDValue"

        
      Experiment : project_id
        
          
    
    
    Experiment --> "1" ELabItemValue : project_id
    click ELabItemValue href "../ELabItemValue"

        
      Experiment : template_name
        
          
    
    
    Experiment --> "1" StringValue : template_name
    click StringValue href "../StringValue"

        
      
```





## Inheritance
* **Experiment**
    * [ExperimentWithData](ExperimentWithData.md)
    * [ExperimentWithInstrumentNoData](ExperimentWithInstrumentNoData.md)
    * [CellCultureInBroth](CellCultureInBroth.md)
    * [FormaldehydeFixation](FormaldehydeFixation.md)
    * [LogCOMETSamplePrep](LogCOMETSamplePrep.md)
    * [DifcoAmendedSporulationAgarProtocol](DifcoAmendedSporulationAgarProtocol.md)
    * [InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md)
    * [SlideCleaning](SlideCleaning.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [data_acquisition_date](data_acquisition_date.md) | 1 <br/> [DateValue](DateValue.md) | Date on which data were acquired according to eLabFTW record | direct |
| [elab_experiment](elab_experiment.md) | 1 <br/> [ELabExperiment](ELabExperiment.md) | A self-reference to this experiment record | direct |
| [operator_id](operator_id.md) | 1 <br/> [OperatorIDValue](OperatorIDValue.md) | Instrument operator during an experiment (a linked item from ELabFTW) | direct |
| [project_id](project_id.md) | 1 <br/> [ELabItemValue](ELabItemValue.md) | The project that an experiment supports (link to an ELabFTW item) | direct |
| [template_name](template_name.md) | 1 <br/> [StringValue](StringValue.md) | The name of the template used to collect metadata for an experiment in ELabFT... | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:Experiment |
| native | microbial_experiment_schema:Experiment |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Experiment
description: Holds information about a specific type of Microbial Strain experiment.
  The specific metadata for each type of experiment is controlled by "template data
  classes"
title: Experiment
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
abstract: true
slots:
- data_acquisition_date
- elab_experiment
- operator_id
- project_id
- template_name
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Experiment
description: Holds information about a specific type of Microbial Strain experiment.
  The specific metadata for each type of experiment is controlled by "template data
  classes"
title: Experiment
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
abstract: true
attributes:
  data_acquisition_date:
    name: data_acquisition_date
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: LabCAS
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: Date on which data were acquired according to eLabFTW record
    title: DataAcquisitionDate
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: data_acquisition_date
    owner: Experiment
    domain_of:
    - Experiment
    range: DateValue
    required: true
  elab_experiment:
    name: elab_experiment
    annotations:
      elabftw_user_input:
        tag: elabftw_user_input
        value: false
    description: A self-reference to this experiment record
    title: ELabFTW Experiment
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: elab_experiment
    owner: Experiment
    domain_of:
    - Experiment
    range: ELabExperiment
    required: true
    inlined_as_list: true
  operator_id:
    name: operator_id
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: LabCAS
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: Instrument operator during an experiment (a linked item from ELabFTW)
    title: OperatorID
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: operator_id
    owner: Experiment
    domain_of:
    - Experiment
    range: OperatorIDValue
    required: true
  project_id:
    name: project_id
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: LabCAS
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: The project that an experiment supports (link to an ELabFTW item)
    title: ProjectID
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: project_id
    owner: Experiment
    domain_of:
    - Experiment
    range: ELabItemValue
    required: true
  template_name:
    name: template_name
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: LabCAS
      read_only:
        tag: read_only
        value: true
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: The name of the template used to collect metadata for an experiment
      in ELabFTW. This value controls what specific metadata fields are allowed.
    title: TemplateName
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: template_name
    owner: Experiment
    domain_of:
    - Experiment
    range: StringValue
    required: true
tree_root: true

```
</details>
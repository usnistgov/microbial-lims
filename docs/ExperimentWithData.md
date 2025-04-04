

# Class: Experiment with Data (ExperimentWithData) <span style="color: pink;"><strong><small> (Abstract) </small></strong></span> 




_Holds information about a specific type of Microbial Strain experiment that results in the collection of data. The specific metadata for each type of experiment is controlled by "template data classes"_




* __NOTE__: this is an abstract class and should not be instantiated directly




URI: [microbial_experiment_schema:ExperimentWithData](https://w3id.org/usnistgov/microbial-experiment-schema/ExperimentWithData)






```mermaid
 classDiagram
    class ExperimentWithData
    click ExperimentWithData href "../ExperimentWithData"
      Experiment <|-- ExperimentWithData
        click Experiment href "../Experiment"
      

      ExperimentWithData <|-- ExperimentWithInstrument
        click ExperimentWithInstrument href "../ExperimentWithInstrument"
      ExperimentWithData <|-- CFU
        click CFU href "../CFU"
      
      
      ExperimentWithData : core_data_path
        
          
    
    
    ExperimentWithData --> "1" StringValue : core_data_path
    click StringValue href "../StringValue"

        
      ExperimentWithData : data_acquisition_date
        
          
    
    
    ExperimentWithData --> "1" DateValue : data_acquisition_date
    click DateValue href "../DateValue"

        
      ExperimentWithData : elab_experiment
        
          
    
    
    ExperimentWithData --> "1" ELabExperiment : elab_experiment
    click ELabExperiment href "../ELabExperiment"

        
      ExperimentWithData : operator_id
        
          
    
    
    ExperimentWithData --> "1" OperatorIDValue : operator_id
    click OperatorIDValue href "../OperatorIDValue"

        
      ExperimentWithData : project_id
        
          
    
    
    ExperimentWithData --> "1" ELabItemValue : project_id
    click ELabItemValue href "../ELabItemValue"

        
      ExperimentWithData : specific_data_path
        
          
    
    
    ExperimentWithData --> "1" StringValue : specific_data_path
    click StringValue href "../StringValue"

        
      ExperimentWithData : template_name
        
          
    
    
    ExperimentWithData --> "1" StringValue : template_name
    click StringValue href "../StringValue"

        
      
```





## Inheritance
* [Experiment](Experiment.md)
    * **ExperimentWithData**
        * [ExperimentWithInstrument](ExperimentWithInstrument.md)
        * [CFU](CFU.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [core_data_path](core_data_path.md) | 1 <br/> [StringValue](StringValue.md) | Portion of the data pathway that will not change as the template is used to g... | direct |
| [specific_data_path](specific_data_path.md) | 1 <br/> [StringValue](StringValue.md) | Portion of the data pathway specific to data from a given experimental record... | direct |
| [data_acquisition_date](data_acquisition_date.md) | 1 <br/> [DateValue](DateValue.md) | Date on which data were acquired according to eLabFTW record | [Experiment](Experiment.md) |
| [elab_experiment](elab_experiment.md) | 1 <br/> [ELabExperiment](ELabExperiment.md) | A self-reference to this experiment record | [Experiment](Experiment.md) |
| [operator_id](operator_id.md) | 1 <br/> [OperatorIDValue](OperatorIDValue.md) | Instrument operator during an experiment (a linked item from ELabFTW) | [Experiment](Experiment.md) |
| [project_id](project_id.md) | 1 <br/> [ELabItemValue](ELabItemValue.md) | The project that an experiment supports (link to an ELabFTW item) | [Experiment](Experiment.md) |
| [template_name](template_name.md) | 1 <br/> [StringValue](StringValue.md) | The name of the template used to collect metadata for an experiment in ELabFT... | [Experiment](Experiment.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:ExperimentWithData |
| native | microbial_experiment_schema:ExperimentWithData |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExperimentWithData
description: Holds information about a specific type of Microbial Strain experiment
  that results in the collection of data. The specific metadata for each type of experiment
  is controlled by "template data classes"
title: Experiment with Data
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: Experiment
abstract: true
slots:
- core_data_path
- specific_data_path

```
</details>

### Induced

<details>
```yaml
name: ExperimentWithData
description: Holds information about a specific type of Microbial Strain experiment
  that results in the collection of data. The specific metadata for each type of experiment
  is controlled by "template data classes"
title: Experiment with Data
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: Experiment
abstract: true
attributes:
  core_data_path:
    name: core_data_path
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: LabCAS
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
      read_only:
        tag: read_only
        value: true
    description: Portion of the data pathway that will not change as the template
      is used to generate experimental records (should be network-resolvable)
    title: CoreDataPath
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: core_data_path
    owner: ExperimentWithData
    domain_of:
    - ExperimentWithData
    range: StringValue
    required: true
  specific_data_path:
    name: specific_data_path
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: LabCAS
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: Portion of the data pathway specific to data from a given experimental
      record  (should be a sub-path of the location specified by `CoreDataPath`)
    title: SpecificDataPath
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: specific_data_path
    owner: ExperimentWithData
    domain_of:
    - ExperimentWithData
    range: StringValue
    required: true
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
    owner: ExperimentWithData
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
    owner: ExperimentWithData
    domain_of:
    - Experiment
    range: ELabExperiment
    required: true
    inlined: true
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
    owner: ExperimentWithData
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
    owner: ExperimentWithData
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
    owner: ExperimentWithData
    domain_of:
    - Experiment
    range: StringValue
    required: true

```
</details>
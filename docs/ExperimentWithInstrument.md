

# Class: Experiment with Instrument (ExperimentWithInstrument) <span style="color: pink;"><strong><small> (Abstract) </small></strong></span> 




_Holds information about a specific type of Microbial Strain experiment that uses an instrument. The specific metadata for each type of experiment is controlled by "template data classes"_




* __NOTE__: this is an abstract class and should not be instantiated directly




URI: [microbial_experiment_schema:ExperimentWithInstrument](https://w3id.org/usnistgov/microbial-experiment-schema/ExperimentWithInstrument)






```mermaid
 classDiagram
    class ExperimentWithInstrument
    click ExperimentWithInstrument href "../ExperimentWithInstrument"
      ExperimentWithData <|-- ExperimentWithInstrument
        click ExperimentWithData href "../ExperimentWithData"
      

      ExperimentWithInstrument <|-- CytoFLEXAcquisition
        click CytoFLEXAcquisition href "../CytoFLEXAcquisition"
      ExperimentWithInstrument <|-- NucleicAcidExtraction
        click NucleicAcidExtraction href "../NucleicAcidExtraction"
      ExperimentWithInstrument <|-- GenericTemplateDeprecated
        click GenericTemplateDeprecated href "../GenericTemplateDeprecated"
      ExperimentWithInstrument <|-- MicroscopyAcquisition
        click MicroscopyAcquisition href "../MicroscopyAcquisition"
      ExperimentWithInstrument <|-- GenericTemplate
        click GenericTemplate href "../GenericTemplate"
      ExperimentWithInstrument <|-- CoulterAcquisition
        click CoulterAcquisition href "../CoulterAcquisition"
      ExperimentWithInstrument <|-- BactoBoxAcquisition
        click BactoBoxAcquisition href "../BactoBoxAcquisition"
      
      
      ExperimentWithInstrument : core_data_path
        
          
    
    
    ExperimentWithInstrument --> "1" StringValue : core_data_path
    click StringValue href "../StringValue"

        
      ExperimentWithInstrument : data_acquisition_date
        
          
    
    
    ExperimentWithInstrument --> "1" DateValue : data_acquisition_date
    click DateValue href "../DateValue"

        
      ExperimentWithInstrument : elab_experiment
        
          
    
    
    ExperimentWithInstrument --> "1" ELabExperiment : elab_experiment
    click ELabExperiment href "../ELabExperiment"

        
      ExperimentWithInstrument : instrument_id
        
          
    
    
    ExperimentWithInstrument --> "1" ELabItemValue : instrument_id
    click ELabItemValue href "../ELabItemValue"

        
      ExperimentWithInstrument : operator_id
        
          
    
    
    ExperimentWithInstrument --> "1" OperatorIDValue : operator_id
    click OperatorIDValue href "../OperatorIDValue"

        
      ExperimentWithInstrument : project_id
        
          
    
    
    ExperimentWithInstrument --> "1" ELabItemValue : project_id
    click ELabItemValue href "../ELabItemValue"

        
      ExperimentWithInstrument : specific_data_path
        
          
    
    
    ExperimentWithInstrument --> "1" StringValue : specific_data_path
    click StringValue href "../StringValue"

        
      ExperimentWithInstrument : template_name
        
          
    
    
    ExperimentWithInstrument --> "1" StringValue : template_name
    click StringValue href "../StringValue"

        
      
```





## Inheritance
* [Experiment](Experiment.md)
    * [ExperimentWithData](ExperimentWithData.md)
        * **ExperimentWithInstrument**
            * [CytoFLEXAcquisition](CytoFLEXAcquisition.md)
            * [NucleicAcidExtraction](NucleicAcidExtraction.md)
            * [GenericTemplateDeprecated](GenericTemplateDeprecated.md)
            * [MicroscopyAcquisition](MicroscopyAcquisition.md)
            * [GenericTemplate](GenericTemplate.md)
            * [CoulterAcquisition](CoulterAcquisition.md)
            * [BactoBoxAcquisition](BactoBoxAcquisition.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [instrument_id](instrument_id.md) | 1 <br/> [ELabItemValue](ELabItemValue.md) | The instrument used to acquire the data in an experiment (linked item from EL... | direct |
| [core_data_path](core_data_path.md) | 1 <br/> [StringValue](StringValue.md) | Portion of the data pathway that will not change as the template is used to g... | [ExperimentWithData](ExperimentWithData.md) |
| [specific_data_path](specific_data_path.md) | 1 <br/> [StringValue](StringValue.md) | Portion of the data pathway specific to data from a given experimental record... | [ExperimentWithData](ExperimentWithData.md) |
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
| self | microbial_experiment_schema:ExperimentWithInstrument |
| native | microbial_experiment_schema:ExperimentWithInstrument |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExperimentWithInstrument
description: Holds information about a specific type of Microbial Strain experiment
  that uses an instrument. The specific metadata for each type of experiment is controlled
  by "template data classes"
title: Experiment with Instrument
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ExperimentWithData
abstract: true
slots:
- instrument_id

```
</details>

### Induced

<details>
```yaml
name: ExperimentWithInstrument
description: Holds information about a specific type of Microbial Strain experiment
  that uses an instrument. The specific metadata for each type of experiment is controlled
  by "template data classes"
title: Experiment with Instrument
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ExperimentWithData
abstract: true
attributes:
  instrument_id:
    name: instrument_id
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: LabCAS
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: The instrument used to acquire the data in an experiment (linked
      item from ELabFTW)
    title: InstrumentID
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: instrument_id
    owner: ExperimentWithInstrument
    domain_of:
    - ExperimentWithInstrument
    - ExperimentWithInstrumentNoData
    range: ELabItemValue
    required: true
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
    owner: ExperimentWithInstrument
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
    owner: ExperimentWithInstrument
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
    owner: ExperimentWithInstrument
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
    owner: ExperimentWithInstrument
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
    owner: ExperimentWithInstrument
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
    owner: ExperimentWithInstrument
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
    owner: ExperimentWithInstrument
    domain_of:
    - Experiment
    range: StringValue
    required: true

```
</details>
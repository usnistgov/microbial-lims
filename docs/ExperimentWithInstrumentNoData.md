

# Class: Experiment with Instrument and No Data (ExperimentWithInstrumentNoData) <span style="color: pink;"><strong><small> (Abstract) </small></strong></span> 




_Holds information about a specific type of Microbial Strain experiment that uses an instrument but does not collect data. The specific metadata for each type of experiment is controlled by "template data classes"_




* __NOTE__: this is an abstract class and should not be instantiated directly




URI: [microbial_experiment_schema:ExperimentWithInstrumentNoData](https://w3id.org/usnistgov/microbial-experiment-schema/ExperimentWithInstrumentNoData)






```mermaid
 classDiagram
    class ExperimentWithInstrumentNoData
    click ExperimentWithInstrumentNoData href "../ExperimentWithInstrumentNoData"
      Experiment <|-- ExperimentWithInstrumentNoData
        click Experiment href "../Experiment"
      

      ExperimentWithInstrumentNoData <|-- CytoFLEXVolumeCalibration
        click CytoFLEXVolumeCalibration href "../CytoFLEXVolumeCalibration"
      
      
      ExperimentWithInstrumentNoData : data_acquisition_date
        
          
    
    
    ExperimentWithInstrumentNoData --> "1" DateValue : data_acquisition_date
    click DateValue href "../DateValue"

        
      ExperimentWithInstrumentNoData : elab_experiment
        
          
    
    
    ExperimentWithInstrumentNoData --> "1" ELabExperiment : elab_experiment
    click ELabExperiment href "../ELabExperiment"

        
      ExperimentWithInstrumentNoData : instrument_id
        
          
    
    
    ExperimentWithInstrumentNoData --> "1" ELabItemValue : instrument_id
    click ELabItemValue href "../ELabItemValue"

        
      ExperimentWithInstrumentNoData : operator_id
        
          
    
    
    ExperimentWithInstrumentNoData --> "1" OperatorIDValue : operator_id
    click OperatorIDValue href "../OperatorIDValue"

        
      ExperimentWithInstrumentNoData : project_id
        
          
    
    
    ExperimentWithInstrumentNoData --> "1" ELabItemValue : project_id
    click ELabItemValue href "../ELabItemValue"

        
      ExperimentWithInstrumentNoData : template_name
        
          
    
    
    ExperimentWithInstrumentNoData --> "1" StringValue : template_name
    click StringValue href "../StringValue"

        
      
```





## Inheritance
* [Experiment](Experiment.md)
    * **ExperimentWithInstrumentNoData**
        * [CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [instrument_id](instrument_id.md) | 1 <br/> [ELabItemValue](ELabItemValue.md) | The instrument used to acquire the data in an experiment (linked item from EL... | direct |
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
| self | microbial_experiment_schema:ExperimentWithInstrumentNoData |
| native | microbial_experiment_schema:ExperimentWithInstrumentNoData |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExperimentWithInstrumentNoData
description: Holds information about a specific type of Microbial Strain experiment
  that uses an instrument but does not collect data. The specific metadata for each
  type of experiment is controlled by "template data classes"
title: Experiment with Instrument and No Data
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: Experiment
abstract: true
slots:
- instrument_id

```
</details>

### Induced

<details>
```yaml
name: ExperimentWithInstrumentNoData
description: Holds information about a specific type of Microbial Strain experiment
  that uses an instrument but does not collect data. The specific metadata for each
  type of experiment is controlled by "template data classes"
title: Experiment with Instrument and No Data
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: Experiment
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
    owner: ExperimentWithInstrumentNoData
    domain_of:
    - ExperimentWithInstrument
    - ExperimentWithInstrumentNoData
    range: ELabItemValue
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
    owner: ExperimentWithInstrumentNoData
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
    owner: ExperimentWithInstrumentNoData
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
    owner: ExperimentWithInstrumentNoData
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
    owner: ExperimentWithInstrumentNoData
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
    owner: ExperimentWithInstrumentNoData
    domain_of:
    - Experiment
    range: StringValue
    required: true

```
</details>
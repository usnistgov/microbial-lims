

# Class: GenericTemplate (GenericTemplate) <span style="color: pink;"><strong><small> (Abstract) </small></strong></span> 




_A generic experiment template used to help create more specific experiment templates. This template should not be used directly._




* __NOTE__: this is an abstract class and should not be instantiated directly




URI: [microbial_experiment_schema:GenericTemplate](https://w3id.org/usnistgov/microbial-experiment-schema/GenericTemplate)






```mermaid
 classDiagram
    class GenericTemplate
    click GenericTemplate href "../GenericTemplate"
      ExperimentWithInstrument <|-- GenericTemplate
        click ExperimentWithInstrument href "../ExperimentWithInstrument"
      
      GenericTemplate : cfu_method
        
          
    
    
    GenericTemplate --> "0..1" CFUMethodValue : cfu_method
    click CFUMethodValue href "../CFUMethodValue"

        
      GenericTemplate : core_data_path
        
          
    
    
    GenericTemplate --> "1" StringValue : core_data_path
    click StringValue href "../StringValue"

        
      GenericTemplate : data_acquisition_date
        
          
    
    
    GenericTemplate --> "1" DateValue : data_acquisition_date
    click DateValue href "../DateValue"

        
      GenericTemplate : elab_experiment
        
          
    
    
    GenericTemplate --> "1" ELabExperiment : elab_experiment
    click ELabExperiment href "../ELabExperiment"

        
      GenericTemplate : fc_acquisition_threshold_channel
        
          
    
    
    GenericTemplate --> "0..1" StringValue : fc_acquisition_threshold_channel
    click StringValue href "../StringValue"

        
      GenericTemplate : fc_acquisition_threshold_value
        
          
    
    
    GenericTemplate --> "0..1" NumberValue : fc_acquisition_threshold_value
    click NumberValue href "../NumberValue"

        
      GenericTemplate : fc_flow_rate_setting
        
          
    
    
    GenericTemplate --> "0..1" FlowRateValue : fc_flow_rate_setting
    click FlowRateValue href "../FlowRateValue"

        
      GenericTemplate : fc_injection_mode
        
          
    
    
    GenericTemplate --> "0..1" FCInjectionModeValue : fc_injection_mode
    click FCInjectionModeValue href "../FCInjectionModeValue"

        
      GenericTemplate : fixation_method
        
          
    
    
    GenericTemplate --> "0..1" FixationMethodValue : fixation_method
    click FixationMethodValue href "../FixationMethodValue"

        
      GenericTemplate : fluorescent_probe
        
          
    
    
    GenericTemplate --> "0..1" FluorescentProbeValue : fluorescent_probe
    click FluorescentProbeValue href "../FluorescentProbeValue"

        
      GenericTemplate : growth_media_name
        
          
    
    
    GenericTemplate --> "0..1" ELabItemValue : growth_media_name
    click ELabItemValue href "../ELabItemValue"

        
      GenericTemplate : incubation_agitation
        
          
    
    
    GenericTemplate --> "0..1" AgitationValue : incubation_agitation
    click AgitationValue href "../AgitationValue"

        
      GenericTemplate : incubation_atmosphere
        
          
    
    
    GenericTemplate --> "0..1" IncubationAtmosphereValue : incubation_atmosphere
    click IncubationAtmosphereValue href "../IncubationAtmosphereValue"

        
      GenericTemplate : incubation_duration
        
          
    
    
    GenericTemplate --> "0..1" DurationValue : incubation_duration
    click DurationValue href "../DurationValue"

        
      GenericTemplate : incubation_temperature
        
          
    
    
    GenericTemplate --> "0..1" TemperatureValue : incubation_temperature
    click TemperatureValue href "../TemperatureValue"

        
      GenericTemplate : instrument_id
        
          
    
    
    GenericTemplate --> "1" ELabItemValue : instrument_id
    click ELabItemValue href "../ELabItemValue"

        
      GenericTemplate : kit_lot_number
        
          
    
    
    GenericTemplate --> "0..1" ELabItemValue : kit_lot_number
    click ELabItemValue href "../ELabItemValue"

        
      GenericTemplate : library_prep
        
          
    
    
    GenericTemplate --> "0..1" StringValue : library_prep
    click StringValue href "../StringValue"

        
      GenericTemplate : microbial_material_id
        
          
    
    
    GenericTemplate --> "0..1" MicrobialMaterialIDValue : microbial_material_id
    click MicrobialMaterialIDValue href "../MicrobialMaterialIDValue"

        
      GenericTemplate : modalities
        
          
    
    
    GenericTemplate --> "0..1" ModalitiesValue : modalities
    click ModalitiesValue href "../ModalitiesValue"

        
      GenericTemplate : nucleic_acid_type
        
          
    
    
    GenericTemplate --> "0..1" NucleicAcidTypeValue : nucleic_acid_type
    click NucleicAcidTypeValue href "../NucleicAcidTypeValue"

        
      GenericTemplate : objective
        
          
    
    
    GenericTemplate --> "0..1" ObjectivesValue : objective
    click ObjectivesValue href "../ObjectivesValue"

        
      GenericTemplate : operator_id
        
          
    
    
    GenericTemplate --> "1" OperatorIDValue : operator_id
    click OperatorIDValue href "../OperatorIDValue"

        
      GenericTemplate : passed_volume_calibration
        
          
    
    
    GenericTemplate --> "0..1" BooleanValue : passed_volume_calibration
    click BooleanValue href "../BooleanValue"

        
      GenericTemplate : percent_volume_deviation
        
          
    
    
    GenericTemplate --> "0..1" UnitlessValue : percent_volume_deviation
    click UnitlessValue href "../UnitlessValue"

        
      GenericTemplate : project_id
        
          
    
    
    GenericTemplate --> "1" ELabItemValue : project_id
    click ELabItemValue href "../ELabItemValue"

        
      GenericTemplate : sample_purpose_codes
        
          
    
    
    GenericTemplate --> "0..1" SamplePurposeCodesValue : sample_purpose_codes
    click SamplePurposeCodesValue href "../SamplePurposeCodesValue"

        
      GenericTemplate : series_image_types
        
          
    
    
    GenericTemplate --> "0..1" SeriesImageTypesValue : series_image_types
    click SeriesImageTypesValue href "../SeriesImageTypesValue"

        
      GenericTemplate : series_images
        
          
    
    
    GenericTemplate --> "0..1" BooleanValue : series_images
    click BooleanValue href "../BooleanValue"

        
      GenericTemplate : single_images
        
          
    
    
    GenericTemplate --> "0..1" BooleanValue : single_images
    click BooleanValue href "../BooleanValue"

        
      GenericTemplate : specific_data_path
        
          
    
    
    GenericTemplate --> "1" StringValue : specific_data_path
    click StringValue href "../StringValue"

        
      GenericTemplate : template_name
        
          
    
    
    GenericTemplate --> "1" StringValue : template_name
    click StringValue href "../StringValue"

        
      
```





## Inheritance
* [Experiment](Experiment.md)
    * [ExperimentWithData](ExperimentWithData.md)
        * [ExperimentWithInstrument](ExperimentWithInstrument.md)
            * **GenericTemplate**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [cfu_method](cfu_method.md) | 0..1 <br/> [CFUMethodValue](CFUMethodValue.md) | Describes deposition format of cells on agar plate | direct |
| [fc_acquisition_threshold_channel](fc_acquisition_threshold_channel.md) | 0..1 <br/> [StringValue](StringValue.md) | Which channel as named by the manufacturer was used to threshold the data acq... | direct |
| [fc_acquisition_threshold_value](fc_acquisition_threshold_value.md) | 0..1 <br/> [NumberValue](NumberValue.md) | Threshold value in arbitrary units that defines the lower limit of data acqui... | direct |
| [fc_flow_rate_setting](fc_flow_rate_setting.md) | 0..1 <br/> [FlowRateValue](FlowRateValue.md) | Set flow rate of data acquisition on flow cytometer | direct |
| [fc_injection_mode](fc_injection_mode.md) | 0..1 <br/> [FCInjectionModeValue](FCInjectionModeValue.md) | Sample acquisition format in flow cytometer | direct |
| [fixation_method](fixation_method.md) | 0..1 <br/> [FixationMethodValue](FixationMethodValue.md) | Specific treatment applied to cells to prevent future changes | direct |
| [fluorescent_probe](fluorescent_probe.md) | 0..1 <br/> [FluorescentProbeValue](FluorescentProbeValue.md) | Fluorescent probe(s) used in the experiment, as linked item(s) from ELabFTW | direct |
| [growth_media_name](growth_media_name.md) | 0..1 <br/> [ELabItemValue](ELabItemValue.md) | Name of media used to culture cells (linked item from ELabFTW) | direct |
| [incubation_agitation](incubation_agitation.md) | 0..1 <br/> [AgitationValue](AgitationValue.md) | Speed of agitation that cells were incubated during an experiment | direct |
| [incubation_atmosphere](incubation_atmosphere.md) | 0..1 <br/> [IncubationAtmosphereValue](IncubationAtmosphereValue.md) | Atmosphere that cells were incubated in to encourage growth | direct |
| [incubation_duration](incubation_duration.md) | 0..1 <br/> [DurationValue](DurationValue.md) | Length of time that cells were incubated during an experiment | direct |
| [incubation_temperature](incubation_temperature.md) | 0..1 <br/> [TemperatureValue](TemperatureValue.md) | Temperature at which cells were incubated during an experiment or culture | direct |
| [kit_lot_number](kit_lot_number.md) | 0..1 <br/> [ELabItemValue](ELabItemValue.md) | The lot number of any relevant kits (linked item from ELabFTW) | direct |
| [library_prep](library_prep.md) | 0..1 <br/> [StringValue](StringValue.md) | The name of a specific kit used for sequencing preparation steps | direct |
| [microbial_material_id](microbial_material_id.md) | 0..1 <br/> [MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) | Cell material(s) used in experiment as named in the eLabFTW database (linked ... | direct |
| [modalities](modalities.md) | 0..1 <br/> [ModalitiesValue](ModalitiesValue.md) | The type (modality) of a microscopy acquisition experiment | direct |
| [nucleic_acid_type](nucleic_acid_type.md) | 0..1 <br/> [NucleicAcidTypeValue](NucleicAcidTypeValue.md) | The type of nucleic acid used in an extraction experiment | direct |
| [objective](objective.md) | 0..1 <br/> [ObjectivesValue](ObjectivesValue.md) | The microscope objectives used in a microscopy acquisition experiment | direct |
| [passed_volume_calibration](passed_volume_calibration.md) | 0..1 <br/> [BooleanValue](BooleanValue.md) | (?) The volume that is passed during a volume calibration | direct |
| [percent_volume_deviation](percent_volume_deviation.md) | 0..1 <br/> [UnitlessValue](UnitlessValue.md) | The volume deviation (measured volume divided by target volume) from a calibr... | direct |
| [sample_purpose_codes](sample_purpose_codes.md) | 0..1 <br/> [SamplePurposeCodesValue](SamplePurposeCodesValue.md) | The types of samples acquired in an experiment (from a controlled list) | direct |
| [series_image_types](series_image_types.md) | 0..1 <br/> [SeriesImageTypesValue](SeriesImageTypesValue.md) | The types of series images acquired in an experiment | direct |
| [series_images](series_images.md) | 0..1 <br/> [BooleanValue](BooleanValue.md) | Whether series images were acquired in an experiment | direct |
| [single_images](single_images.md) | 0..1 <br/> [BooleanValue](BooleanValue.md) | Whether single images were acquired in an experiment | direct |
| [instrument_id](instrument_id.md) | 1 <br/> [ELabItemValue](ELabItemValue.md) | The instrument used to acquire the data in an experiment (linked item from EL... | [ExperimentWithInstrument](ExperimentWithInstrument.md) |
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
| self | microbial_experiment_schema:GenericTemplate |
| native | microbial_experiment_schema:GenericTemplate |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GenericTemplate
description: A generic experiment template used to help create more specific experiment
  templates. This template should not be used directly.
title: GenericTemplate
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ExperimentWithInstrument
abstract: true
slots:
- cfu_method
- fc_acquisition_threshold_channel
- fc_acquisition_threshold_value
- fc_flow_rate_setting
- fc_injection_mode
- fixation_method
- fluorescent_probe
- growth_media_name
- incubation_agitation
- incubation_atmosphere
- incubation_duration
- incubation_temperature
- kit_lot_number
- library_prep
- microbial_material_id
- modalities
- nucleic_acid_type
- objective
- passed_volume_calibration
- percent_volume_deviation
- sample_purpose_codes
- series_image_types
- series_images
- single_images

```
</details>

### Induced

<details>
```yaml
name: GenericTemplate
description: A generic experiment template used to help create more specific experiment
  templates. This template should not be used directly.
title: GenericTemplate
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
is_a: ExperimentWithInstrument
abstract: true
attributes:
  cfu_method:
    name: cfu_method
    description: Describes deposition format of cells on agar plate
    title: CFUMethod
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: cfu_method
    owner: GenericTemplate
    domain_of:
    - GenericTemplateDeprecated
    - GenericTemplate
    - CFU
    range: CFUMethodValue
    required: false
  fc_acquisition_threshold_channel:
    name: fc_acquisition_threshold_channel
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: Fluorescence FC
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: Which channel as named by the manufacturer was used to threshold
      the data acquisition
    title: FCAcquisitionThresholdChannel
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: fc_acquisition_threshold_channel
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - GenericTemplateDeprecated
    - GenericTemplate
    range: StringValue
    required: false
  fc_acquisition_threshold_value:
    name: fc_acquisition_threshold_value
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: Fluorescence FC
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: Threshold value in arbitrary units that defines the lower limit of
      data acquisition in flow cytometry
    title: FCAcquisitionThresholdValue
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: fc_acquisition_threshold_value
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - GenericTemplateDeprecated
    - GenericTemplate
    range: NumberValue
    required: false
  fc_flow_rate_setting:
    name: fc_flow_rate_setting
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: Fluorescence FC
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
      elabftw_default_unit:
        tag: elabftw_default_unit
        value: µL/min
    description: Set flow rate of data acquisition on flow cytometer
    title: FCFlowRateSetting
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: fc_flow_rate_setting
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - CytoFLEXVolumeCalibration
    - GenericTemplateDeprecated
    - GenericTemplate
    range: FlowRateValue
    required: false
  fc_injection_mode:
    name: fc_injection_mode
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: Fluorescence FC
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: Sample acquisition format in flow cytometer
    title: FCInjectionMode
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    ifabsent: Tube
    alias: fc_injection_mode
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - CytoFLEXVolumeCalibration
    - GenericTemplateDeprecated
    - GenericTemplate
    range: FCInjectionModeValue
    required: false
  fixation_method:
    name: fixation_method
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: Generic Microbial
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: Specific treatment applied to cells to prevent future changes
    title: FixationMethod
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    ifabsent: None
    alias: fixation_method
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - GenericTemplateDeprecated
    - FormaldehydeFixation
    - MicroscopyAcquisition
    - GenericTemplate
    - CoulterAcquisition
    - BactoBoxAcquisition
    - LogCOMETSamplePrep
    - CFU
    range: FixationMethodValue
    required: false
  fluorescent_probe:
    name: fluorescent_probe
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: Generic Microbial
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: Fluorescent probe(s) used in the experiment, as linked item(s) from
      ELabFTW
    title: FluorescentProbe
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: fluorescent_probe
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - GenericTemplateDeprecated
    - MicroscopyAcquisition
    - GenericTemplate
    range: FluorescentProbeValue
    required: false
  growth_media_name:
    name: growth_media_name
    description: Name of media used to culture cells (linked item from ELabFTW)
    title: GrowthMediaName
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: growth_media_name
    owner: GenericTemplate
    domain_of:
    - CellCultureInBroth
    - GenericTemplateDeprecated
    - GenericTemplate
    - CFU
    - InitiateGrowthOfBSpizizenii
    range: ELabItemValue
    required: false
  incubation_agitation:
    name: incubation_agitation
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: Generic Microbial
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
      elabftw_default_unit:
        tag: elabftw_default_unit
        value: rpm
    description: Speed of agitation that cells were incubated during an experiment
    title: IncubationAgitation
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: incubation_agitation
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - CellCultureInBroth
    - GenericTemplateDeprecated
    - FormaldehydeFixation
    - MicroscopyAcquisition
    - GenericTemplate
    - InitiateGrowthOfBSpizizenii
    range: AgitationValue
    required: false
  incubation_atmosphere:
    name: incubation_atmosphere
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: Generic Microbial
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: Atmosphere that cells were incubated in to encourage growth
    title: IncubationAtmosphere
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: incubation_atmosphere
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - CellCultureInBroth
    - GenericTemplateDeprecated
    - FormaldehydeFixation
    - MicroscopyAcquisition
    - GenericTemplate
    - CFU
    - InitiateGrowthOfBSpizizenii
    range: IncubationAtmosphereValue
    required: false
  incubation_duration:
    name: incubation_duration
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: Generic Microbial
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
      elabftw_default_unit:
        tag: elabftw_default_unit
        value: hr
    description: Length of time that cells were incubated during an experiment
    title: IncubationDuration
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: incubation_duration
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - CellCultureInBroth
    - GenericTemplateDeprecated
    - FormaldehydeFixation
    - MicroscopyAcquisition
    - GenericTemplate
    - CFU
    - InitiateGrowthOfBSpizizenii
    range: DurationValue
    required: false
  incubation_temperature:
    name: incubation_temperature
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: Generic Microbial
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
      elabftw_default_unit:
        tag: elabftw_default_unit
        value: oC
    description: Temperature at which cells were incubated during an experiment or
      culture
    title: IncubationTemperature
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: incubation_temperature
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - CellCultureInBroth
    - GenericTemplateDeprecated
    - FormaldehydeFixation
    - MicroscopyAcquisition
    - GenericTemplate
    - CFU
    - InitiateGrowthOfBSpizizenii
    range: TemperatureValue
    required: false
  kit_lot_number:
    name: kit_lot_number
    description: The lot number of any relevant kits (linked item from ELabFTW)
    title: KitLotNumber
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: kit_lot_number
    owner: GenericTemplate
    domain_of:
    - NucleicAcidExtraction
    - GenericTemplateDeprecated
    - GenericTemplate
    range: ELabItemValue
    required: false
  library_prep:
    name: library_prep
    description: The name of a specific kit used for sequencing preparation steps
    title: LibraryPrep
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: library_prep
    owner: GenericTemplate
    domain_of:
    - GenericTemplateDeprecated
    - GenericTemplate
    range: StringValue
    required: false
  microbial_material_id:
    name: microbial_material_id
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: LabCAS
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: Cell material(s) used in experiment as named in the eLabFTW database
      (linked items)
    title: MicrobialMaterialID
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: microbial_material_id
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - NucleicAcidExtraction
    - CellCultureInBroth
    - GenericTemplateDeprecated
    - FormaldehydeFixation
    - MicroscopyAcquisition
    - GenericTemplate
    - CoulterAcquisition
    - BactoBoxAcquisition
    - LogCOMETSamplePrep
    - CFU
    - InitiateGrowthOfBSpizizenii
    range: MicrobialMaterialIDValue
    required: false
  modalities:
    name: modalities
    description: The type (modality) of a microscopy acquisition experiment
    title: Modalities
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: modalities
    owner: GenericTemplate
    domain_of:
    - MicroscopyAcquisition
    - GenericTemplate
    range: ModalitiesValue
    required: false
  nucleic_acid_type:
    name: nucleic_acid_type
    description: The type of nucleic acid used in an extraction experiment
    title: NucleicAcidType
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: nucleic_acid_type
    owner: GenericTemplate
    domain_of:
    - NucleicAcidExtraction
    - GenericTemplateDeprecated
    - GenericTemplate
    range: NucleicAcidTypeValue
    required: false
  objective:
    name: objective
    description: The microscope objectives used in a microscopy acquisition experiment
    title: Objective
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: objective
    owner: GenericTemplate
    domain_of:
    - GenericTemplateDeprecated
    - MicroscopyAcquisition
    - GenericTemplate
    range: ObjectivesValue
    required: false
  passed_volume_calibration:
    name: passed_volume_calibration
    description: (?) The volume that is passed during a volume calibration
    title: PassedVolumeCalibration
    todos:
    - double check description
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: passed_volume_calibration
    owner: GenericTemplate
    domain_of:
    - CytoFLEXVolumeCalibration
    - GenericTemplate
    range: BooleanValue
    required: false
  percent_volume_deviation:
    name: percent_volume_deviation
    description: The volume deviation (measured volume divided by target volume) from
      a calibration experiment
    title: PercentVolumeDeviation
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: percent_volume_deviation
    owner: GenericTemplate
    domain_of:
    - CytoFLEXVolumeCalibration
    - GenericTemplate
    range: UnitlessValue
    required: false
  sample_purpose_codes:
    name: sample_purpose_codes
    annotations:
      elabftw_group:
        tag: elabftw_group
        value: Generic Microbial
      elabftw_user_input:
        tag: elabftw_user_input
        value: true
    description: The types of samples acquired in an experiment (from a controlled
      list)
    title: SamplePurposeCodes
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    ifabsent: Positive control
    alias: sample_purpose_codes
    owner: GenericTemplate
    domain_of:
    - CytoFLEXAcquisition
    - NucleicAcidExtraction
    - CellCultureInBroth
    - GenericTemplateDeprecated
    - FormaldehydeFixation
    - MicroscopyAcquisition
    - GenericTemplate
    - CoulterAcquisition
    - BactoBoxAcquisition
    - LogCOMETSamplePrep
    - CFU
    - InitiateGrowthOfBSpizizenii
    range: SamplePurposeCodesValue
    required: false
  series_image_types:
    name: series_image_types
    description: The types of series images acquired in an experiment
    title: SeriesImageTypes
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: series_image_types
    owner: GenericTemplate
    domain_of:
    - MicroscopyAcquisition
    - GenericTemplate
    range: SeriesImageTypesValue
    required: false
  series_images:
    name: series_images
    description: Whether series images were acquired in an experiment
    title: SeriesImages
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: series_images
    owner: GenericTemplate
    domain_of:
    - MicroscopyAcquisition
    - GenericTemplate
    range: BooleanValue
    required: false
  single_images:
    name: single_images
    description: Whether single images were acquired in an experiment
    title: SingleImages
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: single_images
    owner: GenericTemplate
    domain_of:
    - MicroscopyAcquisition
    - GenericTemplate
    range: BooleanValue
    required: false
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
    owner: GenericTemplate
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
    owner: GenericTemplate
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
    owner: GenericTemplate
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
    owner: GenericTemplate
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
    owner: GenericTemplate
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
    owner: GenericTemplate
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
    owner: GenericTemplate
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
    owner: GenericTemplate
    domain_of:
    - Experiment
    range: StringValue
    required: true

```
</details>
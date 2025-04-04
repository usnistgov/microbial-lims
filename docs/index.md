# **Microbial Experiment Schema** <br>a data model for microbial strain experimental metadata.

The Microbial Experiment Schema is a data model (expressed in
[LinkML](https://linkml.io)) used by microbial strain researchers in the
[Biosystems and Biomaterials Division](https://www.nist.gov/mml/bbd) at NIST.

The top-level representation of an experiment is contained in the abstract
[Experiment](Experiment.md) class. The expected specific metadata
for each type of experiment are contained in sub-classes of 
[Experiment](Experiment.md), which correspond to experimental
templates in the ELabFTW Electronic Lab Notebook software. Researchers enter metadata
using an ELabFTW template, which is validated against this schema to ensure data
integrity.

For a graphical overview of the schema structure, please see the following
[interactive visualization](schema_visualization.md).

## Classes

| Class | Description |
| --- | --- |
| [ArrayValue](ArrayValue.md) | A class to hold an array of values |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CFUMethodValue](CFUMethodValue.md) | An override of ArrayValue allowing only values from the CFUMethodEnum enum |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FixationMethodValue](FixationMethodValue.md) | An override of ArrayValue allowing only values from the FixationMethodEnum enum |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FluorescentProbeValue](FluorescentProbeValue.md) | An override of ArrayValue allowing only ELabItem values |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~[LabCASMicrobialMaterialIDValue](LabCASMicrobialMaterialIDValue.md)~~ | *(Deprecated)* A named sub-class of ArrayValue to hold a list of microbial material links |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MicrobialMaterialIDValue](MicrobialMaterialIDValue.md) | A named sub-class of ArrayValue to hold a list of microbial material links |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ModalitiesValue](ModalitiesValue.md) | A named sub-class of ArrayValue to hold a list of modality types |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ObjectivesValue](ObjectivesValue.md) | An override of ArrayValue allowing only values from the ObjectivesEnum enum |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SamplePurposeCodesValue](SamplePurposeCodesValue.md) | An override of ArrayValue allowing only values from the SamplePurposeCodeEnum enum |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SeriesImageTypesValue](SeriesImageTypesValue.md) | An override of ArrayValue allowing only values from the ImageTypeEnum enum |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~[TransmissionModeValue](TransmissionModeValue.md)~~ | *(Deprecated)* An override of ArrayValue allowing only values from the TransmissionModeEnum enum |
| [BooleanValue](BooleanValue.md) | A class to hold a boolean value |
| [DateValue](DateValue.md) | A class to hold a date value |
| [ELabItemValue](ELabItemValue.md) | A class to hold a reference to an item record in ELabFTW |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InstrumentIDValue](InstrumentIDValue.md) | A named sub-class of ELabItemValue to hold an instrument identifier value |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~[LabCASInstrumentValue](LabCASInstrumentValue.md)~~ | *(Deprecated)* A named sub-class of ELabItemValue to hold the instrument identifier |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~[LabCASOperatorValue](LabCASOperatorValue.md)~~ | *(Deprecated)* A named sub-class of ELabItemValue to hold the operator identifier |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~[LabCASProjectValue](LabCASProjectValue.md)~~ | *(Deprecated)* A named sub-class of ELabItemValue to hold the project identifier |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OperatorIDValue](OperatorIDValue.md) | A named sub-class of ELabItemValue to hold an operator identifier value |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProjectIDValue](ProjectIDValue.md) | A named sub-class of ELabItemValue to hold a project identifier value |
| [ELabRecord](ELabRecord.md) | An abstract data type representing a link to an record (experiment or resource/item) in an eLabFTW instance. Use one of the ELabItem or ELabRecord classes that implement this one rather than using it directly. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ELabExperiment](ELabExperiment.md) | A class to hold metadata sufficient to reference an experiment record in an ELabFTW instance. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ELabItem](ELabItem.md) | A class to hold metadata sufficient to reference a resource (database item) record in an ELabFTW instance. |
| [ELabUser](ELabUser.md) | A data type representing a link to a user in an eLabFTW instance |
| [Experiment](Experiment.md) | Holds information about a specific type of Microbial Strain experiment. The specific metadata for each type of experiment is controlled by "template data classes" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellCultureInBroth](CellCultureInBroth.md) | Metadata describing a cell culture experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DifcoAmendedSporulationAgarProtocol](DifcoAmendedSporulationAgarProtocol.md) | Metadata describing the preparation process for amended sporulation agar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExperimentWithData](ExperimentWithData.md) | Holds information about a specific type of Microbial Strain experiment that results in the collection of data. The specific metadata for each type of experiment is controlled by "template data classes" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CFU](CFU.md) | Metadata describing a colony forming unit counting experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExperimentWithInstrument](ExperimentWithInstrument.md) | Holds information about a specific type of Microbial Strain experiment that uses an instrument. The specific metadata for each type of experiment is controlled by "template data classes" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BactoBoxAcquisition](BactoBoxAcquisition.md) | Metadata describing a data acquisition experiment using the BactoBox |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CoulterAcquisition](CoulterAcquisition.md) | Metadata describing a Coulter counter acquisition experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CytoFLEXAcquisition](CytoFLEXAcquisition.md) | Metadata describing a data acquisition using the CytoFLEX instrument |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenericTemplate](GenericTemplate.md) | A generic experiment template used to help create more specific experiment templates. This template should not be used directly. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~~[GenericTemplateDeprecated](GenericTemplateDeprecated.md)~~ | *(Deprecated)* A retired version of a generic experiment template used to create other templates |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MicroscopyAcquisition](MicroscopyAcquisition.md) | Metadata describing a microscopy acquisition experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NucleicAcidExtraction](NucleicAcidExtraction.md) | Metadata describing a nucleic acid extraction experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExperimentWithInstrumentNoData](ExperimentWithInstrumentNoData.md) | Holds information about a specific type of Microbial Strain experiment that uses an instrument but does not collect data. The specific metadata for each type of experiment is controlled by "template data classes" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CytoFLEXVolumeCalibration](CytoFLEXVolumeCalibration.md) | Metadata describing a volume calibration using the CytoFLEX instrument |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FormaldehydeFixation](FormaldehydeFixation.md) | Metadata describing a formaldehyde fixation experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InitiateGrowthOfBSpizizenii](InitiateGrowthOfBSpizizenii.md) | Metadata describing an initiate growth experiment of B. spizizenii |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LogCOMETSamplePrep](LogCOMETSamplePrep.md) | Metadata describing a sample preparation process for a LOGComet experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SlideCleaning](SlideCleaning.md) | Metadata describing an experiment preparing microscopy slides for microbial work |
| [NumberValue](NumberValue.md) | A class to hold a numerical value with a free-text string as a unit |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AgitationValue](AgitationValue.md) | A class to hold a numerical value representing an agitation speed |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CountValue](CountValue.md) | A class to hold a numerical value representing a counting measurement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DurationValue](DurationValue.md) | A class to hold a numerical value representing a time duration measurement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FlowRateValue](FlowRateValue.md) | A class to hold a numerical value representing a flow rate measurement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LengthValue](LengthValue.md) | A class to hold a numerical value representing a linear measurement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TemperatureValue](TemperatureValue.md) | A class to hold a numerical value representing a temperature measurement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UnitlessValue](UnitlessValue.md) | A class to hold an explicitly unitless numerical value |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VolumeValue](VolumeValue.md) | A class to hold a numerical value representing a volumetric measurement |
| [StringValue](StringValue.md) | A class to hold a string value |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BactoBoxAcquisitionTemplateNameValue](BactoBoxAcquisitionTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a BactoBox_Acquisition experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellCultureInBrothTemplateNameValue](CellCultureInBrothTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a Cell Culture in Broth experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CFUTemplateNameValue](CFUTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a CFU experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CoulterAcquisitionTemplateNameValue](CoulterAcquisitionTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a Coulter_Acquisition experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CytoFLEXAcquisitionTemplateNameValue](CytoFLEXAcquisitionTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a CytoFLEX_Acquisition experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CytoFLEXVolumeCalibrationTemplateNameValue](CytoFLEXVolumeCalibrationTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a CytoFLEX_VolumeCalibration experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DifcoAmendedSporulationAgarProtocolTemplateNameValue](DifcoAmendedSporulationAgarProtocolTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a Difco Amended Sporulation Agar Protocol experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FCInjectionModeValue](FCInjectionModeValue.md) | An override of StringValue allowing only values from the FCInjectionModeEnum enum |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FormaldehydeFixationTemplateNameValue](FormaldehydeFixationTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a FormaldehydeFixation experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IncubationAtmosphereValue](IncubationAtmosphereValue.md) | An override of StringValue allowing only values from the IncubationAtmosphereEnum enum |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InitiateGrowthOfBSpizizeniiTemplateNameValue](InitiateGrowthOfBSpizizeniiTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a Initiate Growth of B spizizenii experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LogCOMETSamplePrepTemplateNameValue](LogCOMETSamplePrepTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a LogCOMET_SamplePrep experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MicroscopyAcquisitionTemplateNameValue](MicroscopyAcquisitionTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a Microscopy_Acquisition experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NucleicAcidExtractionTemplateNameValue](NucleicAcidExtractionTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a Nucleic Acid Extraction experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NucleicAcidTypeValue](NucleicAcidTypeValue.md) | An override of StringValue allowing only a value from the NucleicAcidTypeEnum enum |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SlideCleaningTemplateNameValue](SlideCleaningTemplateNameValue.md) | An override of StringValue specified an allowed value for the template_name for a SlideCleaning experiment |
| [UriValue](UriValue.md) | A class to hold a string value that is a URI |



## Slots

| Slot | Description |
| --- | --- |
| ~~[acquisition_time](acquisition_time.md)~~ | *(Deprecated)* Data acquisition time as set by instrument |
| ~~[acquisition_volume](acquisition_volume.md)~~ | *(Deprecated)* Data acquisition volume as set by instrument |
| [api_url](api_url.md) | A URL for accessing this item via the eLabFTW API |
| [base_url](base_url.md) | The URL of the ELabFTW instance in which the user is registered |
| ~~[bead_lot_number_concentration_qc](bead_lot_number_concentration_qc.md)~~ | *(Deprecated)* Lot number of beads used for quality control of concentration measurements |
| ~~[bead_lot_number_size_qc](bead_lot_number_size_qc.md)~~ | *(Deprecated)* Lot number of beads used for quality control of size measurements |
| [category_title](category_title.md) | The name of the category for this item (called an "item type") in eLabFTW |
| ~~[cell_volume](cell_volume.md)~~ | *(Deprecated)* Volume of cell stock added to acquisition vessel |
| [cfu_method](cfu_method.md) | Describes deposition format of cells on agar plate |
| [core_data_path](core_data_path.md) | Portion of the data pathway that will not change as the template is used to g... |
| ~~[coulter_aperture_size](coulter_aperture_size.md)~~ | *(Deprecated)* Aperture installed on Coulter counter during measurement |
| [data_acquisition_date](data_acquisition_date.md) | Date on which data were acquired according to eLabFTW record |
| ~~[diluent_name](diluent_name.md)~~ | *(Deprecated)* Which diluent was used to suspend cells for acquisition (linked item) |
| ~~[diluent_volume](diluent_volume.md)~~ | *(Deprecated)* Volume of diluent added to acquisition vessel |
| [elab_experiment](elab_experiment.md) | A self-reference to this experiment record |
| [elabid](elabid.md) | The unique "eLabID" for this item |
| [email](email.md) | The user's email address |
| ~~[error_flag](error_flag.md)~~ | *(Deprecated)* Indicates if a known error appears in the dataset |
| ~~[fc_acquisition_count_target](fc_acquisition_count_target.md)~~ | *(Deprecated)* Set number of events to acquire in a particular gate on flow cytometer |
| [fc_acquisition_threshold_channel](fc_acquisition_threshold_channel.md) | Which channel as named by the manufacturer was used to threshold the data acq... |
| [fc_acquisition_threshold_value](fc_acquisition_threshold_value.md) | Threshold value in arbitrary units that defines the lower limit of data acqui... |
| [fc_flow_rate_setting](fc_flow_rate_setting.md) | Set flow rate of data acquisition on flow cytometer |
| ~~[fc_fluorescent_channels](fc_fluorescent_channels.md)~~ | *(Deprecated)* List of fluorescent channels acquired during a flow cytometry experiment as n... |
| [fc_injection_mode](fc_injection_mode.md) | Sample acquisition format in flow cytometer |
| [first_name](first_name.md) | The user's first (given) name |
| [fixation_method](fixation_method.md) | Specific treatment applied to cells to prevent future changes |
| [fluorescent_probe](fluorescent_probe.md) | Fluorescent probe(s) used in the experiment, as linked item(s) from ELabFTW |
| ~~[growth_duration](growth_duration.md)~~ | *(Deprecated)* Time that cells were incubated to encourage growth |
| [growth_media_name](growth_media_name.md) | Name of media used to culture cells (linked item from ELabFTW) |
| [id](id.md) | The integer identifier for this item used by this eLabFTW instance |
| [incubation_agitation](incubation_agitation.md) | Speed of agitation that cells were incubated during an experiment |
| [incubation_atmosphere](incubation_atmosphere.md) | Atmosphere that cells were incubated in to encourage growth |
| [incubation_duration](incubation_duration.md) | Length of time that cells were incubated during an experiment |
| [incubation_temperature](incubation_temperature.md) | Temperature at which cells were incubated during an experiment or culture |
| [instrument_id](instrument_id.md) | The instrument used to acquire the data in an experiment (linked item from EL... |
| [kit_lot_number](kit_lot_number.md) | The lot number of any relevant kits (linked item from ELabFTW) |
| ~~[labcas_data_acquisition_date](labcas_data_acquisition_date.md)~~ | *(Deprecated)* Date on which data were acquired according to eLabFTW record |
| ~~[labcas_instrument](labcas_instrument.md)~~ | *(Deprecated)* Date on which data were acquired according to eLabFTW record |
| ~~[labcas_microbial_material_id](labcas_microbial_material_id.md)~~ | *(Deprecated)* Cell material(s) used in experiment as named in the eLabFTW database (linked ... |
| ~~[labcas_operator](labcas_operator.md)~~ | *(Deprecated)* Instrument operator during an experiment (a linked item from ELabFTW) |
| ~~[labcas_project](labcas_project.md)~~ | *(Deprecated)* The project that an experiment supports (link to an ELabFTW item) |
| [last_name](last_name.md) | The user's last name (surname) |
| [library_prep](library_prep.md) | The name of a specific kit used for sequencing preparation steps |
| [microbial_material_id](microbial_material_id.md) | Cell material(s) used in experiment as named in the eLabFTW database (linked ... |
| [modalities](modalities.md) | The type (modality) of a microscopy acquisition experiment |
| [nucleic_acid_type](nucleic_acid_type.md) | The type of nucleic acid used in an extraction experiment |
| [objective](objective.md) | The microscope objectives used in a microscopy acquisition experiment |
| [operator_id](operator_id.md) | Instrument operator during an experiment (a linked item from ELabFTW) |
| [orcid](orcid.md) | The user's ORCID (if defined) |
| [passed_volume_calibration](passed_volume_calibration.md) | (?) The volume that is passed during a volume calibration |
| [percent_volume_deviation](percent_volume_deviation.md) | The volume deviation (measured volume divided by target volume) from a calibr... |
| [project_id](project_id.md) | The project that an experiment supports (link to an ELabFTW item) |
| ~~[qc_reagent_lot_number](qc_reagent_lot_number.md)~~ | *(Deprecated)* The lot number for a QC reagent (link to an ELabFTW item) |
| [sample_purpose_codes](sample_purpose_codes.md) | The types of samples acquired in an experiment (from a controlled list) |
| [series_image_types](series_image_types.md) | The types of series images acquired in an experiment |
| [series_images](series_images.md) | Whether series images were acquired in an experiment |
| [single_images](single_images.md) | Whether single images were acquired in an experiment |
| [specific_data_path](specific_data_path.md) | Portion of the data pathway specific to data from a given experimental record... |
| [status_title](status_title.md) | The status title of an ELabFTW resource |
| [template_name](template_name.md) | The name of the template used to collect metadata for an experiment in ELabFT... |
| [title](title.md) | A short description of this item |
| ~~[transmission_mode](transmission_mode.md)~~ | *(Deprecated)* The type (modality) of a microscopy acquisition experiment |
| [type](type.md) | Whether this item is a resource (database item) or an experiment |
| [unit](unit.md) | The unit corresponding to a metadata value |
| [url](url.md) | A (resolvable) URL for accessing this item via a web browser |
| [userid](userid.md) | The "local" identifier number for this user in the eLabFTW instance |
| [value](value.md) | The actual metadata value for an attribute |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AgitationEnum](AgitationEnum.md) | Allowed agitation speed unit type values |
| [CFUMethodEnum](CFUMethodEnum.md) | Allowed colony forming unit count method values |
| [CountUnitEnum](CountUnitEnum.md) | Allowed count unit type values |
| [DurationUnitEnum](DurationUnitEnum.md) | Allowed time duration unit type values |
| [ELabExperimentType](ELabExperimentType.md) | Allowed record type value for an ELabFTW experiment |
| [ELabItemType](ELabItemType.md) | Allowed record type value for an ELabFTW item/resource |
| [FCInjectionModeEnum](FCInjectionModeEnum.md) | Allowed flow cytometry injection mode values |
| [FixationMethodEnum](FixationMethodEnum.md) | Allowed fixation method values |
| [FlowRateUnitEnum](FlowRateUnitEnum.md) | Allowed flow rate unit type values |
| [ImageTypeEnum](ImageTypeEnum.md) | Allowed microscopy image type values |
| [IncubationAtmosphereEnum](IncubationAtmosphereEnum.md) | Allowed cell incubation atmosphere values |
| [LengthUnitEnum](LengthUnitEnum.md) | Allowed linear length unit type values |
| [MicroscopyModalitiesEnum](MicroscopyModalitiesEnum.md) | Allowed microscopy modality values |
| [NucleicAcidTypeEnum](NucleicAcidTypeEnum.md) | Allowed nucleic acid type values |
| [ObjectivesEnum](ObjectivesEnum.md) | Allowed microscopy objective values |
| [SamplePurposeCodeEnum](SamplePurposeCodeEnum.md) | Allowed sample purpose code values |
| [TemperatureUnitEnum](TemperatureUnitEnum.md) | Allowed temperature unit type values |
| ~~[TransmissionModeEnum](TransmissionModeEnum.md)~~ | *(Deprecated)* Allowed microscopy transmission mode values |
| [UnitlessEnum](UnitlessEnum.md) | Allowed value for "unitless" numerical values |
| [VolumeUnitEnum](VolumeUnitEnum.md) | Allowed volume unit type values |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |

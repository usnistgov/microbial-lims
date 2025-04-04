

# Class: Uri Value (UriValue)




_A class to hold a string value that is a URI_







URI: [microbial_experiment_schema:UriValue](https://w3id.org/usnistgov/microbial-experiment-schema/UriValue)






```mermaid
 classDiagram
    class UriValue
    click UriValue href "../UriValue"
      UriValue : value
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [Uri](Uri.md) | The actual metadata value for an attribute | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/usnistgov/microbial-experiment-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | microbial_experiment_schema:UriValue |
| native | microbial_experiment_schema:UriValue |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UriValue
description: A class to hold a string value that is a URI
title: Uri Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
slots:
- value
slot_usage:
  value:
    name: value
    range: uri

```
</details>

### Induced

<details>
```yaml
name: UriValue
description: A class to hold a string value that is a URI
title: Uri Value
from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
slot_usage:
  value:
    name: value
    range: uri
attributes:
  value:
    name: value
    description: The actual metadata value for an attribute
    title: value
    from_schema: https://w3id.org/usnistgov/microbial-experiment-schema
    rank: 1000
    alias: value
    owner: UriValue
    domain_of:
    - BooleanValue
    - NumberValue
    - StringValue
    - UriValue
    - DateValue
    - ArrayValue
    - ELabItemValue
    - FCInjectionModeValue
    - IncubationAtmosphereValue
    range: uri
    required: true

```
</details>
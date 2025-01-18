__all__ = ["schema_view"]

from linkml_runtime import SchemaView as _sv
from pathlib import Path as _p

_yaml_path = _p(__file__).resolve().parent / "schema" / "microbial_experiment_schema.yaml"
schema_view = _sv(_yaml_path)

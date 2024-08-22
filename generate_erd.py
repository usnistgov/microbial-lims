# for debugging of ERD/doc generation
from linkml.generators import erdiagramgen, docgen

gen = erdiagramgen.ERDiagramGenerator(
    schema="microbial_experiment.yaml",
)
doc_gen = docgen.DocGenerator(
    schema="microbial_experiment.yaml",
    directory="docs"
)
doc_gen.serialize()
gen.serialize_classes(
    ["CytoFLEXAcquisition"],
    follow_references=False,
    max_hops=None,
    include_upstream=False,
)
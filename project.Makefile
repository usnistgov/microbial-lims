## Add your own custom Makefile targets here
gen-viz-data:
	$(RUN) python src/microbial_experiment_schema/scripts/generate_json.py

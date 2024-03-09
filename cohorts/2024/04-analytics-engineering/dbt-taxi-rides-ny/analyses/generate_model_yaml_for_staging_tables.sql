-- depends_on: {{ ref('stg_green_taxi_trips') }}
-- depends_on: {{ ref('stg_yellow_taxi_trips') }}

{% if execute %}

    {% set models_to_generate = codegen.get_models(directory="staging", prefix="stg_") %}
    {{ codegen.generate_model_yaml(
        model_names = models_to_generate
    ) }}

{% endif %}

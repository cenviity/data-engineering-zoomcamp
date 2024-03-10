-- depends_on: {{ ref('dim_monthly_zone_revenue') }}
-- depends_on: {{ ref('dim_zones') }}
-- depends_on: {{ ref('fact_trips') }}
-- depends_on: {{ ref('fact_fhv_trips') }}

{% if execute %}

    {% set models_to_generate = codegen.get_models(directory="core") %}
    {{ codegen.generate_model_yaml(
        model_names = models_to_generate
    ) }}

{% endif %}

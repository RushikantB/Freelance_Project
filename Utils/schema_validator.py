import json
from jsonschema import validate


def validate_json_schema(response_json, schema_path):
    """
    Validates JSON response with a given schema file.
    """
    with open(schema_path, 'r') as file:
        schema = json.load(file)

    validate(instance=response_json, schema=schema)

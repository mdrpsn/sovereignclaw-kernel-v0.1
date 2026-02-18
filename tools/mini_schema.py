from __future__ import annotations

from typing import Any


class SchemaError(ValueError):
    pass


def _is_type(value: Any, t: str) -> bool:
    if t == "object":
        return isinstance(value, dict)
    if t == "array":
        return isinstance(value, list)
    if t == "string":
        return isinstance(value, str)
    return False


def validate(instance: Any, schema: dict[str, Any], path: str = "$") -> None:
    if "type" in schema:
        if not _is_type(instance, schema["type"]):
            raise SchemaError(f"{path}: expected {schema['type']}")

    required = schema.get("required", [])
    if isinstance(instance, dict):
        for k in required:
            if k not in instance:
                raise SchemaError(f"{path}: missing required field '{k}'")

    props = schema.get("properties", {})
    if isinstance(instance, dict):
        for k, v in instance.items():
            if k in props:
                validate(v, props[k], f"{path}.{k}")

        if schema.get("additionalProperties") is False:
            unknown = [k for k in instance.keys() if k not in props]
            if unknown:
                raise SchemaError(f"{path}: unknown fields {unknown}")

    if isinstance(instance, str):
        min_len = schema.get("minLength")
        if min_len is not None and len(instance) < int(min_len):
            raise SchemaError(f"{path}: string shorter than minLength {min_len}")

        if "enum" in schema and instance not in schema["enum"]:
            raise SchemaError(f"{path}: value '{instance}' not in enum {schema['enum']}")

    if isinstance(instance, list):
        min_items = schema.get("minItems")
        if min_items is not None and len(instance) < int(min_items):
            raise SchemaError(f"{path}: array shorter than minItems {min_items}")

        item_schema = schema.get("items")
        if item_schema is not None:
            for i, item in enumerate(instance):
                validate(item, item_schema, f"{path}[{i}]")

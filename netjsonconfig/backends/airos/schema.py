"""
AirOS specific JSON-Schema definition
"""
from ...schema import schema as default_schema
from ...schema import DEFAULT_FILE_MODE  # noqa - backward compatibility
from ...utils import merge_config

gui_schema = {
        "properties": {
            "gui": {
                "additionalProperties": True,
                "propertyOrder": 1,
                "properties": {
                    "advanced": {
                        "type": "boolean",
                        "propertyOrder": 1,
                    },
                    "language": {
                        "type": "string",
                        "propertyOrder": 2,
                    },
                },
                "required": [
                    "advanced",
                    "language"
                ],
                "title": "Gui",
                "type": "object",
            },
        }
}

schema = merge_config(default_schema, gui_schema)

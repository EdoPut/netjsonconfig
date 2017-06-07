"""
AirOS specific JSON-Schema definition
"""
from ...schema import schema as default_schema
from ...schema import DEFAULT_FILE_MODE  # noqa - backward compatibility
from ...utils import merge_config

"""
This schema defines a new property ``gui`` in netjson
to configure the web interface for airos
"""
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

"""
This defines a new property in the ``Interface``.

The management interface is the one that exposes the
web interface

It can be used on a single interface (ethernet, vlan) or
on a bridge
"""

netconf_schema = {
        "type": "object",
        "addtionalProperties": True,
        "definitions": {
            "base_address": {
                "properties": {
                    "management": {
                        "type": "boolean",
                        "default": False,
                    }
                }
            }
        }
    }


"""
This schema override the possible encryption for AirOS from the default schema
"""
wpasupplicant_schema = {
    "encryption_wireless_property_sta": {
        "properties": {
            "encryption": {
                "type": "object",
                "title": "Encryption",
                "required": "protocol",
                "propertyOrder": 20,
                "oneOf": [
                    {"$ref": "#/definitions/encryption_none"},
                    {"$ref": "#/definitions/encryption_wpa_personal"},
                    {"$ref": "#/definitions/encryption_wpa_enterprise_sta"},
                ],
            },
        },
    },
    "encryption_wireless_property_ap": {
        "properties": {
            "encryption": {
                "type": "object",
                "title": "Encryption",
                "required": "protocol",
                "propertyOrder": 20,
                "oneOf": [
                    {"$ref": "#/definitions/encryption_none"},
                    {"$ref": "#/definitions/encryption_wpa_personal"},
                    {"$ref": "#/definitions/encryption_wpa_enterprise_sta"},
                ],
            },
        },
    },
}


schema = merge_config(default_schema, gui_schema, netconf_schema, wpasupplicant_schema)

=============
AirOS Backend
=============

.. include:: ../_github.rst

The ``AirOs`` backend allows to generate AirOS v8.3 compatible configurations.

Initialization
--------------

.. automethod:: netjsonconfig.AirOs.__init__

Initialization example:

.. code-block:: python

    from netjsonconfig import AirOs

    router = AirOs({
        "general": {
            "hostname": "MasterAntenna"
        }
    })

If you are unsure about the meaning of the initalization parameters,
read about the following basic concepts:

    * :ref:`configuration_dictionary`
    * :ref:`template`
    * :ref:`context`

Render method
-------------

.. automethod:: netjsonconfig.AirOs.render

Generate method
---------------

.. automethod:: netjsonconfig.AirOs.generate


Write method
------------

.. automethod:: netjsonconfig.AirOs.write


JSON method
-----------

.. automethod:: netjsonconfig.AirOs.json


General settings
----------------

From the ``general`` key we can configure the contact and the location for a device using the ``contact`` and ``location`` properties.

The following snippet specify both contact and location:

.. code-block:: json

    {
        "type": "DeviceConfiguration",
        "general": {
            "contact": "user@example.com",
            "location": "Up in the roof"
        }
    }

Network interface
-----------------

From the ``interfaces`` key we can configure the device network interfaces.

AirOS supports the following types of interfaces

* **network interfaces**: may be of type ``ethernet``
* **wirelesss interfaces**: must be of type ``wireless``
* **bridge interfaces**: must be of type ``bridge``

A network interface can be designed to be the management interfaces by setting the ``managed`` key to ``True`` on the address chosen.

As an example here is a snippet that set the vlan ``eth0.2`` to be the management interface on the address ``192.168.1.20``

.. code-block:: json

   {
       "interfaces": [
           {
               "name": "eth0.2",
               "type": "ethernet",
               "addresses": [
                   {
                       "address": "192.168.1.20",
                       "family": "ipv4",
                       "managed": true,
                       "mask": 24,
                       "proto": "static"
                   }
               ]
           }
       ]
   }

DNS servers
-----------


GUI
---

As an extension to `NetJSON <http://netjson.org/rfc.html>` you can use the ``gui`` key to set the language of the interface and show the advanced network configuration option.

The default values for this key are as reported below

.. code-block:: json

    {
        "gui": {
            "language": "en_US",
            "advanced": true
        }
    }

NTP servers
-----------

This is an extension to the `NetJSON` specification.

By setting the key ``ntp_servers`` in your input you can provide a list of ntp servers to use.

.. code-block:: json

    {
        "type": "DeviceConfiguration",
        ...
        "ntp_servers": [
            "0.ubnt.pool.ntp.org"
        ]
    }

WPA2
----

AirOS v8.3 supports both WPA2 personal (PSK+CCMP) and WPA2 enterprise (EAP+CCMP) as an authentication protocol. The only ciphers available is CCMP.

As an antenna only has one wireless network available only the first wireless interface will be used during the generation.

As an example here is a snippet that set the authentication protocol to WPA2 personal

.. code-block:: json

    {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "encryption": {
                    "protocol": "wpa2_personal",
                    "key": "changeme"
                }
            }
        ]
    }

And another that set the authentication protocol to WPA2 enterprise, but this is still not supported by netjsonconfig

.. code-block:: json

    {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "encryption": {
                    "protocol": "wpa2_enterprise",
                    "key": "changeme"
                }
            }
        ]
    }

Leaving the `NetJSON Encryption object <http://netjson.org/rfc.html#rfc.section.5.4.2.1>` empty defaults to no encryption at all

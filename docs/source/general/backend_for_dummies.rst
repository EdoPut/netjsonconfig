===================
Backend for dummies
===================

.. raw:: html

    <p>
        <iframe src="https://nodeshot.org/github-btn.html?user=openwisp&amp;repo=netjsonconfig&amp;type=watch&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="120" height="33"></iframe>
        <iframe src="https://nodeshot.org/github-btn.html?user=openwisp&amp;repo=netjsonconfig&amp;type=fork&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="120" height="33"></iframe>
    </p>

This guide will help you get started creating a custom backend for netjsonconfig

A backend is a Python class that create a text from a :ref:`configuration_dictionary`

A :ref:`schema` can be specified to validate a :ref:`configuration_dictionary` 
before creation

Creating a backend
------------------

A backend must accept both configuration and :ref:`template` as input. This has been
taken care for you, just inherit from the ``BaseBackend`` object as in this example

.. code:: python

    from netjsonconfig.backends.base import BaseBackend

    class FooBackend(BaseBackend):
        pass

Now your `FooBackend` can be used with a :ref:`configuration_dictionary` as input to produce a configuration.


.. code-block:: python

   >>> foo = FooBackend({
   ...    "general": {
   ...        "hostname": "FooRouter"
   ...     }
   ...})
   >>> print(foo.render())

   >>>

but as it does not define how to render something the output of `foo.render` is empty.

Adding a renderer
-----------------

.. code:: python

    # netjsonconfig/backends/foo/foo.py

    from ..base import BaseBackend
    from .schema import schema

    class FooBackend(BaseBackend):

        schema = schema

.. code:: python

    # netjsonconfig/backends/foo/schema.py

    # there is predefined schema to use if you
    # are not sure what to do
    from ..schema import schema as default_schema
    from ..schema import DEFAULT_FILE_MODE

    # but if you nedd to add some restrictions
    # you can use merge_config to overwrite
    # the default one
    from ..utils import merge_config

    # here we define the schema for the foo backend
    schema = merge_config(default_schema)

Now we are going to add a renderer to our backend

.. code:: python

    # netjsonconfig/backends/foo/foo.py

    from ..base import BaseBackend, BaseRenderer

    class FooRenderer(BaseRender):
       pass

    class FooBackend(BaseBackend):

        renderers = [
            FooRenderer,
        ]

        schema = schema

And this renderer have to build a `context` to be used inside a Jinja template

.. code:: python

    class FooRenderer(BaseRenderer):
        def __get_foo(self):
            # this will return the value of the
            # key `foo` from the configuration
            # dictionary or default to 'baz'
            return self.config.get('foo', 'baz')

Unfortunately we still have something to do, define a template

Create the directory `netjsonconfig/backends/foo/templates` and add this line to `FooBackend` so that it will search there for templates.

.. code:: python

   class FooBackend(BaseBackend):

       # Jinja2 will append `.templates` to this
       # and use the resulting directory as the source
       # for templates
       env_path = 'netjsonconfig.backends.foo'

       renderers = [
           FooRenderer,
       ]

       schema = schema

Every renderer will search for a file that matches it's name in the template directory, e.g `FooBackend` will search for `netjsonconfig/backends/foo/templates/foo.jinja2` and `BarRenderer` will search for `netjsonconfig/backends/foo/templates/bar.jinja2`.

Creating a template
-------------------

Create the file `netjsonconfig/backends/foo/templates/foo.jinja2` with this content


.. code:: python

    {% if not is_empty %}
    This is the configuration file
    
    The value of foo is: {{ foo }}
    {% endif %}

If we run the previous example we get a different result

.. code:: python

   >>> foo = FooBackend({
   ...    "general": {
   ...        "hostname": "FooRouter"
   ...     }
   ...})
   >>> print(foo.render())
   This is the configuration file
   
   The value of foo is: baz
   >>> foo = FooBackend({
   ...    "general": {
   ...        "hostname": "FooRouter"
   ...     }
   ...     "foo": "bar"
   ...})
   >>> print(foo.render())
   This is the configuration file
   
   The value of foo is: bar
   >>>


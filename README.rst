|PyPI version| |Build Status|

conf
====

A *very* simple and *lightweight* configuration loader and parser for Python.

Supports:

-  yaml files (``*.yml``, ``*.yaml``)
-  ini files (``*.ini``)
-  json files (``*.json``)

Installation
''''''''''''

::

    pip install conf

Usage
'''''

Starting your app
"""""""""""""""""

Start your app with your configuration file:

::

    python your_app.py --config your_config.yml

The ``--config`` argument can be a relative path or an absolute path to a file. You are allowed to provide multiple configuration files (separated by a single space), in which case any setting of a former configuration file can be overwritten by a setting of a later configuration file, if the name of that setting is identical.

Fetching your setting (option 1)
""""""""""""""""""""""""""""""""

Simply get your setting from the ``conf`` module:

.. code:: python

    import conf
    your_setting = conf.your_setting

Fetching your setting (option 2)
""""""""""""""""""""""""""""""""
Import your setting directly:

.. code:: python

    from conf import your_setting

Fetching your setting (option 3)
""""""""""""""""""""""""""""""""
You can provide a default value if you are not sure the setting will be present:

.. code:: python

    import conf
    your_setting = conf.get('your_setting', 'your default value')

Note: If you use an ArgumentParser in your own application for other purposes, you must use the ``parse_known_args()`` method of the parser.

Meta
''''
This lib was designed and written in 2018 by `finetuned89 <https://github.com/finetuned89>`_ and `ramonhagenaars <https://github.com/ramonhagenaars>`_.

.. |PyPI version| image:: https://badge.fury.io/py/conf.svg
   :target: https://badge.fury.io/py/conf

.. |Build Status| image:: https://api.travis-ci.org/ramonhagenaars/conf.svg?branch=master
   :target: https://travis-ci.org/ramonhagenaars/conf

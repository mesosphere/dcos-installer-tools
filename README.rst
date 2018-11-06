|Build Status|

|codecov|

DC/OS Installer Tools
=====================

A DC/OS installer provides the following interface:

.. code:: console

   $ bash dcos_generate_config.sh --version
   Extracting image from this script and loading into docker daemon, this step can take a few minutes
   x dcos-genconf.75af9b2571de95e074-c74aa914537fa9f81b.tar
   Loaded image: mesosphere/dcos-genconf:75af9b2571de95e074-c74aa914537fa9f81b
   {
     "variant": "",
     "version": "1.12.0-rc3"
   }
   $ bash dcos_generate_config.sh --version
   {
     "variant": "",
     "version": "1.12.0-rc3"
   }

For DC/OS Enterprise installers, the ``"variant"`` key is set to ``"ee"``.

This is a Python library for collecting the outputted information from the installer.

Installation
------------

.. code:: console

   pip install git+https://github.com/adamtheturtle/dcos-installer-tools.git

Usage
-----

.. code:: python

   from pathlib import Path

   from dcos_installer_tools import DCOSVariant, get_dcos_installer_details

   installer = Path('/Users/Eleanor/Documents/dcos_generate_config.sh')
   details = get_dcos_installer_details(installer=installer)
   assert details.version == '1.12'
   assert details.variant == DCOSVariant.OSS
   assert details.variant != DCOSVariant.ENTERPRISE

Determining details about the artifact requires extracting the artifact.
Extracting the artifact requires over a gigabyte of space in a workspace directory.
By default, this directory is the result of ``tempfile.gettempdir()``.
It is possible to use the ``workspace_dir`` parameter of ``get_dcos_installer_details`` to set a workspace directory ``pathlib.Path``.

By default, the extracted artifact is removed.
Set the ``keep_extracted`` parameter to of ``get_dcos_installer_details`` to ``True`` to keep the extracted artifact.
This will be in the same directory as the given ``installer``.

Exceptions which may be raised include:

* ``CalledProcessError``: An error was encountered when extracting the given artifact.

.. |Build Status| image:: https://travis-ci.com/adamtheturtle/dcos-installer-tools.svg?branch=master
   :target: https://travis-ci.com/adamtheturtle/dcos-installer-tools
.. |codecov| image:: https://codecov.io/gh/adamtheturtle/dcos-installer-tools/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/adamtheturtle/dcos-installer-tools

DC/OS Artifact Tools
====================

Tools for getting information from DC/OS installer artifacts.

Installation
------------

.. code:: console

   pip install git+https://github.com/adamtheturtle/dcos-installer-tools.git

.. code:: python

   from pathlib import Path

   from dcos_artifact_tools import DCOSVariant, get_dcos_installer_details

   installer = Path('/Users/Eleanor/Documents/dcos_generate_config.sh')
   details = get_dcos_installer_details(installer=installer)
   assert details.version == '1.12'
   assert details.variant == DCOSVariant.OSS

Determining details about the artifact requires extracting the artifact.
Extracting the artifact requires over a gigabyte of space in a workspace directory.
By default, this directory is the result of ``tempfile.gettempdir()``.
It is possible to use the ``workspace_dir`` parameter of ``get_dcos_installer_details`` to set a workspace directory ``pathlib.Path``.

By default, the extracted artifact is removed.
Set the ``keep_extracted`` parameter to of ``get_dcos_installer_details`` to ``True`` to keep the extracted artifact.
This will be in the same directory as the given ``installer``.

Exceptions which may be raised include:

* ``ValueError``: A space was in the path to the artifact.
* ``CalledProcessError``: An error was encountered when extracting the given artifact.

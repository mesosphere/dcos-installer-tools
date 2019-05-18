"""
Tests for ``get_dcos_installer_details``.
"""

import shutil
from pathlib import Path
from tempfile import gettempdir

import pytest
# See https://github.com/PyCQA/pylint/issues/1536 for details on why the errors
# are disabled.
from py.path import local  # pylint: disable=no-name-in-module, import-error

from dcos_installer_tools import DCOSVariant, get_dcos_installer_details


class TestOSS:
    """
    Tests for giving OSS artifacts to ``get_dcos_installer_details``.

    We could use pytest parameterization to consolidate these tests, but then
    we would have to store all artifacts and Travis builders run out of space.
    """

    def test_master(
        self,
        oss_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS OSS master artifact.
        """
        details = get_dcos_installer_details(
            installer=oss_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.OSS
        assert details.version.startswith('1.14')

    def test_1_13(
        self,
        oss_1_13_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS OSS 1.13 artifact.
        """
        details = get_dcos_installer_details(
            installer=oss_1_13_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.OSS
        assert details.version.startswith('1.13')

    def test_1_12(
        self,
        oss_1_12_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS OSS 1.12 artifact.
        """
        details = get_dcos_installer_details(
            installer=oss_1_12_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.OSS
        assert details.version.startswith('1.12')

    def test_1_11(
        self,
        oss_1_11_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS OSS 1.11 artifact.
        """
        details = get_dcos_installer_details(
            installer=oss_1_11_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.OSS
        assert details.version.startswith('1.11')

    def test_1_10(
        self,
        oss_1_10_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS OSS 1.10 artifact.
        """
        details = get_dcos_installer_details(
            installer=oss_1_10_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.OSS
        assert details.version.startswith('1.10')

    def test_1_9(
        self,
        oss_1_9_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS OSS 1.9 artifact.
        """
        details = get_dcos_installer_details(
            installer=oss_1_9_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.OSS
        assert details.version.startswith('1.9')


class TestEnterprise:
    """
    Tests for giving Enterprise artifacts to ``get_dcos_installer_details``.

    We could use pytest parameterization to consolidate these tests, but then
    we would have to store all artifacts and Travis builders run out of space.
    """

    def test_master(
        self,
        enterprise_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS Enterprise master artifact.
        """
        details = get_dcos_installer_details(
            installer=enterprise_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.ENTERPRISE
        assert details.version.startswith('1.14')

    def test_1_13(
        self,
        enterprise_1_13_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS Enterprise 1.13 artifact.
        """
        details = get_dcos_installer_details(
            installer=enterprise_1_13_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.ENTERPRISE
        assert details.version.startswith('1.13')

    def test_1_12(
        self,
        enterprise_1_12_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS Enterprise 1.12 artifact.
        """
        details = get_dcos_installer_details(
            installer=enterprise_1_12_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.ENTERPRISE
        assert details.version.startswith('1.12')

    def test_1_11(
        self,
        enterprise_1_11_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS Enterprise 1.11 artifact.
        """
        details = get_dcos_installer_details(
            installer=enterprise_1_11_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.ENTERPRISE
        assert details.version.startswith('1.11')

    def test_1_10(
        self,
        enterprise_1_10_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS Enterprise 1.10 artifact.
        """
        details = get_dcos_installer_details(
            installer=enterprise_1_10_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.ENTERPRISE
        assert details.version.startswith('1.10')

    def test_1_9(
        self,
        enterprise_1_9_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Details are returned when given a DC/OS Enterprise 1.9 artifact.
        """
        details = get_dcos_installer_details(
            installer=enterprise_1_9_artifact,
            workspace_dir=Path(str(tmpdir)),
        )

        assert details.variant == DCOSVariant.ENTERPRISE
        assert details.version.startswith('1.9')


class TestParameters:
    """
    Tests for the parameters to ``get_dcos_installer_details``.
    """

    def test_default_keep_extracted(
        self,
        oss_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        By default, the extracted artifact is removed.
        """
        workspace_dir = Path(str(tmpdir))
        get_dcos_installer_details(
            installer=oss_artifact,
            workspace_dir=workspace_dir,
        )

        assert not list(workspace_dir.iterdir())

    def test_keep_extracted_true(
        self,
        oss_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        If ``keep_extracted`` is set to ``True``, the extracted artifact is not
        removed.
        """
        workspace_dir = Path(str(tmpdir))
        get_dcos_installer_details(
            installer=oss_artifact,
            workspace_dir=workspace_dir,
            keep_extracted=True,
        )

        genconf_dir = workspace_dir / 'genconf'
        assert genconf_dir.exists()
        (_, ) = workspace_dir.glob('dcos-genconf.*.tar')

    def test_default_workspace_dir(self, oss_artifact: Path) -> None:
        """
        By default, the workspace directory is set to the value of
        ``gettempdir()``.
        """
        # We check that the filesystem is in an appropriate state to run the
        # test.
        workspace_dir = Path(gettempdir())
        genconf_dir = workspace_dir / 'genconf'
        assert not genconf_dir.exists()
        assert not list(workspace_dir.glob('dcos-genconf.*.tar'))

        get_dcos_installer_details(
            installer=oss_artifact,
            keep_extracted=True,
        )
        assert genconf_dir.exists()
        shutil.rmtree(path=str(genconf_dir))

        (tarfile, ) = workspace_dir.glob('dcos-genconf.*.tar')
        tarfile.unlink()

    def test_space_installer_path(
        self,
        oss_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        Spaces are not allowed in the installer path.
        """
        tmpdir_path = Path(str(tmpdir))
        target_dir = tmpdir_path / 'example space'
        target_dir.mkdir()
        new_artifact = target_dir / oss_artifact.name
        shutil.copyfile(src=str(oss_artifact), dst=str(new_artifact))

        with pytest.raises(ValueError) as exc:
            get_dcos_installer_details(installer=new_artifact)

        expected_message = (
            'No spaces allowed in path to the installer. '
            'See https://jira.mesosphere.com/browse/DCOS_OSS-4429.'
        )
        assert str(exc.value) == expected_message

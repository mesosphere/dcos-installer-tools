"""
Tests for ``get_dcos_installer_details``.
"""

from pathlib import Path

# See https://github.com/PyCQA/pylint/issues/1536 for details on why the errors
# are disabled.
from py.path import local  # pylint: disable=no-name-in-module, import-error

from artifact_utils import DCOSVariant, get_dcos_installer_details


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


class TestKeepExtracted:
    """
    Tests for the ``keep_extracted`` parameter to
    ``get_dcos_installer_details``.
    """

    def test_default(
        self,
        oss_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        By default, the extracted artifact is removed.
        """
        workspace_dir = Path(str(tmpdir))
        details = get_dcos_installer_details(
            installer=oss_artifact,
            workspace_dir=workspace_dir,
        )

        assert not list(workspace_dir.iterdir())

    def test_true(
        self,
        oss_artifact: Path,
        tmpdir: local,
    ) -> None:
        """
        If ``keep_extracted`` is set to ``True``, the extracted artifact is not
        removed.
        """
        workspace_dir = Path(str(tmpdir))
        details = get_dcos_installer_details(
            installer=oss_artifact,
            workspace_dir=workspace_dir,
            keep_extracted=True,
        )

        filenames = {item.name for item in workspace_dir.iterdir()}
        filenames.remove('genconf')
        (tarfile, ) = filenames
        assert tarfile.startswith('dcos-genconf')
        assert tarfile.endswith('.tar')

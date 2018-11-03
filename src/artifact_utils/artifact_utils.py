"""
Tools for getting details from DC/OS installer artifacts.
"""

class DCOSVariant(Enum):
    """
    Variants of DC/OS.
    """

    OSS = 1
    ENTERPRISE = 2


class DCOSInstallerUti:
    """
    Details of a DC/OS Artifact.
    """

    def __init__(
        self,
        installer: Path,
        workspace_dir: Path,
        keep_extracted: bool = False,
    ):
        """
        Get details from a DC/OS artifact.

        Args:
            installer: The path to a DC/OS installer. This cannot include a
                space.
            workspace_dir: The directory in which large temporary files will be
                created.
                This is equivalent to `dir` in :py:func:`tempfile.mkstemp`.
            keep_extracted: Whether to keep the extracted artifact.

        Attributes:
            variant: The DC/OS variant which can be installed using the given
            installer.

        Raises:
            ValueError: A space is in the build artifact path.
            CalledProcessError: XXX
        """
        if ' ' in str(installer):
            message = 'No spaces allowed in path to the build artifact.'
            raise ValueError(message)

        result = subprocess.check_output(
            args=['bash', str(installer), '--version'],
            cwd=str(workspace_dir),
            stderr=subprocess.PIPE,
        )

        result = result.decode()
        result = ' '.join(
            [
                line for line in result.splitlines()
                if not line.startswith('Extracting image')
                and not line.startswith('Loaded image') and '.tar' not in line
            ],
        )

        version_info = json.loads(result)
        variant = version_info['variant']

        self.version = version_info['version']
        self.variant = {
            'ee': DCOSVariant.ENTERPRISE,
            '': DCOSVariant.OSS,
        }[variant]

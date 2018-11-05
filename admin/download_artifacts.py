"""
Download artifacts.
"""

import os
from pathlib import Path
from typing import Dict  # noqa: F401
from typing import Tuple  # noqa: F401

import click
import requests

OSS_PATTERN = (
    'https://downloads.dcos.io/dcos/testing/{version}/dcos_generate_config.sh'
)
OSS_MASTER_ARTIFACT_URL = OSS_PATTERN.format(version='master')
OSS_1_9_ARTIFACT_URL = OSS_PATTERN.format(version='1.9')
OSS_1_10_ARTIFACT_URL = OSS_PATTERN.format(version='1.10')
OSS_1_11_ARTIFACT_URL = OSS_PATTERN.format(version='1.11')
OSS_1_12_ARTIFACT_URL = OSS_PATTERN.format(version='1.12')

EE_MASTER_ARTIFACT_URL = os.environ.get('EE_MASTER_ARTIFACT_URL')
EE_1_9_ARTIFACT_URL = os.environ.get('EE_1_9_ARTIFACT_URL')
EE_1_10_ARTIFACT_URL = os.environ.get('EE_1_10_ARTIFACT_URL')
EE_1_11_ARTIFACT_URL = os.environ.get('EE_1_11_ARTIFACT_URL')
EE_1_12_ARTIFACT_URL = os.environ.get('EE_1_12_ARTIFACT_URL')

OSS_MASTER_ARTIFACT_PATH = Path('/tmp/dcos_generate_config.sh')
OSS_1_9_ARTIFACT_PATH = Path('/tmp/dcos_generate_config_1_9.sh')
OSS_1_10_ARTIFACT_PATH = Path('/tmp/dcos_generate_config_1_10.sh')
OSS_1_11_ARTIFACT_PATH = Path('/tmp/dcos_generate_config_1_11.sh')
OSS_1_12_ARTIFACT_PATH = Path('/tmp/dcos_generate_config_1_12.sh')

EE_MASTER_ARTIFACT_PATH = Path('/tmp/dcos_generate_config.ee.sh')
EE_1_9_ARTIFACT_PATH = Path('/tmp/dcos_generate_config_1_9.ee.sh')
EE_1_10_ARTIFACT_PATH = Path('/tmp/dcos_generate_config_1_10.ee.sh')
EE_1_11_ARTIFACT_PATH = Path('/tmp/dcos_generate_config_1_11.ee.sh')
EE_1_12_ARTIFACT_PATH = Path('/tmp/dcos_generate_config_1_12.ee.sh')

OSS_MASTER = (OSS_MASTER_ARTIFACT_URL, OSS_MASTER_ARTIFACT_PATH)
OSS_1_9 = (OSS_1_9_ARTIFACT_URL, OSS_1_9_ARTIFACT_PATH)
OSS_1_10 = (OSS_1_10_ARTIFACT_URL, OSS_1_10_ARTIFACT_PATH)
OSS_1_11 = (OSS_1_11_ARTIFACT_URL, OSS_1_11_ARTIFACT_PATH)
OSS_1_12 = (OSS_1_12_ARTIFACT_URL, OSS_1_12_ARTIFACT_PATH)
EE_MASTER = (EE_MASTER_ARTIFACT_URL, EE_MASTER_ARTIFACT_PATH)
EE_1_9 = (EE_1_9_ARTIFACT_URL, EE_1_9_ARTIFACT_PATH)
EE_1_10 = (EE_1_10_ARTIFACT_URL, EE_1_10_ARTIFACT_PATH)
EE_1_11 = (EE_1_11_ARTIFACT_URL, EE_1_11_ARTIFACT_PATH)
EE_1_12 = (EE_1_12_ARTIFACT_URL, EE_1_12_ARTIFACT_PATH)

PATTERNS = {
    'tests/test_dcos_artifact_info.py::TestOSS::test_master': (OSS_MASTER, ),
    'tests/test_dcos_artifact_info.py::TestOSS::test_1_11': (OSS_1_11, ),
    'tests/test_dcos_artifact_info.py::TestOSS::test_1_12': (OSS_1_12, ),
    'tests/test_dcos_artifact_info.py::TestOSS::test_1_10': (OSS_1_10, ),
    'tests/test_dcos_artifact_info.py::TestOSS::test_1_9': (OSS_1_9, ),
    'tests/test_dcos_artifact_info.py::TestEnterprise::test_master':
    (EE_MASTER, ),
    'tests/test_dcos_artifact_info.py::TestEnterprise::test_1_11': (EE_1_11, ),
    'tests/test_dcos_artifact_info.py::TestEnterprise::test_1_12': (EE_1_12, ),
    'tests/test_dcos_artifact_info.py::TestEnterprise::test_1_10': (EE_1_10, ),
    'tests/test_dcos_artifact_info.py::TestEnterprise::test_1_9': (EE_1_9, ),
    'tests/test_dcos_artifact_info.py::TestParameters': (OSS_MASTER, ),
}  # type: Dict[str, Tuple]


def _download_file(url: str, path: Path) -> None:
    """
    Download a file to a given path.
    """
    label = 'Downloading to ' + str(path)
    stream = requests.get(url, stream=True)
    assert stream.ok
    content_length = int(stream.headers['Content-Length'])
    total_written = 0
    chunk_size = 1024
    # See http://click.pocoo.org/6/arguments/#file-args for parameter
    # information
    with click.open_file(
        filename=str(path),
        mode='wb',
        atomic=True,
        lazy=True,
    ) as file_descriptor:
        content_iter = stream.iter_content(chunk_size=chunk_size)
        with click.progressbar(  # type: ignore
                content_iter,
                length=content_length / chunk_size,
                label=label,
        ) as progress_bar:
            for chunk in progress_bar:
                # Filter out keep-alive new chunks.
                if chunk:
                    total_written += len(chunk)
                    file_descriptor.write(chunk)  # type: ignore

    message = (
        'Downloaded {total_written} bytes. '
        'Expected {content_length} bytes.'
    ).format(
        total_written=total_written,
        content_length=content_length,
    )

    assert total_written == content_length, message


def download_artifacts(test_pattern: str) -> None:
    """
    Download artifacts.
    """
    downloads = PATTERNS[test_pattern]
    for url, path in downloads:
        _download_file(url=url, path=path)


if __name__ == '__main__':
    CI_PATTERN = os.environ.get('CI_PATTERN')
    if CI_PATTERN:
        download_artifacts(test_pattern=CI_PATTERN)

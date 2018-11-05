"""
Fixtures for tests.
"""

from pathlib import Path

import pytest


@pytest.fixture()
def oss_artifact() -> Path:
    """
    Return the path to a build artifact for DC/OS OSS master.
    """
    return Path('/tmp/dcos_generate_config.sh')


@pytest.fixture()
def enterprise_artifact() -> Path:
    """
    Return the path to a build artifact for DC/OS Enterprise master.
    """
    return Path('/tmp/dcos_generate_config.ee.sh')


@pytest.fixture()
def oss_1_9_artifact() -> Path:
    """
    Return the path to a build artifact for DC/OS OSS 1.9.
    """
    return Path('/tmp/dcos_generate_config_1_9.sh')


@pytest.fixture()
def enterprise_1_9_artifact() -> Path:
    """
    Return the path to a build artifact for DC/OS Enterprise 1.9.
    """
    return Path('/tmp/dcos_generate_config_1_9.ee.sh')


@pytest.fixture()
def oss_1_10_artifact() -> Path:
    """
    Return the path to a build artifact for DC/OS OSS 1.10.
    """
    return Path('/tmp/dcos_generate_config_1_10.sh')


@pytest.fixture()
def enterprise_1_10_artifact() -> Path:
    """
    Return the path to a build artifact for DC/OS Enterprise 1.10.
    """
    return Path('/tmp/dcos_generate_config_1_10.ee.sh')


@pytest.fixture()
def oss_1_11_artifact() -> Path:
    """
    Return the path to a build artifact for DC/OS OSS 1.11.
    """
    return Path('/tmp/dcos_generate_config_1_11.sh')


@pytest.fixture()
def enterprise_1_11_artifact() -> Path:
    """
    Return the path to a build artifact for DC/OS Enterprise 1.11.
    """
    return Path('/tmp/dcos_generate_config_1_11.ee.sh')


@pytest.fixture()
def oss_1_12_artifact() -> Path:
    """
    Return the path to a build artifact for DC/OS OSS 1.12.
    """
    return Path('/tmp/dcos_generate_config_1_12.sh')


@pytest.fixture()
def enterprise_1_12_artifact() -> Path:
    """
    Return the path to a build artifact for DC/OS Enterprise 1.12.
    """
    return Path('/tmp/dcos_generate_config_1_12.ee.sh')

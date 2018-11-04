SHELL := /bin/bash -euxo pipefail

include lint.mk


.PHONY: lint
# We do not currently run pydocstyle as we have to ignore vendored items.
lint: \
    check-manifest \
    custom-linters \
    doc8 \
    flake8 \
    isort \
    linkcheck \
    mypy \
    pip-extra-reqs \
    pip-missing-reqs \
    pylint \
    pyroma \
    shellcheck \
    spelling \
    vulture \
    yapf

# Fix some linting errors.
.PHONY: fix-lint
fix-lint: autoflake fix-yapf
	isort --recursive --apply

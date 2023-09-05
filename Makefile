SHELL := /bin/bash

.PHONY: lint
## Run linting
lint:
	pre-commit run --all-files

.PHONY: test
## Run tests
test:
	pytest magic/tests

.PHONY: install_libmagic
## Install libmagic
install_libmagic:
	# Debian https://packages.ubuntu.com/libmagic-dev
	# Mac https://formulae.brew.sh/formula/libmagic
	# Windows https://github.com/julian-r/file-windows
	( ( ( brew install libmagic || ( apt-get update && apt-get install -y libmagic-dev ) ) || apk add --update libmagic ) || yum install file-libs ) || python -c 'import platform, zipfile, urllib.request; assert platform.system() == "Windows"; machine = "x64" if platform.machine() == "AMD64" else "x86"; zipfile.ZipFile(urllib.request.urlopen(f"https://github.com/julian-r/file-windows/releases/download/v5.44/file_5.44-build104-vs2022-{machine}.zip")).extractall("magic")'
		find / -name *magic*

.PHONY: install
## Install for development
install:
	pip install -v .[test]
	pre-commit install || true  # not installed on older python versions

.DEFAULT_GOAL := help
.PHONY: help
## Print Makefile documentation
help:
	@perl -0 -nle 'printf("\033[36m  %-15s\033[0m %s\n", "$$2", "$$1") while m/^##\s*([^\r\n]+)\n^([\w.-]+):[^=]/gm' $(MAKEFILE_LIST) | sort

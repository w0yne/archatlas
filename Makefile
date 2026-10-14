# One entry point for development and CI.
#   make setup   create .venv, install the package with the dev extra and the site deps
#   make check   run every check CI runs (tests, generators, i18n, lint, pack, site)
# Optional variables:
#   ARCHATLAS_PRIVATE_NAMES_FILE=/path/outside/repo   private-names list for the lint
#   I18N_FLAGS=--release   stale translations become errors (release builds)
#   PACK_OUT=dir           keep the packed skill zip there instead of a temp dir

VENV   ?= .venv
PYTHON ?= $(VENV)/bin/python
SITE_BASE ?= /archatlas/
I18N_FLAGS ?=

.PHONY: setup check test generated i18n lint pack site

setup:
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e '.[dev]'
	npm run site:install

check: test generated i18n lint pack site

test:
	$(PYTHON) -m pytest -q

generated:
	$(PYTHON) tools/check_front_matter.py
	$(PYTHON) tools/build_selection.py --check
	$(PYTHON) tools/build_skill_refs.py --check
	$(PYTHON) tools/build_samples.py --check

i18n:
	$(PYTHON) tools/i18n_check.py $(I18N_FLAGS)

lint:
	$(PYTHON) tools/lint_private.py --strict --history

pack:
ifdef PACK_OUT
	$(PYTHON) tools/pack_skill.py --out "$(PACK_OUT)" --verify
else
	out=$$(mktemp -d) && $(PYTHON) tools/pack_skill.py --out "$$out" --verify; rc=$$?; rm -rf "$$out"; exit $$rc
endif

site:
	npm run check
	SITE_BASE=$(SITE_BASE) npm run build

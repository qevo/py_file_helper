# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS	  =
SPHINXBUILD   = sphinx-build
PAPER		  =
BUILDDIR	  = .
PKGDIR		  = ..
RSTDIR		  = _rst

buildDir = $(realpath $(BUILDDIR))
pkgDir = $(realpath $(PKGDIR))
rstDir = $(realpath $(RSTDIR))


# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4	 = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(buildDir)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(buildDir)
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(buildDir)


html:
	@`cd $(buildDir)`
	@echo "remove docs from git index"
	@git ls-files | xargs -I %s git rm -f --cache %s

	@echo "remove any existing files"
	@rm .buildinfo || true
	@rm *.html || true
	@rm *.inv || true
	@rm *.js || true
	@rm *.rst || true
	@rm -r .doctrees || true
	@rm -r _modules || true
	@rm -r _sources || true
	@rm -r _static || true

	@`cd $(rstDir)`
	@rm *.rst || true
	@echo "copying static pages"
	@find . -depth -name "*.rs_" -exec sh -c 'cp "$$1" "$${1%.rs_}.rst"' _ {} \; || true

	@echo "find python packages and generate API documentation"
	@find $(pkgDir) -depth -name "__init__.py" -exec sh -c 'sphinx-apidoc -f -T -e -o $(rstDir) "$${1%__init__.py}"' _ {} \; || true

	@echo "convert markdown files"
	@pandoc --from=markdown --to=rst --output=$(rstDir)/changelog.rst $(pkgDir)/CHANGELOG.md

	@cp -a $(rstDir)/*.rst $(buildDir)
	@rm $(rstDir)/*.rst || true
	@echo "generate HTML documentation"
	$(SPHINXBUILD) -b html $(buildDir) $(buildDir)

	@echo "remove doctrees"
	@rm -r $(buildDir)/.doctrees || true

	@`cd $(buildDir)`
	@echo "add docs to git index"
	@git add *

	@echo
	@echo "Build finished. The HTML page is in $(buildDir)."
	@echo
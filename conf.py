# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'cdfwriter'
copyright = '2023, Joey Mukherjee'
author = 'Joey Mukherjee'
release = '1.1.0'

# -- Hand-edit for autodoc extension below -----------------------------------
# -- Sphinx documentation says the module or the package must be in one of the directories on sys.path

import os, sys

# sys.path.append(os.path.abspath('../../'))
sys.path.append(os.path.abspath('../../src/cdfwriter/'))

# according to SpacePy.pycdf notes, which cdfwriter uses
os.environ["CDF_LIB"] = "/SDDAS/hapi_src_build/_deps/cdffetch-src/lib"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
              'sphinx.ext.duration',
              'sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.autosummary',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.intersphinx',
              'sphinx_changelog',
             ]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = []


# Napoleon settings
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Changed all of these from default
napoleon_google_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_special_with_doc = False
napoleon_use_ivar = True
napoleon_use_param = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'
html_static_path = ['_static']

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import datetime
import sys

sys.path.insert(0, os.path.abspath("../.."))
from sphinx.builders.html import StandaloneHTMLBuilder


# -- Project information -----------------------------------------------------

project = "TownsNet"
copyright = "2023-{}, IDU".format(datetime.datetime.now().year)
author = "IDU"

# The full version, including alpha/beta/rc tags
release = "0.0.10"
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "autodocsumm",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.graphviz",
    "nbsphinx",
    "nbsphinx_link",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# StandaloneHTMLBuilder.supported_image_types = [
#     'image/svg+xml',
#     'image/gif',
#     'image/png',
#     'image/jpeg'
# ]

html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

# autodoc_inherit_docstrings = False
# napoleon_google_docstring = True
# napoleon_include_init_with_doc = True
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_keyword = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_attr_annotations = False

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "member-order": "bysource",
    "ignore-module-all": True,
    "exclude-members": "model_config, model_fields, model_post_init",
}
autoclass_content = "class"
autodoc_typehints = "signature"
autodoc_typehints_format = "short"
autodoc_mock_imports = ["objgraph", "memory_profiler", "gprof2dot", "snakeviz"]

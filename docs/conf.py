# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

# Agrega la ruta del paquete
sys.path.insert(0, os.path.abspath('../'))  # Ajusta si tu paquete está en otro nivel

html_title = "IndicPy Documentation"
project = 'IndicPy'
copyright = '2025, Data Science for Health Services and Policy Research Group- Aragon Institute of Health Sciences'
author = 'Javier González-Galindo, Francisco Estupiñan-Romero, Santiago Royo-Sierra'
release = 'HTML'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Para soportar docstrings en formato Google/NumPy
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_show_sourcelink = False  # Hide "Show Source"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

html_static_path = ['_static']

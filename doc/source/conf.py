# -*- coding: utf-8 -*-
#
# BOLOS Python Loader documentation build configuration file.

import os
import sys

sys.path.append(os.path.abspath('../../'))

# General Configuration
# =====================

extensions = []

source_suffix = ['.rst']

master_doc = 'index'

project = u'BOLOS Python Loader'
copyright = u'2017, Ledger Team'
author = u'Ledger Team'

version = u'0.1.14'
release = u'0.1.14'

pygments_style = 'sphinx'

# Options for HTML Output
# =======================

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css', # Override wide tables in RTD theme
    ],
}

# sphinxarg
# =========

extensions += ['sphinxarg.ext']

# intersphinx
# ===========

extensions += ['sphinx.ext.intersphinx']

intersphinx_mapping = {
    'ledger': ('https://ledger.readthedocs.io/en/1/', None)
}
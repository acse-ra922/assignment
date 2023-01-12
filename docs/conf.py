import sys
import os

sys.path.insert(0, os.path.abspath(os.sep.join((os.curdir, '..'))))

project = 'Programming Assignment'
author = "Rubab Atwal
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.mathjax']
source_suffix = '.rst'
master_doc = 'src/index'
exclude_patterns = ['_build']
autoclass_content = "both"
html_theme = 'sphinx_rtd_theme'

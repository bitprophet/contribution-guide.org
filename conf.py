from datetime import datetime


extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'contribution-guide.org'
year = datetime.now().year
copyright = u'%d Jeff Forcier' % year

exclude_trees = ['_build']
default_role = 'obj'
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'

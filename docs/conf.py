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
import sys
# sys.path.insert(0, os.path.abspath('.'))


"""""
----------------Dependencies ------------------------
1. The sphinx book theme is a theme that is used for the documentation. It is a theme that is not included in the standard sphinx package and can be found below at  "Options for HTML output"
2. For the embedding of youtube and vimeo videos into the pages we use, they are also marked in the extensions section of this file:  pip install sphinxcontrib-youtube
"""

# -- Project information -----------------------------------------------------

language = "en"

project = 'Radii Documentation'
copyright = '2023, ETH Zürich, Gramazio Kohler Research'
author = 'Gereon Sievi, Corrections by Sarah Schneider'
release = '0.42'

# The full version, including alpha/beta/rc tags


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# pip install sphinxcontrib-youtube

extensions = [
  'sphinxcontrib.youtube',
  'sphinx.ext.githubpages'

    ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

exclude_patterns = ['_build',
'Thumbs.db',
'.DS_Store',
"tutorial/grashopper/documentation_rst/Vorlage.rst",
"conf2.py", "index2.rst", "readme.rst",
"tutorial/Quick_Guide/1_LV_Exploration.rst", "changelog.rst", 
"8_install_server.rst", "5_install_mobile.rst"

]




# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'


# How to use the sphinx book theme
"""
the sphinx_book_theme can be found at https://sphinx-themes.org/sample-sites/sphinx-book-theme/#id2

Quickstart

Install this theme: $ pip install sphinx-book-theme

Set the following in your existing Sphinx documentation’s conf.py file:
html_theme = 'sphinx_book_theme'
"""

#----------------------------
# Theme Options: 

html_last_updated_fmt = '%d.%m.%Y'

html_theme_options =  {
    "logo": {
      "image_light": "_static/logo.png",
      "image_dark": "_static/logo_dark.png",
     },
   "content_footer_items": ["last-updated"],
   "body_max_width": 'none',

   "repository_url": "https://github.com/gramaziokohler/radii_docs/",
    "use_source_button": True,
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_edit_page_button": True,
    "use_issues_button": True,

}





# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_Font']


# Prolog is an index that helps with linking between files https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-rst_prolog
# It works by pasting what is noted under rst_prolog in the beginning of every rst file. this way you can call the shortcuts and can edit them on this central location.
#  the Radii Logo can be called with |xyz| --- did not work so was taken out again. Did not work with relative paths.
# Aliases with spaces are calls with `Operation Menu`_ in the specific pages
rst_prolog = """

.. _RadiiViewer: https://gramaziokohler.github.io/radii_docs/tutorial/Viewer_PC/documentation_rst/0_Viewer.html
.. _RadiiGrasshopper: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/01_Components_Overview.html
.. _Setup: https://gramaziokohler.github.io/radii_docs/tutorial/Setup/install_setup.html
.. _Grasshopper Setup: https://gramaziokohler.github.io/radii_docs/tutorial/Quick_Guide/Setup/3_install_grasshopper.html
.. _PC Viewer Setup: https://gramaziokohler.github.io/radii_docs/tutorial/Quick_Guide/Setup/2_install_PC.html
.. _Oculus Viewer Setup:

.. _RADii.info: https://radii.info/
.. _Radii Rhino7 Grasshopper Win/Mac: https://radii.info/download/plugin/R7/RADii.zip
.. _Radii Rhino8 Grasshopper Win/Mac: https://radii.info/download/plugin/R8/RADii.zip
.. _Radii Capture Win/Mac: https://radii.info/download/plugin/RADiiCapture.zip

.. _Radii Viewer Windows 10+: https://radii.info/download/standard/RADii%20Viewer%20Setup.zip
.. _Radii Viewer macOS X: https://apps.apple.com/app/id1505325031
.. _Radii Viewer VR Oculus: https://radii.info/download/vr/RADii%20Viewer%20Oculus.zip
.. _Radii Viewer VR universal : https://radii.info/download/vr/RADii%20Viewer%20VR.zip

.. _Connect: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/02_connect.html
.. _PublishGeometry: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/03_publish_geometry.html
.. _PublishMaterial: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/04_publish_material.html
.. _Publish View: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/07_publish_View.html
.. _Publish Section: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/05_publish_section.html
.. _Publish Animation: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/09_publish_Animation.html
.. _Publish Control: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/06_publish_control.html
.. _Publish Reference: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/14_publish_reference.html
.. _Publish Parameter: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/15_publish_parameter.html

.. _Save Scenario: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/16_save_scenario.html
.. _Save Content: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/12_SaveContent.html

.. _Subscribe Curve: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/103_SubscribeCurve.html
.. _Subscribe Message: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/104_SubscribeMessages.html
.. _Subscribe Pointcloud: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/105_SubscribePointCloud.html
.. _Subscribe Geometry: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/106_SubscribeGeometry.html
.. _Subscribe Parameter: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/107_SubscribeParameter.html
.. _Subscribe User: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/108_SubscribeUser.html

.. _Tools Pointcloud: https://gramaziokohler.github.io/radii_docs/tutorial/grashopper/documentation_rst/301_Tools_PointCloudResource_subset.html

.. _Radii Viewer: https://gramaziokohler.github.io/radii_docs/tutorial/Viewer_PC/documentation_rst/0_Viewer.html
.. _Connect Menu: https://gramaziokohler.github.io/radii_docs/tutorial/Viewer_PC/documentation_rst/1_Connect.html
.. _Remote Content Menu: https://gramaziokohler.github.io/radii_docs/tutorial/Viewer_PC/documentation_rst/2_Remote_content.html
.. _Users Menu: https://gramaziokohler.github.io/radii_docs/tutorial/Viewer_PC/documentation_rst/4_Users.html
.. _Operation Menu: https://gramaziokohler.github.io/radii_docs/tutorial/Viewer_PC/documentation_rst/6_Operation_menu.html

  

.. _Basics & Exploration tutorial: https://gramaziokohler.github.io/radii_docs/tutorial/Quick_Guide/1_LV_Exploration_short.html
.. _Tutorial Grasshopper Basics:  https://gramaziokohler.github.io/radii_docs/tutorial/Quick_Guide/1_LV_Exploration_Grashopper.html
.. _Tutorial Viewer Basics:  https://gramaziokohler.github.io/radii_docs/tutorial/Quick_Guide/1_LV_Exploration_Grashopper.html
.. _Tutorial Advanced Presentation: https://gramaziokohler.github.io/radii_docs/tutorial/Quick_Guide/3_LV_20Presentation_Storry.html

.. _Github Radii Documentation Issues: https://github.com/gramaziokohler/radii_docs/issues



.. _Introducing Publish Parameter: https://www.youtube.com/watch?v=3u-yBNSTHpU
.. _Voice chat and viewer to viewer control: https://www.youtube.com/watch?v=CCU14B5tqCM





"""
 

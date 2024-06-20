.. Radii_documentation documentation master file, created by
   sphinx-quickstart on Mon Oct  9 18:29:30 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. image:: tutorial/Radii_Icons/Radii_logo.png

**************************
Radii Documentation
**************************

v39.1

Welcome to the Radii documentation.

.. 
   Table of content:
   1. Home Page with general information
   2. Radii Viewer - Detailed description of all parts & options 
   3. Radii Grasshopper - Detailed description of all parts & options
   4. Guides - Installations and Guides for different use cases

`RADii <https://RADii.info/>`_ is a cloud platform where you can publish (upload) 3D Models to share, explore and collaborate. 

RADii consists of two parts, a plugin for the CAD software Rhino Grasshopper to publish (upload) 3D Models and programs called Viewers that run on a range of devices ( PC/Mac, VR Headsets or mobile devices) to receive and explore the models.


Rhino, Grasshopper and Viewer
________________________________

.. image:: /tutorial/Quick_Guide/1_LV_Explo_Images/Rhino_GH_Viewer.png



Example Project
_____________________ 

..
   .. image:: tutorial/Viewer_PC/images/01_Start_image.png
      :alt: The empty Radii viewer after starting

.. image:: tutorial/Viewer_PC/images/231218_cadeim_kytami_Photo_1_WM.jpg
   :alt: Autumn semester 2023, project by Cadei  Matteo & Tami  Kyan  

Immersive Design Studio at Gramazio Kohler Research, ETH Zürich, Autumn semester 2023 student project by Matteo Cadei & Kyan Tami  




How RADii works
___________________


.. image:: tutorial/Radii_diagramms/Daten_Diagramme_v2/svg/Radii_funktionality_simple_crop.svg

**How it works simplified:** A CAD software (Rhino Grasshopper) is connected to a cloud through a plugin. 3D Models are live uploaded to the cloud (Unity) and then distributes them to the RADii viewers.
The RADii Viewers are a program that can be run on PC/Mac, iPhone and VR Headsets. Viewers are connected through the cloud and can interact with each other.






Further Links
______________

Videos about the current development and news are available on `Archtica Youtube Channel <https://www.youtube.com/channel/UCfOGfaqPczXAGTpFDPm8XsA>`_.
Should you find bugs please notify us on `GitHub <https://github.com/Archtica/RADii/issues/>`_.
For errors or inconsistencies in the documentation, please notify us on `Github Radii Documentation Issues`_.



Download Links
___________________

**Grasshopper Plugin**

- `RADii Rhino7 Grasshopper Win/Mac`_
- `RADii Rhino8 Grasshopper Win/Mac`_
- `RADii Capture Win/Mac`_

**PC Viewers**

- `RADii Viewer Windows 10+`_
- `RADii Viewer macOS X`_
- `RADii Viewer VR Oculus`_
- `RADii Viewer VR universal`_

Further viewers for VR, Mobile, Looking Glass and the Webviewer can be found at `RADii.info <https://RADii.info/>`_.


About
___________________

RADii is being developed by Thomas W. Lee since 2020. In 2022 he started a collaboration with Gramazio Kohler Research at ETHZ for further development of the program in the context of the Immersive Design Studio. 
ETH supported this project with a `Innovedum Grant <https://ethz.ch/de/die-eth-zuerich/lehre/innovedum/innovedum-fund.html>`_ , which among other this made this documentation possible.



Table of Contents
==================

.. toctree::
   :maxdepth: 2
   :titlesonly:
   
   Home <self>
   tutorial/Viewer_PC/documentation_rst/0_Viewer 
   tutorial/grashopper/documentation_rst/01_Components_Overview
   tutorial/Quick_Guide/Quick_Guides 
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
  
.. * :ref:`modindex`


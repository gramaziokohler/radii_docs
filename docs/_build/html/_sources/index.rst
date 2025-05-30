.. Radii_documentation documentation master file, created by
   sphinx-quickstart on Mon Oct  9 18:29:30 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. @gereon_: I think, this page needs some restructuring; would like to have a look at it together (also i cannot preview this)
.. @sarah_: I agree, i am under the impression it lacks bite for the welcoming page, would be great to talk about it

.. image:: tutorial/Radii_Icons/Radii_logo.png

**************************
Radii Documentation
**************************

V. 0.40

   
.. @gereon vielleicht braucht es hier bei what is radii mehr einen übergreifenden text, der erklärt, was damit ermöglicht wird. vielleicht hat ja auch thomas dazu irgendwo was? Und das mit den parts würd ich dann weglassen, zumal du hier von 2 parts sprichst, später dann von 3... 



.. topic::  What is RADii ?
      
      RADii was created to easily access 3D models with different devices. Paired with a CAD plugin it creates a powerful real time connection to collaboratively develop 3d Models and discuss them in a VR environment.

..   `RADii <https://RADii.info/>`_ is a cloud platform that allows you to publish 3D Models for sharing, exploration and collaboration. RADii consists of **two parts**: 

.. - A Software **Plugin** for Rhino / Grasshopper to publish 3D Models
.. - A bunch of **Viewers** for various devices (Win/Mac PCs, VR Headsets or mobile devices) .to receive and explore the models.



Example Project
_______________________________________________________________________________ 

.. youtube:: NFQ2JTfqHFc
  :width: 100%
  :align: left

Immersive Design Studio at Gramazio Kohler Research, ETH Zürich, Autumn semester 2023 student project by Gabriel Mösch & Brandon Schwab Rodriguez

.. image example project
   .. image:: tutorial/Viewer_PC/images/01_Start_image.png
      :alt: The empty Radii viewer after starting

  .. image:: tutorial/Viewer_PC/images/231218_cadeim_kytami_Photo_1_WM.jpg
    :alt: Autumn semester 2023, project by Cadei  Matteo & Tami  Kyan  







..  How RADii works section ----------------------------------------------------------------------------------------
.. image:: tutorial/Radii_diagramms/Daten_Diagramme_v2/Artboard_1_4.svg

.. topic:: How RADii works

   A plugin connects your CAD software (Rhino / Grasshopper) and 3D model to the cloud. Through the live connection the geometry and other content is distributed to the RADii Viewers.RADii Viewers exist for different platforms: Win/Mac, mobile devices and VR Headsets. Viewers are connected through the cloud and can interact with each other. This is a simplified representation of what Radii can, a more complete graphic can be found in RadiiGrasshopper_




.. topic:: About

 RADii is being developed by the architect Thomas W. Lee since 2020. From 2022 further development happened in collaboration with Gramazio Kohler Research in the context of the Immersive Design Studio at ETH Zurich. ETH supported this project with a `Innovedum Grant <https://ethz.ch/de/die-eth-zuerich/lehre/innovedum/innovedum-fund.html>`_ , which made this made this documentation and further proliferation possible.

.. @gereon_ diese Seite wäre vielleicht gut, mal als text an Thomas zu schicken. Ich denke, er hat da vermutlich das richtige wording, das auszudrücken. Auch das mit der Kollaboration wäre gut, mit Thomas zu diskutieren. ich würde dann die beiden nächsten absätze rausnehmen, und weiter oben versuchen ein video einzubauen ----- geschickt warte auf Antwort 



.. image of Rhino Grsshopper and the Viewer next to each other, felt to confoluted 
  ..Rhino, Grasshopper and Viewer
  _______________________________________________________________________________
  .. image:: /tutorial/Quick_Guide/1_LV_Explo_Images/Rhino_GH_Viewer.png




Further Links
_________________________________________________________________________________

Videos about the current development and news are available on `Archtica Youtube Channel <https://www.youtube.com/channel/UCfOGfaqPczXAGTpFDPm8XsA>`_.
If you find any bugs, please notify us on `GitHub <https://github.com/Archtica/RADii/issues/>`_.
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

Further viewers for VR, Mobile, Looking Glass and the Webviewer can be found on `RADii <https://RADii.info/>`_.




Table of Contents
==================

.. toctree::
   :maxdepth: 2
   :titlesonly:
   
   Home <self>
   tutorial/Quick_Guide/Setup/1_install_overview.rst
   tutorial/Quick_Guide/Quick_Guides
   tutorial/Viewer_PC/documentation_rst/0_Viewer 
   tutorial/grashopper/documentation_rst/01_Components_Overview
   
   
   
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
  
.. * :ref:`modindex`


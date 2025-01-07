********************
PublishTransform
********************

.. image:: ../images/Publish/Publish_transformation.png
  :scale: 40 %

.. topic:: Definition

  Transforms geometry in the viewer by sending transformations. The geometry is then transformed localy in the viewer which make very fast and smooth change to it possible, as only positions and no new geometry is send.
  Currently transform inputs from move, rotate and scale are supported.
  They can be send as a single transformations or by combining them with the "compound" component from the "Transformation" tab in Grasshopper.

.. important:: 

  Currently only move, scale and rotate transformations are supported.


Input
-----------

==========  ======================================  ==============
Name        Description                             Type
==========  ======================================  ==============
Connection  Link with the Connect component         Connection
Ttransform  Transformation to be applied to geom.   Transform
Content     Geometry to be transformed              Radii content
==========  ======================================  ==============

Output
------------

==========  ======================================  ==============
Name        Description                             Type
==========  ======================================  ==============
Log         Documents changes & data send           Text
Content     Connect to a Save component             RADii content
Sequence    Sequence to be saved as content         Radii content
==========  ======================================  ==============

Right click menu
-----------------

.. image:: ../images/Publish/Publish_transformation_menu.png


==========================  ==========================================
Name                        Description
==========================  ==========================================
Transformation Duration     A higher value leads to slower transformation
Transformation Start
Reset                       Resets the geometry to its original position
Transformation End
Replay                      Loops the transformation
Reverse                     Geometry returns to its original state at the end
Animate                     Animates or disregards the transformation of selected inputs
==========================  ==========================================



Video tutorials:
---------------------

RADii: PublishTransform component

.. youtube:: mv7_ne3KI4I
  :width: 100%
  :align: left
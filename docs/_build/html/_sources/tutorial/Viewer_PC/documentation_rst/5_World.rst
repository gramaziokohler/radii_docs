************
World Menu
************
.. image:: /tutorial/Radii_Icons/World.png


.. image:: ../images/World_menu_detail.png
  :align: right
  :scale: 110%

Camera
""""""""""

.. table::
  :align: left 

  ================  =================================
  Field of view     Controls the field of view 
  Sensitivity       Mouse sensitivity
  Speed             Movement speed
  ================  =================================


.. note::

  Turn slow when someone is following you through the project


Effects - turning them off increases performance
""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. table::
  :align: left 

  ==========  ==================================================================================================
  Motion      Motion blur
  Bloom       Makes bright spots bleed at the edges, simulating a real camera
  DOF         Depth of field - distance between closest and furthest part of an image that are in focus
  Chrom       Chromatic effect - adds artifacts to the image, simulating a poor len
  Vignet      Darkening on the edges of images, simulating real cameras
  Inverse     Clipping/sectioning leaves a ghost of the hidden geometry
  ==========  ==================================================================================================

Point Cloud
"""""""""""""""""""""""

.. table::
  :align: left 
   
  ================  =======================================
  Point Size        Size of the Points of the cloud
  Point near size   Increases point sizes near you
  ================  =======================================

.. Note:: 

  Point Clouds are disabled in IOS/Android viewers because they require a lot of computing power

Weather
""""""""

.. table::
  :align: left 
   
  =========== ===========================================================
  Quality     Resolution of the sky, above lv3 not significantly better
  Condition   Types of weather: rainy, foggy and sunny
  Fog density Can hide the horizon but also your model
  =========== ===========================================================

.. Note:: 
  
  for better performance turn weather to sunny, fog off, quality to lowest

Time
"""""""""""""

Transform
""""""""""""

.. table::
  :align: left 
   
  ==========  ==========================================
  Rotation    Rotates all models around the origin
  Scale       Scales all content
  ==========  ==========================================



Select Viewer
"""""""""""""""

.. image:: /tutorial/Radii_Icons/Viewer.png
      


.. image:: /tutorial/Viewer_PC/images/Menu_Viewer_Studio.png
  :scale: 60 %
  :align: right

- ``Standard``
- ``Studio`` = Studio conditions, no weather or horizon, neutral reflections, color can be set with RGB values
- ``Pepper Ghost`` = displays the model in a virtual box
- ``Stereo Shutter`` = for active 3D glasses
- ``Augmented Reality (AR)`` = Available on IOs, Android, Oculus. Displays virtual model in a real environment 

Tracking & Reposition
""""""""""""""""""""""

.. image:: /tutorial/Radii_Icons/Position.png
  :align: left
      

.. image:: /tutorial/Viewer_PC/images/World_menu_tracking.png
  :scale: 70 %

.. attention:: 

  This option has different functions on pc and vr.

  **PC-Viewer**

    - Tracker Method = for using Pepper Ghost viewer mode
    - Tracking is done with a camera and the external software: `Optitrack <https://github.com/opentrack/opentrack/>`_

    Videos:
      
    - `OptiTrack Implementation <https://www.youtube.com/watch?v=jnvcOJw7FeE>`_
    - `OptiTrack Tracking View and Origin <https://www.youtube.com/watch?v=WMEc1gVGah0>`_
    - `OptiTrack Tracking on large screen <https://www.youtube.com/watch?v=CP3z3kR98ZU>`_

  **VR-Viewer**

    - reposition the origin and rotation to a location that is pointed on, the rotation is controlled with the joystick



.. note::

  - in the VR Viewer, the icon opens a different menu that lets you position the X,Y = 0 position and its orientation
  - this is very helpful to precisely place a model in real space 


.. image:: /tutorial/Radii_Icons/Projection.png
  :align: left

Projection
"""""""""""""
   
.. image:: /tutorial/Viewer_PC/images/World_menu_Projection.png
  :scale: 70 %
  :align: right

- Projection = screen size settings

  - you can also edit the overall scale and height of the horizon

Grid 
""""""

Toggles the default floor

Origin
"""""""

Toggles the origin point

Video tutorials:
""""""""""""""""

**Time animation**

.. youtube:: nheVCJKet8k
  :width: 90%
  :align: left

|

**Scaling**

.. youtube:: 72bPt8c2lzM
  :width: 90%
  :align: left
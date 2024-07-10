******************
PublishGeometry
******************


.. image:: ../images/Publish/Publish_geometry.png
    :scale: 80 %

.. topic:: Definition

  This component is used to select geometry that should be published to a channel.

**Input**

.. table::
  :align: left

  =========== ================================ ================
  Name        Description                         Type
  =========== ================================ ================
  Connection  Link with the Connect component     Connection
  Geometry    Geometry you want to upload         Brep or Mesh
  Quality     Mesh Quality for conversion         Settings
  =========== ================================ ================


.. important:: 

 - RADii converts all Rhino surfaces and polysurfaces to meshes. 
 - The automatic mesh conversion often produces many faces which results in big amount of data and longer loading times.
 


.. Tip::

  **Quality:** 
  To control the conversion process to meshes and the smoothness of your geometry you can use the following gh components:

      - Setting (Speed)
      - Setting (Quality)
      - Setting (Custom)

        - use "Min Edge" to sett the minimal edge length this will make your model low poly if you go to high

**Output**

.. table::
  :align: left

  =========   =====================================   ===================
  Name        Description                             Type
  =========   =====================================   ===================
  Log         Documents changes & data send           Text
  Content     Connect to Save component for saving    RADii content
  =========   =====================================   ===================


.. Tip::

  **Log:** helps to identify how much and what kind of data is sent


**Menu:**

.. table::
  :align: left

  ==========  =====================================================
  Update:     update only changed geometry
  Rebuild:    republish everything in the component
  Render:     visible/invisible
  Collision:  permeable/impermeable
  Physics:    objects push on each other
  Gravity:    9.807 m/s² pulling on each object
  Shared:     collaborative editing of geometry in the viewer
  ==========  =====================================================

**Video tutorials:**

- `Collaborative content modification <https://www.youtube.com/watch?v=YuBep3x01cE>`_
  
  - activate the "Shared" option in the menu
- `Collaboration  <https://www.youtube.com/watch?v=PVB9a0dsJfQ>`_ 

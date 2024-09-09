********************************
Tutorial: Collaborative Working
********************************

.. topic:: What this is about

  Radii can be used in a linear way, sending commands and geometry from your CAD to connected viewers. The RADii subscribe components (`Subscribe Geometry`_, `Subscribe User`_, `Subscribe Parameter`_, `Subscribe Curve`_, `Subscribe PointCloud`_, `Subscribe Message`_    ) can add the reverse diction to the workflow. This means, that data from the viewers can be imported back into your CAD software. We will give a few examples of working with these components that we found useful. 



Collaborative Geometry Modification
-----------------------------------------------------------------------

Geometry is first send from Grasshopper with PublishGeometry_ to the viewers, it is important that the shared option is selected in the component.
The geometry can then be modified in the viewer in collaboration and fed back into Rhino via the `Subscribe Geometry`_ component.
After baking or internalizing the fed back geometry it can be permanently stored.

.. image:: ../Quick_Guide/4_LV_Subscribe_Images/Subscribe_Geometry_Grasshopper_viewer.png

.. image:: ../Quick_Guide/4_LV_Subscribe_Images/Subscribe_Geometry_Grasshopper.png


.. topic:: Components needed:

  - `Connect`_
  - PublishGeometry_
  - PublishMaterial_
  - `Subscribe Geometry`_




Recording the viewers movement and using it to create an animation path.
---------------------------------------------------------------------------
  
It can be quiet difficult to create a smooth animation path with Rhino, this can be done by recording the movement of the viewer and using it to create an animation path as shown in the example below.

.. image:: ../Quick_Guide/4_LV_Subscribe_Images/Recording_Path_viewer_planes_icons_rhino.png
  
.. topic:: Components needed:

  - `Connect`_
  - `Subscribe User`_
  - Data Recorder
  - Cull Duplicates
  - List Item
  - `Publish Animation`_

   


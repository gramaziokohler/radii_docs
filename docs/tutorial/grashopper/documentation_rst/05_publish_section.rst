.. RevSarah

****************
PublishSection
****************

.. image:: ../images/Publish/Publish_section.png
    :scale: 80 %

.. topic:: Definition
    
  This component is used to publish clipping planes from Rhino or directly from Grasshopper to a channel.


**Input**

.. table::
  :align: left
    
  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Connection  Link with the Connect component         Connection
  Section     Select A plane that will cut the model   Plane/surfaces
  Index       Select a plane from a list              Number
  ==========  ======================================  ==============

.. tip::

   - Rhino clipping planes are automatically imported and have to be selected in the menu below ``-Activate clipping planes-``
   - If you hav connected one or multiple surfaces with the input: ``Section Plane``, you have to connect a number slider with ``index`` to select them.

**Output**

.. table::
  :align: left

  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Log         Document changes & Data sent            Text
  Content     Connect to Content                      RADii content
  ==========  ======================================  ==============

**Right click menu**

.. table::
  :align: left

  ==========================  ================================================
  Section Duration:           how quickly the section is moving into place
  Set duration:               toggle to have a moving clipping plane
  Activate clipping planes:   clipping planes from rhino to be selected
  ==========================  ================================================

.. tip:: 
  
  - In Rhino flipping a clipping plane is not recognized by Radii, rotating the plane by 180° however achieves the same
  - Names of clipping planes are not carried over into the Grasshopper plugin at the time of writing

Video tutorials:
-----------------

- `Publish Section city scale <https://www.youtube.com/watch?v=5zsiGtmGIz4>`_
- `Publish Section building scale <https://www.youtube.com/watch?v=3mJXLDXxK8o>`_
- `Section Pointcloud <https://www.youtube.com/watch?v=JkuKp_Q2p2A>`_

************
PublishView
************

.. image:: ../images/Publish/Publish_view.png
    :scale: 80 %

.. topic:: Definition
  
  This component is used to publish saved views to all Subscribers of a channel. All present Subscribers will be moved to the selected view.

- there are two ways to import views:
  
  - Grasshopper via the component input
  - Saved Rhino views are accessible in the component menu

Input
---------

.. table::
  :align: left

  =============   ======================================  ==============
  Name            Description                             Type
  =============   ======================================  ==============
  Connection      Link with the Connect component         Connect
  Camera Planes   Planes to define viewpoints             Plane
  Lens Length     Lense to describe the field of view     Number
  Index           To switch between views                 Number
  =============   ======================================  ==============

Output
------------

.. table::
  :align: left
    
  =======   ======================================  ==============
  Name      Description                             Type
  =======   ======================================  ==============
  Log       Document changes & Data sent            Text
  Save      Connect to SaveContent for saving       RADii content
  =======   ======================================  ==============

Right click menu
-----------------

.. table::
  :align: left
    
  =========== ======================================  
  View        Duration Speed to switch between views
  Active view Rhino Views
  =========== ======================================

.. note:: 

  RADii uses the camera lense length thas is saved with your Rhino views, if you select one of your saved Rhino Views from the Right click menu. So you have to change it in your Rhino Saved Views settings.

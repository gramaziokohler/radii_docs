******************
PublishAnimation
******************

.. image:: ../images/Publish/Publish_animation_2.png
    :scale: 80 %


.. topic:: Definition
    
  This component is used to publish animations to a channel.
  If no content is given as an input, all Viewers present will be subjected to the animation, similar to a dolly camera.
  In case content is connected to the component, the animation will be applied to the geometry. 
  At least 3 planes are necessary for an animation.


Input
---------

.. table::
  :align: left
    
  =================   ========================================    =======================================
  Name                Description                                 Type
  =================   ========================================    =======================================
  Connection          Link with the Connect component             Connect
  Animation Planes    Along the path you want to animate          Planes
  Lens Length         Lense to describe the field of view         Number
  Content             Geometry you want to animate                Save of Publish Geometry component
  =================   ========================================    =======================================


Output
------------

.. table::
  :align: left
    
  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Log         Document changes & Data sent            Text
  Content     Connect to Content                      RADii content
  ==========  ======================================  ==============


Right click menu
-----------------

.. table::
  :align: left
    
  ==========  ==========================================
  Animation   Title / Name of your Animation
  Animation   Duration Speed: higher number = quicker
  Animation   Behavior Play, Replay, Reverse, Return
  ==========  ==========================================

 
Multiple Animations in parallel:
--------------------------------------

To play multiple animations in parallel with one component, use the following setup:

.. image:: ../images/Publish/Publish_animation_parallel_schaltplan.png


Videos
------------

**Object Animation example**

.. youtube:: yMZXNn_Pgq4
  :width: 90%
  :align: left

|

**Animation example**

.. youtube:: 9h1RwmqvWDQ
  :width: 90%
  :align: left

|

**Object animation**

.. youtube:: yMZXNn_Pgq4
  :width: 90%
  :align: left

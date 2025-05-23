*********************
PublishPointcloud
*********************

.. image:: ../images/Publish/Publish_Pointclouds.png
    :scale: 90 %

.. topic:: Definition

  This component is used to publish Pointclouds to a channel.

.. tip:: 
  
  Pointclouds have a tendency to be very heavy and can make your viewer choke. In those cases see `Tools Pointcloud`_ to reduce their size.


Input
---------

.. table::
  :align: left

  ===========  ======================================  ==============
  Name         Description                             Type
  ===========  ======================================  ==============
  Connection   Link with the Connect component         Connect
  Point Cloud  Input for a Point cloud                  Point cloud
  ===========  ======================================  ==============




Output
------------

.. table::
  :align: left
    
  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Log         Document changes & Data sen             Text
  Content     Connect to Content                      RADii content
  Sequence    Sequence to be saved as content         Radii content
  ==========  ======================================  ==============



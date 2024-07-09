*********************
SubscribePointCloud
*********************

.. image:: ../images/Subscribe/Pointcloud.png

.. topic:: Definition
  
  This component is used to subscribe to Pointclouds that are published to a channel.

**Input**

.. table::
  :align: left
    
  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Connection  Link with the Connect component         Connection
  Filter      Filter own publication/broadcast        Boolean
  Subscribe   Toggle the subscription                 Boolean
  ==========  ======================================  ==============

**Output**

.. table::
  :align: left

  =========== ======================================  ==============
  Name        Description                             Type
  =========== ======================================  ==============
  Point Cloud Element to work with                    Point Cloud
  =========== ======================================  ==============
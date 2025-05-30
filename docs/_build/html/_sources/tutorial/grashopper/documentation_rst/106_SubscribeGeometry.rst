********************
SubscribeGeometry
********************

.. image:: ../images/Subscribe/Sub_geometry.png

.. topic:: Definition
    
  This component is used to subscribe to geometry that is published to a channel.

Input
---------

.. table::
  :align: left
    
  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Connection  Link with the Connect component         Connection
  Filter      Filter own publication/broadcast        Boolean
  Subscribe   Toggle the subscription                 Boolean
  ==========  ======================================  ==============

Output
------------

.. table::
  :align: left
    
  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Log         Documents changes & Data send           Text
  Geometry    Element to work with                    Geometry
  ==========  ======================================  ==============


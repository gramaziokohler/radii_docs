****************
SubscribeCurve
****************

.. image:: ../images/Subscribe/Sub_curve.png
    :scale: 90 %

.. topic:: Definition

  This component is used to subscribe to curves that are published to a channel.

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
    
  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Log         Documents changes & Data send           Text
  Curve       Element to work with                    Curve
  ==========  ======================================  ==============
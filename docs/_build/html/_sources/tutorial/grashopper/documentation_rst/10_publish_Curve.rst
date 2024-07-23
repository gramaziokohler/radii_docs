.. RevSarah

*************
PublishCurve
*************

.. image:: ../images/Publish/Publish_curve.png

.. topic:: Definition
    
  This component is used to publish lines, polylines or curves to a channel.

*Option:* The line weight can be controlled by setting it in the Rhino layer or directly on the object, after baking the curves.

.. important:: 
  Curves will be converted into line segments. Be Careful with the max. and min. edge length, it can create a lot of data if the values are too small.
  Curves are not a very efficient geometry and can slow down the model if you publish many of them.

**Input**

.. table::
  :align: left

  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Connection  Link with the Connect component         Connect
  Curve       the curves to publish                   Curve
  MinEdge     Min length of segments                  Number
  MaxEdge     Max length of segments                  Number
  ==========  ======================================  ==============

**Output**

.. table::
  :align: left
    
  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Log         Document changes & Data sent            Text
  Content     Connect to Content                      RADii content
  ==========  ======================================  ==============





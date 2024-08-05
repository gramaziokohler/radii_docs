*******************
SubscribeParameter
*******************

Grasshopper component
-------------------------

.. image:: ../images/Subscribe/Sub_parameter.png
    
.. topic:: Definition

  This component is used to subscribe to a parameter that is set in a RADii Viewer or by `Publish Parameter`_ , it can then be changed in the Viewer and fed back into the Grasshopper session with this component.


Radii viewer counterpart
--------------------------

.. image:: ../images/Subscribe/Sub_parameter22.png


.. tip::

  Values from SubscribeParameter could be used to modify geometry in a Grasshopper algorithm.


Input
---------

.. table::
  :align: left
    
  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Connection  Link with the Connect component         Connection
  Subscribe   Toggle the subscription                 Boolean
  ==========  ======================================  ==============

Output
------------

.. table::
  :align: left
    
  ==================  ======================================  ==============
  Name                Description                             Type
  ==================  ======================================  ==============
  Log                 Documents changes & Data send           Text
  Parameter/Boolean   Parameter/Boolean from Radii Viewer     Boolean/Number
  ==================  ======================================  ==============

.. note:: 

  - The more parameters you define in the viewer, the more will be on this component
  - The number will be between 0 to 1, you can remap this to any other range



.. icon Menu

.. image:: /tutorial/Radii_Icons/publish_circle_48.png
    :scale: 60

************
Publish Menu
************

  This menu allows for the control of other viewers, the publication of content and the publication of 
  parameters to Rhino sessions that have subscribed to this specific viewer.

.. image:: ../images/Publish_menu_detail.png
    :align: right
    :scale: 100%

Published content
"""""""""""""""""""""

- controls the type of content that is published with this viewer

Publish control
""""""""""""""""""""""

Allows for the control of other viewers on the channel.

.. table::
  :align: left 
    
  =========   =================================================================
  Control     This viewer's settings are forced on all other viewers
  Follow      viewers on the channel are forced to follow this viewer's movement
  Merge       control and follow in one button
  =========   =================================================================

.. note::

  To Publish control, the active viewer has to be a member auf the channel


Parameters
""""""""""""

Send parameters back to Rhino Grasshopper that can be received with `Subscribe Parameter`_ 


**Add by** typing a ``name`` and then click one of the options:

.. table::
  :align: left 

  ======================================================  =====================================
  .. image:: /tutorial/Radii_Icons/Circle.png             Boolean (on/off)
  .. image:: /tutorial/Radii_Icons/Control.png            Slider (Number between 0 and 1)
  .. image:: /tutorial/Radii_Icons/Numb_Parameter_24.png  Integer (0,1,2, ...)
  ======================================================  =====================================


Video tutorial:
""""""""""""""""

- `Parameters <https://www.youtube.com/watch?v=d4HaI0gQRH4>`_
- `Voice chat and viewer to viewer control`_
.. RevSarah

****************
PublishControl
****************


.. image:: ../images/Publish/Publish__controll_new_menu.png
    :scale: 80 %

.. topic:: Definition
    
  Publish Control lets you control the Viewers settings from Grasshopper.

.. note::

  The scenario Manager was spun of into `Save Scenario`_ and the loading of references into `Publish Reference`_ in v 039.B2 from PublishControl
  


**Input**

.. table::
  :align: left

  =============   ======================================      ==============
  Name            Description                                 Type
  =============   ======================================      ==============
  Connection      Link with the Connect component             Connect
  Time of Year    Day of the Year                             Number
  Time of Day     Time of the day                             Number
  Content Save    Output from other RADii components          save (RADii)
  Index           For switching between scenarios             Number
  =============   ======================================      ==============


**Output**

.. table::
  :align: left

  =============  ======================================      ==============
  Name           Description                                 Type
  =============  ======================================      ==============
  Log            Documents changes & Data send               Text
  Save Control   Saving the controls only                    RADii
  Save Scenario  Save control and geometry                   RADii
  =============  ======================================      ==============


**Right click menu**

.. table::
  :align: left
    
  =================== ============================================================================================
  Name                Description
  =================== ============================================================================================
  Scale               Set the model scale
  Weather             Weather options
  Background color    Set the background color
  Background          Toggle the background color
  Grid                Toggle base floor
  Origin              Toggle origin sign
  Labels              Toggle all labels
  Fly                 Forces viewers to fly
  Set position        Set the camera of your active Rhino viewport as position
  Save position       Include the position in a scenario save
  Clear               Clears all content from viewers
  Set Location        Sets the world location for the sun
  Origin rotation     Rotates the model by x-degrees
  Set origin rotation Confirm rotation
  =================== ============================================================================================



Video tutorials:
---------------------

- `Publish Control overview <https://www.youtube.com/watch?v=-_7DvX_-9uY>`_
- `Publish Control cloud load <https://www.youtube.com/watch?v=9upFjrH9zrE>`_


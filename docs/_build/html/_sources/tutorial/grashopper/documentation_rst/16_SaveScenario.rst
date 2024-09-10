**********************
Save Scenario
**********************

.. image:: ../images/Save_Content/Save_scenario_manager.png

.. topic:: Definition

  The Scenario Manager can collect all type of content, views, references, settings and more into scenarios, that can then be called into a viewer at once.
  With scenarios it is possible to do more complex presentations.
  
.. attention:: 

  Be careful or refrain from saving geometry content into this component with scenarios, instead use `Save Scenario`_ to save to the cloud and `Publish Reference`_ to download it. Otherwise the Grasshopper file can get very heavy and slow.
  


.. tip:: 

  - The ``Content`` output can be saved to the cloud with `Save Content`_
  - Grasshoppers autosave can be deactivated when the saving takes to long

Input
---------

==========  ========================================= ==============
Name        Description                               Type
==========  ========================================= ==============
Connection  Link with the Connect component           Connection
Content     Content to be bundled into one scenario   RADii content
Index       To switch between scenarios               Integer
==========  ========================================= ==============

Output
------------

==========  ======================================  ==============
Name        Description                             Type
==========  ======================================  ==============
Log         Documents changes & data send           Text
Content     Connect to a Save component             RADii content
==========  ======================================  ==============





Scenario Manager
-----------------------

.. image:: ../images/Save_Content/Save_Scenario_controll_manager.png
    :scale: 80 %
    :align: left

=================== ============================================================================================================================
Scenario Name       The name you want to give your scenario
Save                Save the scenario, can be used to save on top of existing scenarios
Rename  	          Renames a scenario
Clear               Clears the scene before a scenario
Duration            Length of the scenario when played in the viewer in auto mode
Add/Replace content New content will be added and existing updated. If used with existing content that has zero elements, it will delete it from the scenario
=================== ============================================================================================================================

**Column titles**

==========  ==============================================================================================
Blank       Index of the scenario
Scenario    Name of the scenario
Content     is content sent (geometry, views, etc.) you could just send settings (time, position etc.)
Clear       Clears the channel before uploading new geometry
Load        Indicated if loading content via `Publish Reference`_ is included 
Duration    of the scenario when played on auto play in the viewer
==========  ==============================================================================================

An example on how to use the component can be found in the Guide at `Tutorial Advanced Presentation`_
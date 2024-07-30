**********************
Save Scenario
**********************

.. image:: ../images/Save_Content/Save_scenario_manager.png

.. topic:: Definition

  The Scenario Manager can collect all type of content, views, references, settings and more into scenarios, that can then be called into a viewer at once
  With scenarios it is possible to do more complex presentations at ease.
  
.. attention:: 

  Be careful or refrain from saving geometry content into this component with scenarios, instead use `Publish Reference`_ to download it. Otherwise the Grasshopper file can get very heavy and slow.
  


.. tip:: 

  - Content from save Scenario can be saved to the cloud with `Save Content`_
  - Grasshoppers autosave can be deactivated, in case it takes to long 
  - To save time with heavier and bigger models: `Publish Reference`_  can direct all viewers to download a previously saved file that was saved to a channel, instead of live uploading and then downloading to the viewers.


**Input**

==========  ========================================= ==============
Name        Description                               Type
==========  ========================================= ==============
Connection  Link with the Connect component           Connection
Content     Content to be bundled into one scenario   RADii content
Index       To switch between scenarios               Integer
==========  ========================================= ==============

**Output**

==========  ======================================  ==============
Name        Description                             Type
==========  ======================================  ==============
Log         Documents changes & data send           Text
Content     Connect to Save component for saving    RADii content   
==========  ======================================  ==============





Scenario Manager
-----------------------

.. image:: ../images/Save_Content/Save_Scenario_controll_manager.png
    :scale: 80 %


=================== ============================================================================================================================
Scenario Name       The name you want to give your scenario
Save                Save the scenario, can be used to save on top of existing scenarios
Rename  	          Renames a scenario
Clear               Clears the scene before a scenario
Duration            Length of the scenario when played in the viewer in auto mode
Add/Replace content New content will be added and existing updated. If used with existing content that has zero elements, it will delete it from the scenario
=================== ============================================================================================================================

**Column descriptions**

==========  ==============================================================================================
Blank       Index of the scenario
Scenario    Name of the scenario
Content     is content sent (geometry, views, etc.) you could just send settings (time, position etc.)
Clear       Clears the channel before uploading new geometry
Load        loading from the channel
Duration    of the scenario when played on auto play in the viewer
==========  ==============================================================================================

.. @Gereon: I would remove the examples below and link to a video or tutorial - keeping things here clean structure wise

Examples
------------------------

The plan is to do the following: Geometry (a building) that has to be publish or downloaded from the server (1), then a walk through it, change the time of the day and the weather (2) and continue your tour via a series of pre defined views (3-4).

Setting and sending the above mentioned live during a presentation takes a lot of time. It is quicker to collect the content into scenarios and save them. Switch through them during a presentation then becomes more easier and makes more complex presentations possible.



**1)**

.. image:: ../images/Publish/Scenario_Manager_examples/1.png
  :alt: 1)

**2)**

.. image:: ../images/Publish/Scenario_Manager_examples/2.png
  :alt: 2)


**3-4)**

.. image:: ../images/Publish/Scenario_Manager_examples/3.png
  :alt: 3-4)

.. image:: ../images/Publish/Scenario_Manager_examples/4.png  
  :alt: 3-4)
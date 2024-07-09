




.. image:: ../images/Publish/Publish_scenario_manager.png


It contains the Scenario Manager that can save setting and all other content into a scenario to be played at once. With scenarios it is possible to do more complex presentations.
  
  - Be careful with saving geometry content into this component, this can make your Grasshopper file very heavy. 
  


.. tip:: 

  Grasshopper has an autosave function as a default setting. If the Publish Control component becomes too heavy, it will make you wait a lot



.. tip:: 

  - The saved content is stored in the component, be aware that huge amounts of geometry can make your .gh file very heavy and slow
  - In this case turn off the grasshopper autosave setting as it will slow you down
  - To save time with heavier and bigger models: with `Publish Reference`_ you can direct all viewers to download a saved file from a channel, instead of live uploading and then downloading to the viewers.



Scenario Manager
-----------------------

.. image:: ../images/Publish/Publish__controll_manager.png
    :scale: 80 %

The scenario manager saves the selected options of the Publish Control component and content that is connected to it into scenarios that can be played in succession. 


==============  ============================================================================================================================
Scenario Name   The name you want to give your scenario
Save            Save the scenario, can be used to save on top of existing scenrios  
Update          Updates time set and settings that can be set in publish control but not geometry
Rename  	      Renames a scenario
Clear           clears the scene before a scenario
Duration        length of the scenario
==============  ============================================================================================================================

**Column descriptions**

==========  ==============================================================================================
Blank       Index of the scenario
Scenario    Name of the scenario
Content     is content sent (geometry, views, etc.) you could just send settings (time, position etc.)
Clear       Clears the channel before uploading new geometry
Load        loading from the channel
Duration    of the scenario when played on auto play in the viewer
==========  ==============================================================================================


**Examples**

You have some geometry (a building) and want to publish or download from the server (1), then walk through it, change the time of the day (2) and
continue your tour via a series of pre defined views (3-4).
Instead of setting everything live during your presentation, you define one position after the other and save
them as individual scenarios. You then can switch through them during your presentation more easily.


**1)**

.. image:: ../images/Publish/Scenario_Manager_examples/1.png

**2)**

.. image:: ../images/Publish/Scenario_Manager_examples/2.png

**3-4)**

.. image:: ../images/Publish/Scenario_Manager_examples/3.png

.. image:: ../images/Publish/Scenario_Manager_examples/4.png  
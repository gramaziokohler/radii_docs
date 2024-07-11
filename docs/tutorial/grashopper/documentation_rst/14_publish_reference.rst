.. RevSarah

******************
PublishReference
******************

.. image:: ../images/Publish/Publish_Reference/Publish_reference.png
    

.. topic:: Definition
    
  With the reference manager you can load RADii content that has been saved on the cloud (see: `Save Content`_) to a specific channel, to make it accessible for connected viewers.
  The component can be connected to `Publish Control`_ & `Save Content`_ to automatically load and show different configurations of references. 
  By making geometry active (loading), you can very quickly switch between visibility states without additional loading times (which can occur with bigger models).    


**Input**

.. table::
  :align: left

  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Connection  Link with the Connect component         Connection
  ==========  ======================================  ==============

**Output**

.. table::
  :align: left
    
  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Log         Document changes & data sent            Text
  Content     Connect to Save component for saving    RADii content   
  ==========  ======================================  ==============

**Menu**

.. @Gereon: somehow i find the table hard to read - lets discuss this 


.. image:: ../images/Publish/Publish_Reference/Publish_reference_manager.png
    :scale: 90%

.. table::
  :align: left
    
  =====================   ==========================================
  Name                    Description                           
  =====================   ==========================================
  Channelname             Channel to access references from
  Refresh                 Update List
  List                    Names of Geometry Collections on the channel
  Reference collection    For collecting references from channels
  Active                  Loads the Reference to all viewers
  Visible                 Shows the Reference to all viewers
  =====================   ==========================================


.. tip:: 

    To add items to the Reference collection, just doubleclick any file from the list above. 
    If your reference is on a different channel, type in the channel name, hit ``Enter`` and ``Refresh`` to update the content.
    You can add references from different channel to the Reference collection.

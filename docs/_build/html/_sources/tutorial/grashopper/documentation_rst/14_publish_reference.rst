.. RevSarah

******************
PublishReference
******************

.. image:: ../images/Publish/Publish_Reference/Publish_reference.png
    

.. topic:: Definition
    
  With the reference manager you can load RADii content that has been saved on the cloud (see: `Save Content`_) to a specific channel, to make it accessible for connected viewers.
  The component can be connected to `Publish Control`_ & `Save Content`_ to automatically load and show different configurations of references. 
  By making geometry active (loading), you can very quickly switch between visibility states without additional loading times (which can occur with bigger models).    


Input
---------

.. table::
  :align: left

  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Connection  Link with the Connect component         Connection
  ==========  ======================================  ==============

Output
------------

.. table::
  :align: left
    
  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Log         Document changes & data sent            Text
  Content     Connect to Save component for saving    RADii content   
  ==========  ======================================  ==============

Right click menu
-----------------

.. @Gereon: somehow i find the table hard to read - lets discuss this - fliestext schreiben



.. image:: ../images/Publish/Publish_Reference/Publish_reference_manager.png
    :scale: 80%
    :align: left

The first ``text field`` is for the the channel name to be accessed, right next to it the ``refresh button`` to manually update the ``list of content`` below it, in case that is necessary. 
Double click on content of the list to collect a reference into the second list, the ``reference collection``. The collection has three options to interact with the content: ``Active`` to load a reference to all viewers, ``Visible`` defines the references visibility for all viewers and ``delete`` to remove an item from the collection. 


.. 
  .. table::
    :align: right
      
    =====================   ==========================================
    Name                    Description                           
    =====================   ==========================================
    Channelname             Channel to access references from
    Refresh                 Update list
    List of content         Display of geometry collections on the selected channel
    Reference collection    For collecting references from the current and different channels
    Active                  Loads the reference to all viewers
    Visible                 Shows the reference to all viewers
    =====================   ==========================================


.. tip:: 

    To add items to the Reference collection, just doubleclick any file from the list above. 
    If your reference is on a different channel, type in the channel name, hit ``Enter`` and ``Refresh`` to update the content.
    You can add references from different channel to the Reference collection.

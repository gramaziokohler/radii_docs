*******************************************
Technical Information
*******************************************


.. @gereon: I think this should become two sections -- Done. maybe have the technical things somewhere else; 
.. i feel that the content of the index, the quick guides and some content from here might need some restructuring.
.. also we should make sure, that the structure here in the explorer matches the chapters names
.. @sarah reply: i agree with the restrucuturing, i will attempt to give this a quick rework
.. regarding the file names an the heading - they did change a lot in the past which is why i did not do the extra work to go through the .conf file and relink them


PC/Mac
^^^^^^^^^^^^

While the Radii Viewer can run on relatively simple machines, the resources necessary scale with the complexity of the model and the level of its optimisation.
As a live renderer the Radii Viewer needs more computing power than the CAD Software (Rhino). A model that is almost to complex in Rhino, will not run on a device in the Viewer.
For very big models it can be necessary to run the Rhino Editor on a different device than the viewer.


.. @sarah i feel like best practices might be at the wrong place here ?



For 32bit system there is a limit of 2GB for each component and saves.

.. topic:: Radii PC requirements:
  
  - ideally min. 4 GB of RAM but also works with 2 GB for small projects
  - a graphics card of medium strength or higher
  - Rhino 3D license to use Grasshopper (only necessary for the Plugin)

.. tip::

  In the cases of very big models it is the best practice to save them to the cloud before a presentation and then commanding a load to the viewers through the `Publish Reference`_ component.

.. topic:: Oculus Quest 2

  - for Pointclouds we found a performance limit of 100 000 Points

  **Best practice:** 
  - in our design studio we found that smaller models such as 1:1 konstruction detail mockups in the pass through mode worked best for the hardware. 
 

Server Storage and channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By registering at `RADii.info`_ you get aces to your own channel on the Radii server.
If you would like to have a specific domain, your own server, unlimited or local storage contact RADii at contact@RADii.info.
 
  - **Unregistered users**:

    - publish limit : 250 mb
    - save limit    : 50 mb
  
  - **Registered users**:

    - publish limit : 500 mb
    - save limit    : 250 mb 
  
  - **Organizations**: Can be defined in coordination with Radii, please write to contact@RADii.info



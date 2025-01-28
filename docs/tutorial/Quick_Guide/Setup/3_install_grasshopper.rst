________________________________________
Setup/Update RADii Grasshopper Plugin
________________________________________

At the time of wrtiting the plugin only runs with `Rhino 3D <https://www.rhino3d.com/>`_ 
We are working on a version for other 3D software and an API for further custom implementations.

The plugin enables you to publish (send) 3D models and other geometry. 
Publishing works is similar to a Radio station, geometry can be received by others as long as they are connected to the same channel as the sender. Once the publisher leaves the channel the geometry is no longer available unless it was saved to the cloud.

1. **Download** the latest Radii Plugin from https://RADii.info/
2. If you did not already: **Register** in the user panel **and confirm** your email 
3. **Unpack** the .Zip file 
4. **Drag & drop** the Radii.gha file it into the Rhino Grasshopper window, you open it by typing the "grasshopper" command in Rhino
5. **Check** if the install was successful, it should be visible in one your tabs as shown below.

.. image:: ../Setup/Images/Grashopper_Blank_install.png

**Congratulations !** you have installed Grasshopper Radii. On how to publish consult the Quick Guide and the Radii Grasshopper documentation


Update
-------------

1. Open the grasshopper component folder 
   
   .. image:: ../Setup/images/Grashopper_components_folder.png

2. Close Rhino 
3. Delete Radii.gha
4. Start from 1 in the setup



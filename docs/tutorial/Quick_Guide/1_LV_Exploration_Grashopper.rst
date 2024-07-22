.. ------Header
    _ Hyperlinks that are written xxxxx_ are collected in the conf.py so they can be modified at any time more easily.

.. |RadiiLogo| image:: ../Radii_Icons/Radii_logo.png
    :height: 50


************************************
Tutorial: Grasshopper Basics
************************************


Length: ca. 10 min

This tutorial is based on the `Grasshopper Setup`_ guide.

It will introduce the basics of the RADii Grasshopper plugin.
With it, you will be able to publish(upload) geometry on a RADii channel.

We advice to make a Radii account at `RADii.info`_ if you want to have your personal space and more storage.
More detail about the components can be found at RadiiGrasshopper_ in the documentation.

.. attention:: 

    The following tool will Publish/Upload all the Geometry in your rhino file. Use it with care and not with big models.





How to build a basic file to publish
--------------------------------------------

.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/01_Quick_Guide_Publisher.png

Every RadiiGrasshopper_ file starts with the Connect_ component.
To it, you connect the PublishMaterial_ |PublishMaterial_icon| and the PublishGeometry_ |PublishGeometry_icon|, components.
Add a ``geometry input`` to the later, in our example we are using the ``geometry pipeline`` as shown in the picture.



.. |Connect| image:: /tutorial/Radii_Icons/ConnectParam.png
.. |PublishMaterial_icon| image:: /tutorial/Radii_Icons/Material.png
.. |PublishGeometry_icon| image:: /tutorial/Radii_Icons/Mesh.png






Enter Credentials
-----------------------


.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/02_Quick_Guide_Publisher.png

Log in with your `Radii.info`_ account and password you have created during the `Grasshopper Setup`_ and left click on ``load account`` to log in.
Your private domain will show up under the section ``- CHANNEL -`` and possibly others if you are part of a class or group.

Choose domain and channel
-------------------------------

.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/03_Quick_Guide_Publisher_zugeschnitten.png


Right click on the Connect component, there should be a tick next to ``username >  My Domain``, in this state your would publish your geometry on on your personal channel.
More information about channel addresses can be found at Connect_.
Change the tick to its respective Domain name.
Press ``Enter`` to confirm.


.. attention::
    You have to publish to the same channel that you are connected with in the viewer - typos leave you stranded.




Connect
---------------

.. image:: ../Quick_Guide/1_LV_Explo_Images/Grashopper/05_Quick_Guide_Publisher_true.png
    :scale: 80 %

To activate the connection to the channel ``double click`` on the dark ``false`` on the ``Boolean Toggle`` to turn it into ``true``, as shown in the picture above.




**Congratulations, your model should now appear in your Radii viewer!**

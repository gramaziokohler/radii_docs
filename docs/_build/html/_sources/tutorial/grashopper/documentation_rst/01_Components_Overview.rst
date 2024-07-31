.. RevSarah

********************
RADii Grasshopper
********************

.. image:: ../images/all_components.png
    :scale: 120 %

Types of components:
------------------------

| **1. Connect** is the fundamental component to connect to a channel, it is always connected to all components.
| **2. Params** relay or link the described datatype
| **3. Publish** components send different types of data from CAD software to a channel and its connected viewers.
| **4. Save** enables you to save locally to .RADii files or on a channel in the cloud.
| **5. Subscribe** imports data from a viewer back to your local Rhino Grasshopper session.
| **6. Tools** to modify point clouds and meshes 



Data flow diagram RADii
----------------------------

.. image:: /tutorial/Radii_diagramms/Daten_Diagramme_v2/Artboard14.png
    :alt: Diagram of all ways in which data can be sent, stored and received with RADii

Diagram of all ways in which data can be sent, stored and received with RADii

| **Publishing** sends data from the CAD software through the cloud to a RADii Viewer.
| **Subscribe** imports data from a RADii Viewer though the cloud back to the CAD software.
| `Publish Reference`_ allows for data that was stored in the cloud to be downloaded to viewers without having to directly upload it again.
| `Save Content`_ can save all publishing content to the cloud or locally as a .RADII file. The viewers can then manually download them from the cloud or import locally.
| Viewers can save all content they have received into a local .RADII file.  




Grasshopper Components
-----------------------


<<<<<<< HEAD
.. @gereon right click menu is how menu should be called from now on no :

.. write a style guide: tips for optional attention for important etc. put it in the vorlage page
=======
>>>>>>> d9dad86e67a605785884263307abbe97a81984ac


.. Note: the naming in toctree is case sensitive

Connect Components
_____________________

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *connect


Publish Components
____________________

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *publish*


Save Components
________________

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Save*

Params Components
___________________

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Params*

Subscribe Components
_________________________

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Subscribe*


<<<<<<< HEAD


**Tools Components**
=======
Tools Components
_____________________
>>>>>>> d9dad86e67a605785884263307abbe97a81984ac

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Tools*


.. Tip::

    .. toctree::
        :titlesonly:
        :glob:

        *10_Tips*


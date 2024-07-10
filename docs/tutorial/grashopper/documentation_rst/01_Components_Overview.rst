********************
RADii Grasshopper
********************

.. image:: ../images/all_components.png
    :scale: 120 %

There are 6 types of components:

| **1. Connect** is the fundamental component to connect to a channel, it is always connected to all components that are in use.
| **2. Params** relay or link the described datatype  
| **3. Publish** components send different types of data from CAD software to a channel and its connected receivers.
| **4. Save** enables you to save locally to .RADii files or on a channel in the cloud.
| **5. Subscribe** imports data from a viewer back to your local Rhino Grasshopper session.
| **6. Tools** to modify point clouds and meshes

Diagram of all ways in which data can be sent, stored and received with RADii:
-----------------------------------------------------------------------------------

.. image:: /tutorial/Radii_diagramms/Daten_Diagramme_v2/Artboard14.png



Grasshopper Components
-----------------------

.. the naming in toctree is case sensitive
.. here you are missing connect, this should come before publish components

**Connect**
.. @help put the connect link here

**Publish Components**

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *connect
    *publish*

**Save Content**

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Save*

**Params**

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Params*

**Subscribe Components**

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Subscribe*

**Tool Components & Tips**

.. tips von menu unten rausnehmen und als eigenen punkt, formatiert in diesem kasten mit tips

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Tools*
    *10_Tips*
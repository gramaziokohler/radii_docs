********************
RADii Grasshopper
********************

.. image:: ../images/all_components.png
    :scale: 120 %

There are 6 types of components:

| **Connect** is the fundamental component to connect to a channel, it is always connected to all components that are in use.
| **Params** relay or link the described datatype 
| **Publishing** components can send data to a channel and its connected receivers.
| **Save** enables you to save locally to .radii files or on a channel in the cloud.
| **Subscribe** imports data from from a connected channel to your local Rhino Grasshopper session. The data can then be further processed or saved.
| **Tools** to modify point clouds and meshes

**Any way in which data can be sent, stored and received in RADii:**

.. image:: /tutorial/Radii_diagramms/Daten_Diagramme_v2/Artboard14.png

Grasshopper Components
_____________________________

.. the naming in toctree is case sensitive

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

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Tools*
    *10_Tips*
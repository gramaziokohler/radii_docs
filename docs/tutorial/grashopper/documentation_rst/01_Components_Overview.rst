.. RevSarah

******************************
RADii Grasshopper
******************************

.. image:: ../images/all_components.png
    :scale: 120 %

Types of components
------------------------

| **1. Connect** is the fundamental component to connect to a channel, it has to be connected to all components for publishing.
| **2. Params** relay or link the described datatype
| **3. Publish** components send different types of data from CAD software to a channel and its connected viewers.
| **4. Save** enables you to save .radii files local on your machine or on a channel in the cloud.
| **5. Subscribe** imports data from a viewer back to your local Rhino Grasshopper session.
| **6. Tools** to modify point clouds and meshes 

.. tip:: 
    
    Individual components have options and managers inside them that can be accessed by right clicking on the components center.

.. @gereon Der Absatz hier vor Grasshopper Components passt finde ich nicht richtig rein. vielleicht könnte das bild auch noch auf die index seite und vielleicht bräuchte es nochmal eine kleine überarbeitung mit den publish local und global? to be discussed

Data flow diagram RADii
----------------------------

.. image:: /tutorial/Radii_diagramms/Daten_Diagramme_v2/Artboard14.png
    :alt: Diagram of all ways in which data can be sent, stored and received with RADii

Diagram of all ways in which data can be sent, stored and received with RADii

.. 
    | **Publish** sends data from the CAD software through the cloud to a RADii Viewer.
    | **Subscribe** imports data from a RADii Viewer though the cloud back to the CAD software.
    | `Publish Reference`_ allows for data that was stored in the cloud to be downloaded to viewers without having to directly upload it again.
    | `Save Content`_ can save all publishing content to the cloud or locally as a .RADII file. The viewers can then manually download them from the cloud or import locally.
    | Viewers can save all content they have received into a local .RADII file.  




Grasshopper Components List
----------------------------

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


Tools Components
_____________________

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


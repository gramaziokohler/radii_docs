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

.. @gereon could the above become a small footnote below the image instead of a headline?

.. image:: /tutorial/Radii_diagramms/Daten_Diagramme_v2/Artboard14.png



Grasshopper Components
-----------------------

.. the naming in toctree is case sensitive
.. @gereon: maybe we could takl about menus on rightclick of components here; maybe think about how to clearly structure
.. explanations of the different menu sections
.. @gereon: generally, there seem to be very different ways of using the formatting. i think it would make sense
.. to unify these; for example use the tips only if you show how something is done, use the important or warning (best decide for one of them) if you want to hint to
.. potential problems; maybe there is also some sort of formatting to use for the videos section and maybe this is always at the very bottom??
.. @gereon here you are missing connect, this should come before publish components
.. @gereon the explorer on the right hand side: would make sense to have things structured better there (mit einrückung??)

**Connect Components**

.. @help put the connect link from below here

**Publish Components**

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *connect
    *publish*

**Save Components**

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Save*

**Params Components**

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


.. @gereon tips von menu unten rausnehmen und als eigenen punkt, formatiert in diesem kasten mit tips

**Tools Components**

.. toctree::
    :titlesonly:
    :numbered:
    :glob:
    
    *Tools*
    *10_Tips*


.. Tip::

  **10 general Tips for working with RADii** 

.. @help put link for 10 tips above
.. RevSarah

******************
PublishMaterial
******************

.. image:: ../images/Publish/Publish_Textures.png

.. topic:: Definition
    
  This component is used to connect Rhino Materials that should be published to a channel. It takes all Materials from the Rhino file. Make sure to remove all unused Materials.
  Textures are automatically resized to 1200px to avoid unnecessary large files, try to avoid this step by using smaller textures, this can be changed with right clicking the component for options.



Input
---------

.. table::
  :align: left

  =========== =============================== ===========
  Name        Description                     Type
  =========== =============================== ===========
  Connection  Link with the Connect component Connection
  =========== =============================== ===========


Output
------------

.. table::
  :align: left
    
  =======     ===================================== ==============
  Name        Description                           Type
  =======     ===================================== ==============
  Log         Document changes & Data sent          Text
  Content     Connect to Save component for saving  RADii content
  =======     ===================================== ==============



Right click menu
-----------------

.. table::
  :align: left
    
  =========== =================================  =============
  Resolution  Max size of the texture in pixel   Integer
  =========== =================================  =============


.. @gereon_ the secont point below with the black material is unclear

.. important::

  - RADii only reads Custom Materials properly from Rhino, no Emission, Glass, Paint, Plaster, ...
  - Custom material that display as black in RADii: check if the color space is set to RGB in the texture settings
  
******************
PublishMaterial
******************

.. image:: ../images/Publish/Publish_Textures.png

This component is used to connect Rhino Materials that should be published to a channel. It takes all Materials from the Rhino file. Make sure to remove all unused Materials.
Textures are automatically resized to 1200px to avoid unnecessary large files, try to avoid this step by using smaller textures, this can be changed with right clicking the component for options.

**Input**

=========== =============================== ===========
Name        Description                     Type
=========== =============================== ===========
Connection  Link with the Connect component Connection
=========== =============================== ===========

**Output**

=======     ===================================== ==============
Name        Description                           Type
=======     ===================================== ==============
Log         Documents changes & Data send         Text
Content     Connect to Save component for saving  RADii content
=======     ===================================== ==============

**Menu:**

=========== ========================  =============
Resolution  Max size of the texture   Pixel count
=========== ========================  =============

Note:

  - RADii only reads Custom Materials properly from Rhino, no Emission, Glass, Paint, Plaster, ...
  - in case your Custom Material remains black, try changing the color profile of the image in use to RGB

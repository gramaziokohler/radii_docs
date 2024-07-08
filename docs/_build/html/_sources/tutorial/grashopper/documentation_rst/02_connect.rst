************
Connect
************

.. image:: ../images/Connect/Connect.png
  :align: left
  :scale: 83%

.. image:: ../images/Connect/Connect_local.png
  :align: left


The connect components are the **central components** of the RADii plugin. 
All other components are connected to one of them via the ``Connection`` output.
Only components that are connected will be published, as soon as you switch the Toggle to "True".

Two types of Connect components:
--------------------------------------------

.. topic:: 1. Connect Global

  - connects to a channel that can be accessed globally
  - works with an account from RADii.info


.. topic:: 2. Connect Local
  
  - can be used offline on your device or local network
  - is quicker since there is not need for an upload to the cloud


With it, you can select the channel you want to publish to, and log into your RADii account.

**Input**

.. table::
  :align: left

  ========    ====================================== ================
  Name            Description                            Type 
  ========    ====================================== ================
  Connect        Start the connection to the server     Boolean
  Point to       The Rhino view is sending a pointer    Boolean
  Follow         Everyone follows the Rhino view        Boolean
  ========    ====================================== ================

`Follow video Demo <https://www.youtube.com/watch?v=h-5thZiZg1Q>`_

**Output**

.. table::
  :align: left

  ===========  ================================================== ================
  Name            Description                                     Type
  ===========  ================================================== ================
  Connection   All further components have to be connected here   RADii components
  ===========  ================================================== ================

.. image:: ../images/Connect/Connect.1.png
    :scale: 80 %

**Right click menu:**

.. image:: ../images/Connect/Connect.1.png

.. table::
  :align: left

  =============   ====================================================
  Nickname        Name in the viewer for other users to recognise you
  Username        `RADii.info`_ username
  Password        `RADii.info`_ password
  Load account    Load Radii.info account
  =============   ====================================================



**Note:**  ``If you are part of a group or organization, please use the respective email address.``

.. image:: ../images/Connect/Connect.11.png



About channels, subchannels and subsubsubchannels:
---------------------------------------------------

The way to note a channel addresses in the Viewers `Connect Menu`_ is channelname.subchannel.subsubchannel. and can be endlessly extended in this way. 

In RADii grasshoppers connect_ the same address can be reached by: logging in, choosing "channelname > My Domain" and then under "-subchannel-" 
typing the respective subchannel or subsubchannel as shown in the image below.

.. image:: /tutorial/Quick_Guide//1_LV_Explo_Images/Grashopper/03_Quick_Guide_Publisher_zugeschnitten.png


**Example how to write channels:**

The channel **sun.hs23.g1**

**In the RADii viewer:**

*sun.hs23.g1*

**In RADii Grasshopper:**

select from the available Channels: 

Sun > My Domain

subchannel:*hs23.g1*

 




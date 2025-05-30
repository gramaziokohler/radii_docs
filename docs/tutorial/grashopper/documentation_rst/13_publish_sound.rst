.. RevSarah

***************
Publish Sound
***************

.. image:: ../images/Publish/Publish_sound.png
    :scale: 80 %

.. topic:: Definition
    
  Sound is emitted in the center of a source defined by an inner and outer envelope. Sound decreases over distance unless "stop on exit" or "limit" is set.


Input
---------

.. table::
  :align: left
    
  ================  ======================================  ==============
  Name                Description                             Type
  ================  ======================================  ==============
  Connection          Link with the Connect component         Connection
  Audio URL           The URL of the audio file               Note - Multiline Data
  Outer Envelope      Defining the outer sound reach          Circle
  Inner Envelope      Defining the inner sound reach          Circle
  ================  ======================================  ==============

Output
------------

.. table::
  :align: left

  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Log         Document  changes & data sent           Text
  Content     Connect to Save component for saving    RADii content
  Sequence    Sequence to be saved as content         Radii content
  ==========  ======================================  ==============

Right click menu
-----------------

.. image:: ../images/Publish/Publish_sound_menu.png
    :scale: 80%

.. table::
  :align: left

  ==============  ==========================================
  Name            Description
  ==============  ==========================================
  Play            Play the sound
  Play on enter   Play sound after entering outer envelope
  Stop on exit    Stop sound after exiting outer envelope
  Loop            Loop the sound
  Spatial         Sound spatial in direction of the origin
  Limit           Sound decreases to 0 at the outer envelope
  ==============  ==========================================

.. important::

  - Use only mp3 files the standard one should work more specifically:
    
    - MPEG -1 Audio Layer III with 32 kHz, 44.1 kHz or 48 kHz sample rate
  
  - To keep the publishing size small use mono and lower sample rates


Videos:
---------------

**Publish sound basic usage**

.. youtube:: 4iT8-PehmJE
  :width: 90%
  :align: left

|

**RADii: Sound development**

.. youtube:: 0mPwLp1ye34
  :width: 90%
  :align: left

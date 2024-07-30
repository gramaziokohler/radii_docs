.. RevSarah

***************
Publish Sound
***************

.. image:: ../images/Publish/Publish_sound.png
    :scale: 80 %

.. topic:: Definition
    
  Sound is emitted in the center of a source defined by an inner and outer envelope. Sound decreases over distance unless "stop on exit" or "limit" is set.


**Input**

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

**Output**

.. table::
  :align: left

  ==========  ======================================  ==============
  Name        Description                             Type
  ==========  ======================================  ==============
  Log         Document  changes & data sent           Text
  Content     Connect to Save component for saving    RADii content
  ==========  ======================================  ==============

**Right click menu**

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

Videos:
---------------

- `Publish sound basic usage <https://www.youtube.com/watch?v=4iT8-PehmJE>`_
- `RADii: Sound development <https://www.youtube.com/watch?v=0mPwLp1ye34>`_

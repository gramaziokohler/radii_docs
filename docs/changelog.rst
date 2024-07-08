***************
Changelog
***************

This is a log file of  changes from v.0.39 B2 onwards.

V 0.39 B2
***********


Features:
------------

- Added local connection for direct zero latency connection on LAN.
- Added component toogle for saveable content. If off, content cannot be exported on the viewer side. Off by default.
- Split the control component into control component and scenario component.
- Scenario component has the option to Add/Replace content in the selected scenario. If the content doesn't exist in the scenario, it will be added. If it exists, the scenario content wil be updated witth the attached. If Add/Replacing content with zero elements, it will delete it from the selected scenario

Changes:
-----------


- Animation and view component now accepts lens length instead of field of view.
- new icons and renaming of connection component.

Fixes:
-----------

- Many minor fixes

Hints:
-----------

- When dropping the ConnectLocal component in for the first time, make sure you allow Rhino to communicate on the network you're currently connected to. In my case it's the private network at home

v0.39-beta.1
*************

Features:
------------


- Added Follow, Control and Merge options in publish menu for viewers. Allows control over other viewers from a viewer. Functions are only allowed when the user role has the following user role on the domain (OWNER, SPECTATOR, EDITOR, ADMINISTRATOR).
- Added voice chat - Control access by web interface. Set required role for output and required role for input.
- Added Rhino lens length when using set position in PublishControl
- Added lens length when using follow on connect component and follow in viewers
- Smooth transition with changes to Field Of View in viewers
- Error reporting to server for improved debug


Changes:
-----------

- World orientation has been removed from the control component and is now only set in the Rhino Sun menu under north direction.
- More UI space for parameter manipulation in the viewers.

Fixes:
-----------

- Fixed an issues with geometry that would skip some objects if they were aligned in a large grid.
- Fixed world orientation bug in plugin for negative rotation
- Fixed VR follow rotation


v0.39-beta.0
*************

Features:
------------

- Added integer option to parameters
- Publish parameter from RADii Plugin
- Subscribe/Sync to paramteres in viewers from other viewers and RADii plugins

..
  Note 


  Features:
  ------------

  Changes:
  -----------

  Fixes:
  -----------

  Notes:
  -----------


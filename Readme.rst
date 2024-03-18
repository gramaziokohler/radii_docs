*****************************************************************************************************
Repository for the `Radii Documentation Website <https://gramaziokohler.github.io/radii_docs/>`_
*****************************************************************************************************

More information on Radii can be found at `<Radii.info>`_


It is done in Restructured text (.rst) and can be eddited with any text software or through the browser directly. However the .rst formating has to be resprected throughout.
A live preview is possible in vscode. with the extension Name: 
`reStructuredText <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_
Syntax help in vs can be provided with `reStructuredText Syntax highlighting <https://marketplace.visualstudio.com/items?itemName=trond-snekvik.simple-rst>`_  

The website is compiled with Sphinx, by calling the "make html" command in the \docs directive. Html files are generated at ..\docs\_build\html
At the moment the html build is then pushed  manually to gh-pages and the website published from that branch with githubs internal service. 

A guide on how to get started with `Sphinx <https://www.sphinx-doc.org/en/master/usage/quickstart.html>`_
Quick guide on the formating can be found `here <https://docutils.sourceforge.io/docs/user/rst/quickref.html#contents>`_

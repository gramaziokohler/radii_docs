![alt text](https://radii.info/img/logo.png)

**Documentation of Radii**

This is the documentation of Radii. The program can be found under Radii.info

This documentation is generated with restructured text files (.rst). They are a simple text format that makes it possible to edit them easily and transparent. File formats such as pdf. or Websites(html) are generated from the .rst files. The library that that is used for the generation is called sphinx. 

Local build of a file: After installing sphinx the easiest way to generate an updated html or pdf, is by navigating with the command prompt to the docs folder and typing: "make html" or "make pdf" the later need more dependencies but the following error messages will tell you which to install via pip.

The two files that control the template as well as the general settings are the central **"index.rst"** that give the structure and fuctions as the home page. The **"conf.py"** has all the webpage options, the theme and generally controlls the look of the website. It also holds all links that are used throughout the pages as links.

A web build is atomatically made at every commit to the main branch. The github action for this process can be found at .github/workflows/Build_webpage.yml

Please file any bugs/inconsistencies you might discover under [Issues](https://github.com/Archtica/RADii/issues) - Share ideas and features under [Discussions](https://github.com/Archtica/RADii/discussions)

Welcome to Priority Matrix Python API's documentation!
==========================================

==============
Index Contents
==============

.. toctree::
   :maxdepth: 3

   tutorial
   get_access_token
   code_documentation

Requirements
============

Priority Matrix requires the following modules:

* Python 2.5+
* Slumber
* Demjson


Quick view of PM use
====================
* PM is easy to use to interact with the API:
   test.py::

     import priority_matrix

     pm = PM("https://sync.appfluence.com/api/v1/", "your_access_token")

     print pm.project("project_name").item("item_name").toString()
     pm.project("project_name").item("item_name").name = "New item name"
     print pm.project("project_name").item("item_name").name
     print pm.project("project_name").item("item_name").id

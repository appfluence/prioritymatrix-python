# What is this?

This project is library to facilitate interaction with the Priority Matrix API. 
Priority Matrix is a multiplatform software suite that implements the [prioritization matrix](https://appfluence.com/productivity/prioritization-matrix/) method for project and project management.

Getting Started with the library
====================================

Requirements
============
Start by installing the API request processor library [Slumber](https://slumber.readthedocs.org/en/v0.6.0/):

  `$ pip install slumber`


Then, the encoder and decoder Json library [Demjson](https://pypi.python.org/pypi/demjson) :

 `$ pip install demjson`


Installation
============

There are two ways to install the extension.
Using pip:

  `$ pip install pmatrix`

or download the package, and from the source tree:

  `$ [sudo] python setup.py install`

Authentication and quick use
===============

1. Priority Matrix API uses a the authentication  OAuth 2.0.

   You need an access token to use the library.

   Please, follow the instructions of this tutorial to get the access token.

2. Printing and modifying an item.

   test:

```
     import priority_matrix

     pm = PM("https://sync.appfluence.com/api/v1/", "your_access_token")

     print pm.project("project_name").item("item_name").toString()
     pm.project("project_name").item("item_name").name = "New item name"
     print pm.project("project_name").item("item_name").name
     print pm.project("project_name").item("item_name").id
```

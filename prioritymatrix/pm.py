import getpass
import os
import re
import slumber
import pprint
import json
import requests
import time
from item import Item
from project import Project
from user import User
from datetime import datetime, timedelta


class PM(object):
    """
    This is the main Priority Matrix Class.
    """

    _printerJson = pprint.PrettyPrinter(indent=4)
    _projects = {}
    api = None

    def __init__(self, api_url, access_token):
        """
        Constructor of the Priority Matrix python API

        :param api_url: The URL of the API
        :param access_token: Our Acess token to connect with the API

        :type api_url: string
        :type access_token: string
        """

        session = requests.session()
        session.headers['Authorization'] = ("Bearer " + access_token)

        self.api = slumber.API(api_url, session = session)

        self.getProjects()

    def _get_api(self, api_url, access_token):
        """
        Returns the slumber API conector

        :param api_url: The URL of the API
        :param access_token: Our Acess token to connect with the API

        :return: Slumber api conector
        :rtype: slumber.API
        """

        session = requests.session()
        session.headers['Authorization'] = ("Bearer " + access_token)

        return slumber.API(api_url, session=session)

    def _is_string(self, s):
        return isinstance(s, basestring)


    def _printJson(self, text):
        _printerJson.pprint(text)

    def getItems(self):
        """
        Returns a dicionary with all the items we have

        :return:A item dictionary {key=item_name, object=Item}
        :rtype: dict

        .. note:: At the creation of the PM object, it gets all the projects, and each project contains his items. So, if we want to get an item from a determined project, we dont need to call this function.
        """

        total_count = (self.api.item.get(format=json))["meta"]["total_count"]

        json_items_array = []

        i=0
        while i<total_count:
            json_items_array.append((self.api.item().get(offset=i, limit=1000, format=json))["objects"])
            i += 1000

        json_items = []

        for i in json_items_array:
            for j in i:
                json_items.append(j)

        items_dict = {}

        for i in json_items:
            items_dict[i["name"]] = Item(i, self.api)

        #print items_dict["Hi Saul 123 , modified item"].id
        return items_dict


    def getProjects(self):
        """
        Obtains all the projects and their items.
        Returns the a project dictionary.

        :return: a project dictionary {key=project_name, object=Project}
        :rtype: dict

        .. note:: This function is called in the constructor of this class.
        """
        total_projects = (self.api.project().get(limit=1, format=json))["meta"]["total_count"]

        json_projects_array = []
        #each element of the array is one get API call (if there are more than 1000 projects)

        i=0
        while i<total_projects:
            json_projects_array.append((self.api.project().get(offset=i, limit=1000, format=json))["objects"])
            i += 1000

        json_projects = []
        #array that is going to content all the projects

        for i in json_projects_array:
            for j in i:
                json_projects.append(j)

        projects_dict = {}
        for i in json_projects:
            projects_dict[i["name"]] = Project(i, self.api)

        for p in projects_dict.itervalues():
            array_items = []
            total_project_items = (self.api.project(p.getIdd()).items.get(limit=1, format=json))["meta"]["total_count"]

            j=0
            while j<total_project_items:
                array_items.append ( (self.api.project(p.getIdd()).items.get(limit=1000, offset=j, format=json))["objects"] )
                j += 1000

            for j in array_items:
                for k in j:
                    p.addItem(Item(k, self.api))

        self._projects = projects_dict

        return projects_dict

    def project(self, project_name):
        """
        Returns the project with the specified name

        :param project_name: The name of the project
        :type project_name: string
        :return: The specified project
        :rtype: Project

        .. note:: The project with the specified name must exists
        """

        return self._projects[project_name]

    def getUsers(self):
        """
        TBD
        """
        users = self.api.user.get(limit=1000, format=json)

        return users


    def newItem(self, name):
        """
        TBD
        """
        if _is_string(name):
            return self.api.item.post({"name": name})
        else:
            return "Error, the parameter wasn't a string"



    def getMe(self):
        """
        TBD
        """
        _printerJson.pprint(self.api.me.get())


    def item(self, id):
        """
        Gets the item with the specified ID

        :param id: The item ID
        :type id: int
        :return: Item object
        :rtype: Item
        """
        item_json = self.api.item(id).get(format=json)

        return Item(item_json, self.api)

    def createItem(self, json_code):
        """
        TBD
        """
        myItem_json = (self.api.item.post(json_code, format=json))
        myItem = Item(myItem_json, self.api)

        return myItem

    def getUser(self, id):
        """
        TBD
        """
        return User(self.api.user(id).get(format=json))

    def getComments(id):
        """
        TBD
        """
        return self.api.item(id).comments.get()

    def getCollaborators(self):
        """
        TBD
        """
        collaborators =  self.api.me.collaborators().get()
        n_collaborators = collaborators["meta"]["total_count"]
        # n_collaborators len(collaborators["objects"])
        collaborators_array = []

        for i in collaborators["objects"]:
            collaborators_array.append(User(i))

        return collaborators_array


    def getCollaboratorsNames(self):
        """
        TBD
        """
        collaborators = getCollaborators()
        names = []
        for c in collaborators:
            names.append(c.getName())

        return names

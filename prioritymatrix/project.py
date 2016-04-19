import json
import demjson
from datetime import datetime, timedelta
from item import Item
import slumber
import pprint
import json
import requests


class Project(object):
    """
    This is the Project class.
    """
    account_uri = ""
    boxFolderID = None
    colorFirstQuadrant = {0, 0, 0, 0}
    colorFourthQuadrant = {0, 0, 0, 0}
    colorSecondQuadrant = {0, 0, 0, 0}
    colorThirdQuadrant = {0, 0, 0, 0}
    completed_effort = 0
    creationDate = None
    creator = ""
    creator_username = ""
    editedByDevice = ""
    edited_by_username = ""
    endDate = None
    hash = ""
    idd = None
    is_team_project = True
    name = ""
    notes = ""
    owner = []
    owners_count = 0
    requested_time = None
    resource_uri = ""
    startDate = None
    state = 1
    tags =  [
        {
            "id": 0,
            "name": "",
            "resource_uri": "",
            "slug": ""
        }
    ]
    templateCreationDate = 0
    textFirstQuadrant = ""
    textFourthQuadrant = ""
    textSecondQuadrant = ""
    textThirdQuadrant = ""
    timestamp = None
    total_effort = 0
    version_id = None
    api = None

    items = {}

    def __init__(self, projectJson, api):
        """
        Constructor of Project class:

        :param projectJson: Json string that describes the project
        :type projectJson: Json
        """
        self.__dict__ = json.loads(demjson.encode(projectJson))
        self.api = api


    def item(self, item_name):
        """
        Returns an item given its name.

        :param item_name: Item name
        :type item_name: string
        :return: Item
        :rtype: Item

        .. note:: If there are two items with the same name, only the first is returned.
        """
        return self.items[item_name]

    def addItem(self, item):
        """
        Needs documentation.
        """
        self.items[item.name] = item

    def setItems(self, items):

        self.items = items

    def getAccount_uri(self):
        """
        Needs documentation.
        """
        return self.account_uri

    def getBoxFolderID(self):
        """
        Needs documentation.
        """
        return self.boxFolderID

    def getColorFirstQuadrant(self):
        """
        Needs documentation.
        """
        return self.colorFirstQuadrant

    def getColorFourthQuadrant(self):
        """
        Needs documentation.
        """
        return self.colorFourthQuadrant

    def getColorThirdQuadrant(self):
        """
        Needs documentation.
        """
        return self.colorThirdQuadrant

    def getCompleted_effort(self):
        """
        Needs documentation.
        """
        return self.completed_effort

    def getCreator(self):
        """
        Needs documentation.
        """
        return self.creator

    def getCreator_username(self):
        """
        Needs documentation.
        """
        return self.creator_username

    def getEditedByDevice(self):
        """
        Needs documentation.
        """
        return self.editedByDevice

    def getEdited_by_username(self):
        """
        Needs documentation.
        """
        return self.edited_by_username

    def getEndDate(self):
        """
        Needs documentation.
        """
        return self.endDate

    def getHash(self):
        """
        Needs documentation.
        """
        return self.hash

    def getID(self):
        """
        Needs documentation.
        """
        return self.idd

    def getIdd(self):
        """
        Needs documentation.
        """
        return self.idd

    def getIs_team_project(self):
        """
        Needs documentation.
        """
        return self.is_team_project

    def getName(self):
        """
        Needs documentation.
        """
        return self.name

    def getNotes(self):
        """
        Needs documentation.
        """
        return self.notes

    def getOwner(self):
        """
        Needs documentation.
        """
        return self.owner

    def getOwners_count(self):
        """
        Needs documentation.
        """
        return self.owners_count

    def getRequested_time(self):
        """
        Needs documentation.
        """
        return self.requested_time

    def getResource_uri(self):
        """
        Needs documentation.
        """
        return self.resource_uri

    def getStartDate(self):
        """
        Needs documentation.
        """
        return self.startDate

    def getState(self):
        """
        Needs documentation.
        """
        return self.state

    def getTags(self):
        """
        Needs documentation.
        """
        return self.tags

    def getTemplateCreationDate(self):
        """
        Needs documentation.
        """
        return self.templateCreationDate

    def getTextFirstQuadrant(self):
        """
        Needs documentation.
        """
        return self.textFirstQuadrant

    def getTextFourthQuadrant(self):
        """
        Needs documentation.
        """
        return self.textFourthQuadrant

    def getTextSecondQuadrant(self):
        """
        Needs documentation.
        """
        return self.textSecondQuadrant

    def getTextThirdQuadrant(self):
        """
        Needs documentation.
        """
        return self.textThirdQuadrant

    def getTimestamp(self):
        """
        Needs documentation.
        """
        return self.timestamp

    def getTotal_effort(self):
        """
        Needs documentation.
        """
        return self.total_effort

    def getVersion_id(self):
        """
        Needs documentation.
        """
        return self.version_id

    def setEndDate(self, endDate ):
        """
        Needs documentation.
        """
        self.endDate = endDate

    def setName(self, name):
        """
        Needs documentation.
        """
        self.name = name

    def setNotes(self, notes):
        """
        Needs documentation.
        """
        self.notes = notes

    def setStartDate(self, startDate):
        """
        Needs documentation.
        """
        self.startDate = startDate

    def setState(self, state):
        """
        Needs documentation.
        """
        self.state = state

    def setQuadrantTitle(self, quadrant, title):
        """
        Sets the title of a given quadrant

        :param quadrant: Quadrant number (from 0 to 3)
        :param title: The new quadrant title
        :type quadrant: int
        :type title: string
        """
        if quadrant == 0:
            self.textFirstQuadrant = title
        if quadrant == 1:
                self.textSecondQuadrant = title
        if quadrant == 2:
            self.textThirdQuadrant = title
        if quadrant == 3:
            self.textFourthQuadrant = title

    def setQuadrantColor(self, quadrant, color):
        """
        Sets the color of a given quadrant

        :param quadrant: Quadrant number (from 0 to 3)
        :param color: The new quadrant color (i.e. "{0.360, 0.644, 0.751, 1}")
        :type quadrant: int
        :type color: string

        """
        if quadrant == 0:
            self.colorFirstQuadrant = color
        if quadrant == 1:
            self.colorSecondQuadrant = color
        if quadrant == 2:
            self.colorThirdQuadrant = color
        if quadrant == 3:
            self.colorFourthQuadrant = color

    def toJson(self):
        """
        Returns all the json code of the project

        :return: The item json code
        :rtype: string
        """
        return self.__dict__

    def _datetimeToTimestamp(self, date, epoch=datetime(1970,1,1)):
        td = date - epoch
        # return td.total_seconds()
        return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6

    def _timestampToDatetime(self, tstamp):
        return datetime.fromtimestamp(tstamp)

    def save(self):
        """
        Update the project with the changes made.

        .. note:: If we have changed some value of the project, until we dont call to this function, it will not be saved on the API.
        """

        self.api.project(self.getID()).put(self.getJson())

    def toString(self):
        """
        Returns a string with relevant information about the project.
        """
        s = ""

        s += "Project name: " + self.name
        s += "ID: " + str(self.idd)
        s += "Creation Date: " + str(datetime.fromtimestamp(self.idd))
        s += "Creator: " + self.creator
        s += "Text first quadrant: " + self.textFirstQuadrant
        s += "Text second quadrant: " + self.textSecondQuadrant
        s += "Text third quadrant: " + self.textThirdQuadrant
        s += "Text fourth quadrant: " + self.textFourthQuadrant
        if (self.state == 0):
            s += "State: " + str(self.state)
        elif (self.state == 1):
            s += "State: " + str(self.state) + " (completed)"
        elif (self.state == 2 or self.state == 3):
            s += "State: " + str(self.state) + " (deleted)"
        s += "Color first quadrant: " + self.colorFirstQuadrant
        s += "Color second quadrant: " + self.colorSecondQuadrant
        s += "Color third quadrant: " + self.colorThirdQuadrant
        s += "Color fourth quadrant: " + self.colorFirstQuadrant
        s += "Owners: " + str(self.owner)
        if (self.timestamp != None):
            s += "Current time: " + str(datetime.fromtimestamp(self.timestamp))

        return s

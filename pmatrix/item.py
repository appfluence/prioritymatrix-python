import json
import demjson
from datetime import datetime, timedelta
from icon import Icon
import slumber
import pprint
import json
import requests


class Item(object):
    """
    This is the Item class.
    """

    _props = None
    api = None

    def __init__(self, itemJson, api):
        """
        Constructor of Item class:

        :param itemJson: Json string that describes the item
        :type itemJson: Json
        """
        self._props = json.loads(demjson.encode(itemJson))
        self.api = api

    @property
    def name(self):
        """
        The name of the item.

        :type: string
        """
        return self._props["name"];


    @name.setter
    def name(self , value):
        self._props["name"] = value


    @property
    def id(self):
        """
        The ID of the item (read only).

        :type: int
        """
        return self._props["id"]

    @property
    def idd(self):
        """
        The idd of the item. (read only)

        :type: int
        """
        return self._props["idd"];


    @property
    def index(self):
        """
        The index of the item.

        :rtype: int
        """

        return self._props["index"]


    @index.setter
    def index(self, index):

        if (index):
            self._props["index"] = index

    def isCompleted(self):
        """
        Returns if the item is completed or not.

        :return: True if the item is completed
        :return: False if the item is not completed
        :rtype: boolean
        """
        if (self._props["state"] == 1):
            return True
        else:
            return False


    def isDue(self):
        """
        Returns if the item is due or not.

        :return: True if the due date has passed
        :return: False if the due date has not passed
        :rtype: boolean
        """
        if (self._props["dueDate"] != None):
            dueDate_datetime = self._timestamptoDatetime(self._props["dueDate"])
            present_time = datetime.now()

            if (dueDate_datetime < present_time):
                return True
            else:
                return False
        else:
            return False


    def isDeleted(self):
        """
        Returns if the item is deleted or not.

        :return: True if the item has been deleted
        :return: False if the item has not been deleted
        :rtype: boolean
        """
        if (self._props["state"] == 2 or self._props["state"] == 3):
            return true
        else:
            return False

    @property
    def allDay(self):
        """
        Boolean to determine is the item is active all day.

        :type: boolean
        """
        return self._props["allDay"]

    @allDay.setter
    def setAllDay(self, allday):
        self._props["allDay"] = allday

    @property
    def boxFolderID(self):
        """
        The BoxFolderID value (read only).

        :type: int
        """
        return self._props["boxFolderID"]

    @property
    def childID(self):
        """
        The childID value. (read only).

        :type: int
        """
        return self._props["childID"]


    @property
    def completionPercentage(self):
        """
        The completion percentage value.

        :type: int

        .. warning:: completionPercentage param must be greater than or equal to 0 and less than or equal to 100.
        .. note:: If the completionPercentage is 100, the item will be set as completed.
        """

        return self._props["completionPercentage"]


    @completionPercentage.setter
    def completionPercentage(self, completionPercentage):
        if (completionPercentage):
            if (completionPercentage >= 0 or completionPercentage <= 100):
                self._props["completionPercentage"] = completionPercentage
            if (completionPercentage == 100):
                self._props["state"] = 1


    @property
    def completed_by(self):
        """
        The name of the user who has completed the item. (read only)

        :type: string

        .. note:: The variable will be modified when an user set an item as completed
        .. note:: None in case the item is not completed
        """

        if (self.isCompleted()):
            return self._props["completed_by_username"]
        else:
            return None

    @property
    def completionDate(self):
        """
        The date when the item was completed (read only).


        :type: datetime
        .. note:: None in case the item is not completed
        """
        if (self.isCompleted()):
            return _timestamptoDatetime(self._props["completionDate"])
        else:
            return None

    @property
    def creationDate(self):
        """
        The date when the item was created (read only).

        :type: datetime
        """
        return self._props["creationDate"]

    @property
    def getCreator(self):
        """
        The user name of the item creator.

        :type: string
        """
        return self._props["creator_username"]

    @property
    def delegated_by(self):
        """
        The user name who delegated the item (read only).

        :type: string
        """
        return self._props["delegated_by_username"]

    @property
    def descriptionText(self):
        """
        The item description text.

        :type: string
        """
        return self._props["descriptionText"]

    @descriptionText.setter
    def setDescriptionText(self, descriptionText):
        self._props["descriptionText"] = descriptionText


    @property
    def dueDate(self):
        """
        The due date in case it exists.

        :type: datetime
        """
        if (dueDate != None):
            return self._timestamptoDatetime(self._props["dueDate"])
        else:
            return None


    @dueDate.setter
    def dueDate(self, dueDate):
        self._props["dueDate"] = dueDate


    @property
    def getEdited_by_username(self):
        """
        The last user's name who edited the item (read only).

        :type: string
        """

        return self._props["edited_by_username"]

    @property
    def effort(self):
        """
        The effort value of the item.

        :type: int
        .. warning:: effort param must be greater than or equal to 0 and less than or equal to 10.
        """
        return self._props["effort"]

    @effort.setter
    def setEffort(self, effort):
        if (effort >= 0 or effort <= 10):
            self._props["effort"] = effort


    @property
    def ownerUsername(self):
        """
        The owner username of the item.

        :type: string
        """
        return self._props["owner_username"]

    @ownerUsername.setter
    def ownerUsername(self, owner_username):
        self._props["owner_username"] = owner_username

    def delegate(self, username):
        """
        Delegate the item to the user with the specified username.

        :param owner_username: The new name of the item's owner
        :type owner_username: string
        """
        self._props["owner_username"] = username


    @property
    def getParentID(self):
        """
        The Parent ID of the item (read only).

        :type: int
        """
        return self._props["parentID"]

    @property
    def projectID(self):
        """
        The Project ID where the item is, in case it isn't in the item box

        :type: int
        .. note:: None in case the item is in item box
        .. note:: The ID must belong to a created project
        """
        if (any(self._props["projects"])):
            return (((self._props["projects"])[0].split('/'))[4])


    @projectID.setter
    def projectID(self, project):
        self._props["projects"] = []

        if (self.__is_number(project)):
            self._props["projects"].append("/api/v1/project/" + str(project) + "/")
            return True
        else:
            return False

    @property
    def quadrant(self):
        """
        The Quadrant where the item is.

        :type: int
        .. note:: None in case the item doesn't belong to a project yet
        """

        return self._props["quadrant"]

    @quadrant.setter
    def quadrant(self, quadrant):
        self._props["quadrant"] = quadrant



    @property
    def frequency(self):
        """
        The item's frequency.

        :type: string.

        .. warning:: frequency value must be one the next list: "Never", "Daily", "Weekly", "Biweekly",  "4-weekly", "Monthly", "Quaterly", "Semesterly", "Yearly" or "None"
        """

        if (self._props["frequency"] == ""):
            return "None"

        return self._props["frequency"]


    @frequency.setter
    def frequency(self, frequency):

        possible_values = ["Never", "Daily", "Weekly", "Biweekly",  "4-weekly", "Monthly", "Quaterly", "Semesterly", "Yearly","None"]

        if (frequency in possible_values):
            if (frequency == "None"):
                self._props["frequency"] = ""
            else:
                self._props["frequency"] = frequency


    def toJson(self):
        """
        Returns all the json code of the item

        :return: The item json code
        :rtype: string
        """
        return self._props


    def _datetimeToTimestamp(self, date, epoch=datetime(1970,1,1)):
        td = date - epoch
        # return td.total_seconds()
        return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6

    def _timestamptoDatetime(self, tstamp):
        return datetime.fromtimestamp(tstamp)

    def save(self):
        """
        Update the item with the changes made.

        .. note:: If we have changed some value of the item, until we dont call to this function, it will not be saved on the API.
        """
        self.api.item(self.getID()).put(self.getJson())


    def __is_number(self, s):
        try:
            float(s) # for int, long and float
        except ValueError:
            try:
                complex(s) # for complex
            except ValueError:
                return False
        return True



    def toString(self):
        """
        Returns a string with relevant information about the item.
        """
        s = ""

        s +="Item name: " + self._props["name"] + "\n"
        if (self._props["descriptionText"] != ""):
            s +="Description: " + self._props["descriptionText"]  + "\n"
        s += "Owner: " + self._props["owner_username"] + "\n"
        s +="Delegated by: " + self._props["delegated_by_username"] + "\n"
        s +="ID: " + str(self._props["id"]) + "\n"
        if (self._props["state"] == 0):
            s +="State: " + str(self._props["state"]) + "\n"
        elif (self._props["state"] == 1):
            s +="State: " + str(self._props["state"]) + " (completed)" + "\n"
        elif (self._props["state"] == 2 or self._props["state"] == 3):
            s +="State: " + str(self._props["state"]) + " (deleted)" + "\n"
        if (any(self._props["projects"])):
            s +="Project: " + self.projectID + "\n"
        else:
            s +="Item in Inbox"  + "\n"
        s +="Effort: " + str(self._props["effort"]) + "\n"
        s +="Quadrant: " + str(self._props["quadrant"]) + "\n"
        s +="Completion Percentage: " + str(self._props["completionPercentage"]) + "%" + "\n"
        s +="Icon: " + self._props["icon"] + "\n"
        if (self._props["timestamp"] != None):
            s +="Last modification date: " + str(datetime.fromtimestamp(self._props["timestamp"])) + "\n"

        return s

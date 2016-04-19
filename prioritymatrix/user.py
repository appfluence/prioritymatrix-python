import json
import demjson
from datetime import datetime, timedelta


class User(object):
    account_manager = ""
    date_joined = None
    email = ""
    first_name = ""
    id = None
    last_login = None
    last_name = ""
    paying_single = False
    paying_team = False
    resource_uri = ""
    teammate = False
    user_profile = ""
    username = ""


    def __init__(self, userJson):
        self.__dict__ = json.loads(demjson.encode(userJson))

    def getAccount_manager(self):
        if self.account_manager == "":
            self.update()

        return self.account_manager

    def getDate_joined(self):
        return self.date_joined

    def getEmail(self):
        return self.email

    def getFirst_name(self):
        return self.first_name

    def getID(self):
        return self.id

    def getId(self):
        return self.id

    def getLast_login(self):
        return self.last_login

    def getLast_name(self):
        return self.last_name

    def getPaying_single(self):
        if self.paying_single == "":
            self.update()

        return self.paying_single

    def getPaying_team(self):
        if self.paying_team == "":
            self.update()

        return self.paying_team

    def getResource_uri(self):
        return self.resource_uri

    def getTeammate(self):
        return self.teammate

    def getUser_profile(self):
        return self.user_profile

    def getUsername(self):
        return self.username

    def getName(self):
        return self.username

    def update(self):
        import slumber
        import pprint
        import json
        import requests

        session = requests.session()
        session.headers['Authorization'] = ("Bearer " + "NahSKHWDnxGzVL8Ac21p3etG218mly")

        api =  slumber.API("http://stage.appfluence.com/api/v1/", session=session)

        user_update = api.user(self.getID()).get(format=json)

        self.__init__(user_update)

    def save(self):
        import slumber
        import pprint
        import json
        import requests

        session = requests.session()
        session.headers['Authorization'] = ("Bearer " + "NahSKHWDnxGzVL8Ac21p3etG218mly")

        api =  slumber.API("http://stage.appfluence.com/api/v1/", session=session)

        api.user(self.getID()).put(self.getJson())

    def printUser(self):
        print ("User email: " + self.email)
        if (self.first_name != ""):
            print ("First name: " + self.first_name)
        if (self.last_name != ""):
            print ("Last name: " + self.last_name)
        print ("ID: " + str(self.id))
        print ("Username: " + self.username)
        print ("Resource Uri: " + self.resource_uri)
        print ("User profile: " + self.user_profile)
        print("Date joined: " + str(datetime.fromtimestamp(float(self.date_joined))))
        print("Last login: " + str(datetime.fromtimestamp(float(self.last_login))))
        if (self.teammate):
            print("Is teammate")
        else:
            print("Is not teammate")

import requests
import json

password = "xxxxx"
username = "xxxxx"

session = requests.session()

class currentUser:
    userName = ""
    passWord = ""
    userToken = ""
    cookies = ''
    lockFile = False
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'x-dell-api-version': '7'}

    def printUser(self):
         print('\n')
#        print(self.userName)
#        print(self.passWord)
#        print(self.userToken)
#        print(self.cookies)

    def getCSRFToken(self, userName, userPassword):
        userToken = "token is not valid"
        currentUser.lockFile = False
        try:
            session = requests.session()

            data = {'password': userPassword,
                        'userName': userName}
            session.headers = currentUser.headers
            login_path = 'https://kbox.website.com/ams/shared/api/security/login'
            data = json.dumps(data)
            response = session.post(login_path, data=data, verify=False,)
            userToken = response.headers['x-dell-csrf-token']
            currentUser.cookies = session.cookies


        except:
            print(response.content)
            currentUser.lockFile = True
            print('Can\'t login...')
            pass

        return userToken

    def setUser(self, newusername, newpassword, ):
        self.userName = newusername
        self.passWord = newpassword
        self.userToken = self.getCSRFToken(self, newusername, newpassword)

        getAPIInventory(currentUser)


def getAPIInventory(currentUser):
    if currentUser.lockFile == False:
        currentUrl = "https://kbox.website.com/api/inventory/machines"
        session.cookies = currentUser.cookies
        currentUser.headers['x-dell-csrf-token'] = currentUser.userToken
        session.headers = currentUser.headers
        response = session.get(currentUrl, verify=False,)
        print(response.content)
        return
    else:
        pass

currentUser.setUser(currentUser, username, password)

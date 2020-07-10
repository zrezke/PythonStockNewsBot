import requests
import json
import smtplib, ssl

class News(object):
    def __init__(self, news):
        self.news = news

    def getNews(self):
        linkDict = {}
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/list"

        querystring = {"category":"generalnews","region":"US"}

        headers = {
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
            'x-rapidapi-key': "Enter your key here"  # Your rapidAPI KEY
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        result = json.loads(response.text)
        desiredInfo = result["items"]["result"]

        for item in self.news:
            linkDict[item] = []
            for i in range(len(desiredInfo)):
                if item in desiredInfo[i]["title"]:
                    linkDict[item].append(desiredInfo[i]["link"])

        return linkDict


class Email(object):

    def __init__(self, messageDict, news):
        self.messageDict = messageDict
        self.news = news
        self.message = ""
            

    def makeEmail(self):
        message = """\
        Subject: News update

        """
        for item in self.news:
            message = message + "\n" + item + ":" + "\n"
            for element in self.messageDict[item]:
                message = message + element + "\n"

        self.message = message
        self.sendEmail()

    def sendEmail(self):
        port = 465  # For SSL
        password = "Enter passsword here"  # Sender email password
        
        #NOTE Sender email needs to have "Allow less secure apps" turned ON (https://myaccount.google.com/lesssecureapps)
        senderEmail = "Enter sender email here" # Sender email
        receiverEmail = "Enter receiver email here" # Receiver email
        
        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(senderEmail, password)
            server.sendmail(senderEmail, receiverEmail, self.message)
        return

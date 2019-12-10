import requests
import os


currentpath = os.path.dirname(os.path.abspath(__file__))
currentpath = currentpath.replace("\\", "/")
currentpath = currentpath + "/"


codestxt = open("%scodes.txt"%(currentpath), "r")
codes = codestxt.read()
codes = codes.replace("\n", ",")

print("Checking codes from codes.txt...")

response = requests.get("https://api.nitestats.com/v1/codes/checker?codes=%s"%(codes))

responsecontent = str(response.content)

responsecontent = responsecontent.replace("<br>", "\n")

responsecontent = responsecontent.replace("b", "")

responsecontent = responsecontent.replace("'", "")

print(responsecontent)

input()

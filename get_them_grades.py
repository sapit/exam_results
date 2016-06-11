
#######################################
# everyone <3's shitty python scripts #
#######################################
# pip install requests beautifulsoup4 getpass#
#######################################

##Original Code by Jordan Andrew Duncan
##Adapted by Andrew McCluskey (to implement user input)

import requests
import sys
import json
import getpass
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

def getCreds():
    f = open("config.json", "a+")
    credentials = {}
    try:
        credentials = json.load(f)
    except:
        print(sys.exc_info()[0])
        credentials["user"] = raw_input("Enter your GUID: ")
        credentials["pass"] = getpass.getpass("Enter your password: ")

        json.dump(credentials, f)

    f.close()
    return credentials

def checkResults(user, passw):

    # get page, parse and pull out table of results
    mgPage = requests.get(
        'https://uogstudents.mycampus.gla.ac.uk/psc/campus/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_GRADE.GBL?PORTALPARAM_PTCNAV=HC_SSR_SSENRL_GRADE&PortalActualURL=https%3a%2f%2fuogstudents.mycampus.gla.ac.uk%2fpsc%2fcampus%2fEMPLOYEE%2fHRMS%2fc%2fSA_LEARNER_SERVICES.SSR_SSENRL_GRADE.GBL&PortalContentURL=https%3a%2f%2fuogstudents.mycampus.gla.ac.uk%2fpsc%2fcampus%2fEMPLOYEE%2fHRMS%2fc%2fSA_LEARNER_SERVICES.SSR_SSENRL_GRADE.GBL&PortalContentProvider=HRMS&PortalCRefLabel=View%20My%20Grades&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fuogstudents.mycampus.gla.ac.uk%2fpsp%2fcampus%2f&PortalURI=https%3a%2f%2fuogstudents.mycampus.gla.ac.uk%2fpsc%2fcampus%2f&PortalHostNode=HRMS&NoCrumbs=yes',
        auth=HTTPBasicAuth(user, passw)
    )
    mgParsed = BeautifulSoup(
        mgPage.content,
        'html.parser'
    )
    mgResultsTable = mgParsed.find(id="TERM_CLASSES$scroll$0").find_all('tr')

    exams = []

    # for each table row...
    for i, row in enumerate(mgResultsTable):

        # skip first two rows cause we dont want them
        if row.contents[0].name == 'th' or i < 2:
            continue

        # get column elements in row
        rowEles = row.findAll('td')

        # construct object
        rowObj = {
            'name': rowEles[1].text.strip(),
            'code': rowEles[0].text.strip(),
            'result': '   ' + ('NO RESULT' if rowEles[4].text.strip() == '' else rowEles[4].text.strip())
        }

        # append to list of exam objects
        exams.append(rowObj)

    # sort exams by name
    return sorted(exams, key=lambda examDict: examDict['name'])

def get_results(user,password):

    # # for each exam, print out nicely
    return checkResults(user, password)
    # for exam in checkResults(user, password):
    #     print exam['name'] + ' (' + exam['code'] + ')\n' + exam['result'] + '\n'
# get_results("2144328i","dv@isei1")
# c = getCreds()
# # for each exam, print out nicely
# for exam in checkResults(c["user"], c["pass"]):
#     print exam['name'] + ' (' + exam['code'] + ')\n' + exam['result'] + '\n'
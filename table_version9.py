from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
# initialize an HTTP session
session = HTMLSession()
def get_all_forms(url):
    """Returns all form tags found on a web page's `url` """
    # GET request
    res = session.get(url)
    # for javascript driven website
    # res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")
def get_form_details(form):
    """Returns the HTML details of a form,
    including action, method and list of form controls (inputs, etc)"""
    details = {}
    # get the form action (requested URL)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, DELETE, etc)
    # if not specified, GET is the default in HTML
    method = form.attrs.get("method", "get").lower()
    # get all form inputs
    inputs = []
    for input_tag in form.find_all("input"):
        # get type of input form control
        input_type = input_tag.attrs.get("type", "text")
        # get name attribute
        input_name = input_tag.attrs.get("name")
        # get the default value of that input tag
        input_value =input_tag.attrs.get("value", "")
        # add everything to that list
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details
url = "https://mcsapps.ciena.com/OCS_RC/ModuleManufacturing/TRParam.asp?AID=20606"
# get all form tags
forms = get_all_forms(url)
# iteratte over forms
for i, form in enumerate(forms, start=1):
    form_details = get_form_details(form)
    print("="*50, f"form #{i}", "="*50)
    print(form_details)
# get the first form
first_form = get_all_forms(url)[0]
# extract all form details
form_details = get_form_details(first_form)
# the data body we want to submit
data = {}
for input_tag in form_details["inputs"]:
    if input_tag["type"] == "hidden":
        # if it's hidden, use the default value
        data[input_tag["name"]] = input_tag["value"]
    elif input_tag["type"] != "submit":
        # all others except submit, prompt the user to set it
        value = input(f"Enter the value of the field '{input_tag['name']}' (type: {input_tag['type']}): ")
        data[input_tag["name"]] = value
# join the url with the action (form request URL)
url = urljoin(url, form_details["action"])

if form_details["method"] == "post":
    res = session.post(url, data=data)
elif form_details["method"] == "get":
    res = session.get(url, params=data)
# the below code is only for replacing relative URLs to absolute ones
soup = BeautifulSoup(res.content, "html.parser")
for link in soup.find_all("link"):
    try:
        link.attrs["href"] = urljoin(url, link.attrs["href"])
    except:
        pass
for script in soup.find_all("script"):
    try:
        script.attrs["src"] = urljoin(url, script.attrs["src"])
    except:
        pass
for img in soup.find_all("img"):
    try:
        img.attrs["src"] = urljoin(url, img.attrs["src"])
    except:
        pass
for a in soup.find_all("a"):
    try:
        a.attrs["href"] = urljoin(url, a.attrs["href"])
    except:
        pass

# write the page content to a file
open("page.html", "w").write(str(soup))
import webbrowser
# open the page on the default browser
webbrowser.open("page.html") 
#other operations
url = 'file:///C:/Users/deeptish/page.html'
df = pd.read_html(url)
df=df[1]Subco
df
data = df[[1,3,5,6,7]].copy()
data.columns =['Tested_At', 'Serial No', 'Outcome','Start Time','Stop Time'] 
data 
filter_data = input('select Tested At')
filtered=(data.loc[data['Tested_At'] == filter_data])                
n_of_pass=len(filtered[filtered['Outcome'].str.contains('Passed')])
print("No of passed cases:",n_of_pass)
n_of_fail=len(filtered[filtered['Outcome'].str.contains('Failed')])
print("No of Failed cases:",n_of_fail)
n_of_incomplete=len(filtered[filtered['Outcome'].str.contains('Incomplete')])
print("No of Incomplete cases:",n_of_incomplete)   
#yield report                      
yield_pass= (n_of_pass/(n_of_pass+n_of_fail+n_of_incomplete))*100                     
print("(Yield)percentage of Passed cases out of all tested:", yield_pass,"%")                      
filtered 

##################################################################
#
#	Robobrowser or url3/request approach abandoned due to issues with SSL certification. 
#	PITA, I tell you...
#
##################################################################

# import re
# from robobrowser import RoboBrowser

# browser = RoboBrowser(history=True)
# # browser.open('https://courses.iitm.ac.in/login/index.php')
# browser.open('http://playgo.to/iwtg/en/')

# import requests
# url = "https://courses.iitm.ac.in/login/index.php"
# returnResponse = requests.get(url, verify=False)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://courses.iitm.ac.in/login/index.php")

# ToDo : Add the encryption later.
username = ""
password = ""

inputElement = driver.find_element_by_id("username")
inputElement.send_keys(username)
inputElement = driver.find_element_by_id("password")
inputElement.send_keys(password)

inputElement = driver.find_element_by_id("loginbtn")
inputElement.submit()

link = driver.find_element_by_link_text('My courses')
link.click()


####### Now choose all the courses one-by-one ####### 

# Add your own courses here
courses = ['CS6040', 'EE5176', 'CS6370', 'CS4100', 'CS4110', 'MS3910', 'HS4370']
courses = [i + ':JUL-NOV 2016' for i in courses]

material_counters = [0 for i in range(len(courses))]
forum_counters = [0 for i in range(len(courses))]

i=0
for course in courses:
	link = driver.find_element_by_link_text(course)
	link.click()
	ids = driver.find_elements_by_xpath('//*[@id]')
	for ID in ids:
		print ID.get_attribute('id') 
	material_counters[i] = len(ids)
	
	print course + ' : ' + str(len(ids)) + ' : '
	
	if 
	print course + 'Forum : ' + str(len(ids)) + ' : '
	i+=1
	link = driver.find_element_by_link_text('My courses')
	link.click()


##### For testing purposes #####

# course = 'CS6040:JUL-NOV 2016'
# link = driver.find_element_by_link_text(course)
# link.click()
# ids = driver.find_elements_by_xpath('//*[@id]')
# for ID in ids:
# 	print ID.get_attribute('id') + ' : ' + ID.value

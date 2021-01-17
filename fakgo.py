#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,zipfile,os,random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pyautogui import press, typewrite, hotkey
from selenium.webdriver.support.ui import Select
from faker import Faker

URLFILE = "URL.csv"
adresslistefile = "addresses.csv"
adresslistefileused = "adresslistefileused.csv"
appname = "fakgo_kickz_0.2_Winx64"
klickbutton = False
slepping = 2
sleppingmini = 1


def readurlfrometxt():
	try:
		f = open(URLFILE, "r")
		URL = (f.read())
	except:
		print("Need:", URLFILE)
	return URL

def startdriver(URL):
	try:
		driver = webdriver.Chrome('chromedriver')
		driver.get(URL)
		time.sleep(sleppingmini)
		driver.maximize_window()
		time.sleep(slepping)
	except:
		driver.close()
		print("chromedriver not found or wrong version.")
	return driver

def addresses():
	adressliste = []
	faktive = open(adresslistefile, "r")
	for i in faktive:
		i = i.strip("\n")
		adressliste.append(i)
	faktive.close()
	adresslisteused = []
	fused = open(adresslistefileused, "r")
	for x in fused:
		x = x.strip("\n")
		adresslisteused.append(x)
	fused.close()
	for checkliste in adressliste:
		if checkliste in adresslisteused:
			pass
		else:
			f = open(adresslistefileused, "a")
			f.write(checkliste)
			f.write("\n")
			f.close()
			checkliste = checkliste.split(":")
			return(checkliste)
	return None


def startfakgo(driver, adressliste):
	print(appname, "started.")
	time.sleep(slepping)
	print("Delay: ", slepping," Seconds ...")
	time.sleep(slepping)   
	driver.find_element_by_id('salutationOptions').send_keys((adressliste[0]))
	time.sleep(sleppingmini)
	driver.find_element_by_id('raffleFirstName').send_keys((adressliste[1]))
	time.sleep(sleppingmini)
	driver.find_element_by_id('raffleLastName').send_keys((adressliste[2]))
	time.sleep(sleppingmini)
	driver.find_element_by_id('raffleStreet').send_keys((adressliste[3]))
	time.sleep(sleppingmini)
	driver.find_element_by_id('raffleHouseNumber').send_keys((adressliste[4]))
	time.sleep(sleppingmini)
	driver.find_element_by_id('raffleZip').send_keys((adressliste[5]))
	time.sleep(sleppingmini)
	driver.find_element_by_id('rafflePlace').send_keys((adressliste[6]))
	time.sleep(sleppingmini)
	driver.find_element_by_id('raffleEmail').send_keys((adressliste[7]))
	time.sleep(sleppingmini)
	driver.find_element_by_id('raffleInstagram').send_keys((adressliste[8]))
	time.sleep(sleppingmini)
	driver.find_element_by_id('sizeOptions').send_keys((adressliste[9]))
	time.sleep(slepping)
	driver.find_element_by_id('termsCheck').click()
	time.sleep(sleppingmini)
	if klickbutton == False:
		driver.find_element_by_id('submitRaffleButton').click()
		time.sleep(sleppingmini)

while True:
	os.system("cls")
	print(appname, "created by goanec#3486\n")
	print(adresslistefileused, "addresses used.")
	print(adresslistefile, "For new addresses.")
	print(URLFILE, "File for URLs.")
	print("Delay:", slepping,"seconds.")
	input("\nfakgo_kickz_0.2_Winx64 waiting for press Enter...\n")
	adresslist = addresses()
	if adresslist == None:
			print(adresslistefile, "is empty or used.")
			break
	URL = readurlfrometxt()
	driver = startdriver(URL)
	startfakgo(driver, adresslist)

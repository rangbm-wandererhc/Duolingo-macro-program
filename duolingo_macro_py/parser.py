from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import re			
import os
import random
from googletrans import Translator
translator = Translator(service_urls=['translate.google.com'])


from difflib import SequenceMatcher

def similar(a,b):
	return SequenceMatcher(None, a, b).ratio()

print("""
_________________________________

Duolingo Macro Program 

_________________________________

	""")

username = input("username: ")
password = input("password: ")

print("\n\nWELCOME!")

print("\n_______________________________\n")
print("USER: " + username)
print("\n_______________________________\n")

opts = Options()
opts.add_argument("user-agent=user1")
driver = webdriver.Chrome(options=opts)

def conver(test_str):			#conversion function
		    word = ''
		    skip1c = 0
		    skip2c = 0
		    skip3c = 0
		    skip4c = 0
		    for i in test_str:
		        if i == '[':
		            skip1c += 1
		        elif i == '(':
		            skip2c += 1
		        elif i == '<':
		        	skip3c += 1
		        elif i == ']' and skip1c > 0:
		            skip1c -= 1
		        elif i == ')'and skip2c > 0:
		            skip2c -= 1
		        elif i=='>' and skip3c>0:
		        	skip3c -= 1

		        elif skip1c == 0 and skip2c == 0 and skip3c ==0:
		            word += i
		    return word
def btnclicker():
		time.sleep(0.2)
		page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
		if "No thanks" in page:
			time.sleep(0.2)
			driver.find_element_by_xpath("//*[text()[contains(., 'No thanks')]]").click()
		page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
		if "listen now" in page:
			time.sleep(0.1)
			driver.find_element_by_xpath("//*[text()[contains(., 'listen now')]]").click()
			time.sleep(0.1)
			driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]").click()
		counter = 0
		while counter < 8:
			time.sleep(0.1)
			page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
			if "Continue" in page and "No thanks" not in page :
				time.sleep(0.1)
				driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]").click()
			counter +=1
		time.sleep(0.1)




driver.get('https://duolingo.com')
driver.find_element_by_xpath("//*[text()[contains(., 'I ALREADY HAVE AN ACCOUNT')]]").click()
inputs = driver.find_elements_by_css_selector('input')
inputs[0].send_keys(username)
inputs[1].send_keys(password)
driver.find_element_by_xpath("/html/body/div[2]/div/div/form/div[1]/button").click()

time.sleep(15)
print("logging in...")

lessonlist = driver.find_elements_by_css_selector("._21B3_")
# levelist = driver.find_elements_by_css_selector("._26l3y")

# levelnum = []
# for level in levelist:
# 	levelnum.append(level.get_attribute('innerText'))

# while "" in levelnum:
# 	levelnum.remove('') #removes empty string
# print(levelnum)
print("choose your lessons")
print("please only choose unlocked lesson")
lessoncounter = 0
lessonname = []

while lessoncounter < len(lessonlist):
	lessonname.append(lessonlist[lessoncounter].get_attribute('innerText'))
	print(str(lessoncounter+1)+". "+lessonlist[lessoncounter].get_attribute("innerText"))
	lessoncounter+=1


choices = []

print("input: ")
choices = [int(x) for x in input().split()]

looper = 0

while looper<len(choices):
	point = 0
	point1 = 0
	correanswer = ''
	wrongquestionspa = []
	correctedanswerspa = []
	wrongquestioneng = []
	correctedanswereng = []
	wrongquestioncomp = []
	correctedanswercomp = []
	wrongquestionmark = []
	correctedanswermark = []
	wrongquestionrand = []
	correctanswerrand = []
	num = choices[looper]
	num-=1
	time.sleep(0.5)

	print(lessonname[num])
	# if len(lessonname) == len(levelnum):
	# 	lvl = int(levelnum[num])
	# else:
	# 	lvl=0
	lvl = 0
	lessonurl = lessonname[num]
	if " " in lessonurl:
		lessonurl = lessonurl.replace(" ", "-")
	if lessonurl ==  "Phrases":
		lessonurl = 'Common-Phrases'
	print(lessonurl)
	
	url = 'https://www.duolingo.com/skill/es/'+lessonurl+'/'+str(lvl)
	print(url)
	driver.get(url)
	# lessonlist[num].click()
	# driver.implicitly_wait(3)
	# driver.execute_script("arguments[0].click();", lessonlist[num])
	# startbtn = driver.find_element_by_xpath("//*[text()[contains(., 'START')]]")
	# # startbtn.click()
	# driver.execute_script("arguments[0].click();", startbtn)
	time.sleep(1)

	while True:
		time.sleep(0.5)
		btnclicker()
		page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
		url = driver.current_url
		print(url)
		if url == "https://www.duolingo.com/learn":
			break
		btnclicker()
		btnclicker()
		btnclicker()
		btnclicker()
		page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
		url = driver.current_url
		print(url)
		if url == "https://www.duolingo.com/learn":
			break
		page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
		url = driver.current_url
		print(url)
		if url == "https://www.duolingo.com/learn":
			break
		time.sleep(0.3)
		page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
		if "Here's a tip" in page:
			print("*")
			instruction = "Here's a tip"
		else:			
			instruction = driver.find_element_by_css_selector("._1Zqmf")
			instruction = instruction.get_attribute("innerHTML")
			instruction = conver(instruction)
			print(instruction)
		# extrc = re.findall('"([^"]*)"', instruction)  #extracting string inside the quotation marks
		# print(extrc)
		btnclicker()
		if instruction == "Write this in English":
			btnclicker()
			shownword = driver.find_element_by_css_selector(".asMbz")
			shownword = shownword.get_attribute("innerText")
			print("shownword")
			print(shownword)
			if point == 0:
				page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
				if "Use keyboard" in page:
					driver.find_element_by_xpath("//*[text()[contains(., 'Use keyboard')]]").click()
				point = 1

			txtarea = driver.find_element_by_css_selector('textarea')
			tr_results = translator.translate(shownword, src='es', dest='en')
			translated = tr_results.text
			print("translated: ")
	
			i = 0
			while i<len(wrongquestioneng):
				if shownword == wrongquestioneng[i]:
					translated = correctedanswereng[i]
					break
				i+=1
			print(translated)

			txtarea.send_keys(translated)
			driver.find_element_by_xpath("//*[text()[contains(., 'Check')]]").click()
			time.sleep(0.2)
			detector = driver.find_element_by_css_selector('.KekRP')
			detectorclass = detector.get_attribute('class')
			print(detectorclass)

			if "_2KlCX" in detectorclass:
				print("flagged")
				recor = driver.find_element_by_css_selector('._75iiA')
				wrongquestioneng.append(shownword)
				correctedanswereng.append(recor.get_attribute('innerText'))
				print(correctedanswereng)
				print(wrongquestioneng)
				flag = 1
			driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]").click()

		elif instruction == "Write this in Spanish":
			btnclicker()
			shownword = driver.find_element_by_css_selector(".asMbz")
			shownword = shownword.get_attribute("innerText")

			if point == 0:
				page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
				if "Use keyboard" in page:
					driver.find_element_by_xpath("//*[text()[contains(., 'Use keyboard')]]").click()
				point = 1


			txtarea = driver.find_element_by_css_selector('textarea')
			tr_results = translator.translate(shownword, src='en', dest='es')
			translated = tr_results.text

			print("translated: ")
			print(translated)
			i = 0
			while i<len(wrongquestionspa):
				if shownword == wrongquestionspa[i]:
					translated = correctedanswerspa[i]
					break
				i+=1
			print(translated)
			txtarea.send_keys(translated)
			driver.find_element_by_xpath("//*[text()[contains(., 'Check')]]").click()
			time.sleep(0.2)
			detector = driver.find_element_by_css_selector('.KekRP')
			detectorclass = detector.get_attribute('class')
			print(detectorclass)
			if "_2KlCX" in detectorclass:
				print("flagged")
				recor = driver.find_element_by_css_selector('._75iiA')
				wrongquestionspa.append(shownword)
				correctedanswerspa.append(recor.get_attribute('innerText'))
				print(correctedanswerspa)
				print(wrongquestionspa)
				flag = 1
			driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]").click()
		elif instruction == "Complete the translation":
			if point1 == 0:
				page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
				if "Make harder" in page:
					driver.find_element_by_xpath("//*[text()[contains(., 'Make harder')]]").click()
				point = 1
			btnclicker()
			shownword = driver.find_element_by_css_selector(".asMbz")
			shownword = shownword.get_attribute("innerText")

			if point == 0:
				page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
				if "Use keyboard" in page:
					driver.find_element_by_xpath("//*[text()[contains(., 'Use keyboard')]]").click()
				point = 1


			txtarea = driver.find_element_by_css_selector('textarea')
			tr_results = translator.translate(shownword, src='en', dest='es')
			translated = tr_results.text

			print("translated: ")
			i = 0
			while i<len(wrongquestioncomp):
				if shownword == wrongquestioncomp[i]:
					translated = correctedanswercomp[i]
					break
				i+=1
			print(translated)
			txtarea.send_keys(translated)
			driver.find_element_by_xpath("//*[text()[contains(., 'Check')]]").click()
			time.sleep(0.2)
			detector = driver.find_element_by_css_selector('.KekRP')
			detectorclass = detector.get_attribute('class')
			print(detectorclass)
			if "_2KlCX" in detectorclass:
				print("flagged")
				recor = driver.find_element_by_css_selector('._75iiA')
				wrongquestioncomp.append(shownword)
				correctedanswercomp.append(recor.get_attribute('innerText'))
				print(correctedanswercomp)
				print(wrongquestioncomp)
			driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]").click()
		elif instruction == "Mark the correct meaning":	
			btnclicker()
			question = driver.find_element_by_css_selector(".KRKEd")
			question = question.get_attribute('innerText')
			tr_results = translator.translate(question, src='en', dest='es')
			translated = tr_results.text
			shownwords = driver.find_elements_by_css_selector("._2gaCX")
			choicelist = []
			i = 0
			while i<len(shownwords):
				choicelist.append(shownwords[i].get_attribute("innerText"))
				i+=1
			print(translated)
			print(choicelist)
			ratiolist = []

			i=0
			while i<len(choicelist):
				ratiolist.append(similar(choicelist[i], translated))
				i+=1
			print(ratiolist)
			
			if ratiolist[0]>ratiolist[1] and ratiolist[0]>ratiolist[2]:
				key = 0
			elif ratiolist[1]>ratiolist[2] and ratiolist[1]>ratiolist[0]:
				key = 1
			elif ratiolist[2]>ratiolist[0] and ratiolist[2]>ratiolist[1]:
				key = 2
			else:
				key=1

			i = 0
			while i<len(wrongquestionmark):
				print("correcting...")
				if question == wrongquestionmark[i]:
					print("corrected")
					choicelist[key] = correctedanswermark[i]
					break
				i+=1

			print(key)
			print(choicelist[key])

			clickbuttons = driver.find_elements_by_xpath("//*[text()[contains(., '"+choicelist[key]+"')]]")
			if len(clickbuttons)>1:
				clickbuttons[1].click()
			else:
				clickbuttons[0].click()
			driver.find_element_by_xpath("//*[text()[contains(., 'Check')]]").click()
			detector = driver.find_element_by_css_selector('.KekRP')
			detectorclass = detector.get_attribute('class')
			print(detectorclass)
			if "_2KlCX" in detectorclass:
				print("flagged")
				recor = driver.find_element_by_css_selector('._75iiA')
				wrongquestionmark.append(question)
				correctedanswermark.append(recor.get_attribute('innerText'))
				print(correctedanswermark)
				print(wrongquestionmark)
			time.sleep(0.2)
			driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]").click()
		elif instruction == "Here's a tip":
			tile = driver.find_elements_by_css_selector("._3PEcc")
			rand = random.randint(0,1)
			if rand == 0:
				tile[0].click()
			else:
				tile[1].click()
			driver.find_element_by_xpath("//*[text()[contains(., 'Check')]]").click()
			time.sleep(0.1)
			driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]").click()


		else:
			btnclicker()
			time.sleep(0.2)
			page = driver.find_element_by_css_selector('body').get_attribute("innerHTML")
			if "Write" in page:
				question = driver.find_element_by_css_selector('._1Zqmf').get_attribute('innerText')
				time.sleep(0.1)
				page = driver.find_element_by_css_selector('body').get_attribute("innerHTML")
				if "los" in page:
					print("los random")
					key = "los random"
				elif "el" in page:
					print("el random")
					key = 'el random'
				else:
					key = "random"
				inputtag = driver.find_element_by_css_selector('._1LstS')
				print(inputtag)
				print(question)
				print(key)

				i = 0
				while i<len(wrongquestionrand):
					if question == wrongquestionrand[i]:
						key = correctanswerrand[i]
					i+=1
				inputtag.send_keys(key)
				driver.find_element_by_xpath("//*[text()[contains(., 'Check')]]").click()
				time.sleep(0.5)
				detector = driver.find_element_by_css_selector('.KekRP')
				detectorclass = detector.get_attribute('class')
				print(detectorclass)
				if "_2KlCX" in detectorclass:
					print("flagged")
					recor = driver.find_element_by_css_selector('._75iiA')
					wrongquestionrand.append(question)
					correctanswerrand.append(recor.get_attribute('innerText'))
					print(correctanswerrand)
					print(wrongquestionrand)
				driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]").click()
			elif "Which" in page:
				question = driver.find_element_by_css_selector('._1Zqmf').get_attribute('innerText')
				print(question)
				tr_results = translator.translate(question, src='en', dest='es')
				translated = tr_results.text
				tiles = driver.find_elements_by_css_selector('._1xgIc')
				tiletext = []
				for tile in tiles:
					tiletext.append(tile.get_attribute('innerText'))
				i = 0
				ratiolist = []
				while i<len(tiletext):
					ratiolist.append(similar(tiletext[i], translated))
					i+=1		

				if ratiolist[0]>ratiolist[1] and ratiolist[0]>ratiolist[2]:
					key = 0
				elif ratiolist[1]>ratiolist[2] and ratiolist[1]>ratiolist[0]:
					key = 1
				elif ratiolist[2]>ratiolist[0] and ratiolist[2]>ratiolist[1]:
					key = 2
				else:
					key=1

				i = 0

				while i<len(wrongquestionmark):
					print("correcting...")
					if question == wrongquestionmark[i]:
						print("corrected")
						tiletext[key] = correctedanswermark[i]
						break
					i+=1	

				print(tiletext[key])
				clickbuttons = driver.find_elements_by_xpath("//*[text()[contains(., '"+tiletext[key]+"')]]")
				if len(clickbuttons)>1:
					clickbuttons[1].click()
				else:
					clickbuttons[0].click()

				time.sleep(0.1)
				driver.find_element_by_xpath("//*[text()[contains(., 'Check')]]").click()
				detector = driver.find_element_by_css_selector('.KekRP')
				detectorclass = detector.get_attribute('class')
				print(detectorclass)

				time.sleep(0.2)
				print(detectorclass)
				if "_2KlCX" in detectorclass:
					print("flagged")
					recor = driver.find_element_by_css_selector('._75iiA')
					wrongquestionmark.append(question)
					correctedanswermark.append(recor.get_attribute('innerText'))
					print(correctedanswermark)
					print(wrongquestionmark)
				driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]").click()

			# shownword = driver.find_element_by_css_selector("._1LstS ")
			# shownword = shownword.get_attribute("innerText")

			# while i<len(wrongquestioncomp):
			# 	if shownword == wrongquestioncomp[i]:
			# 		translated = correctedanswercomp[i]
			# 		break
			# 	i+=1
			# print(translated)
			# txtarea.send_keys(translated)
			# driver.find_element_by_xpath("//*[text()[contains(., 'Check')]]").click()
			# if point == 0:
			# 	page = driver.find_element_by_css_selector('body').get_attribute('innerHTML')
			# 	if "Use keyboard" in page:
			# 		driver.find_element_by_xpath("//*[text()[contains(., 'Use keyboard')]]").click()
			# 	point = 1


			# txtarea = driver.find_element_by_css_selector('textarea')
			# tr_results = translator.translate(shownword, src='en', dest='es')
			# translated = tr_results.text

			# print("translated: ")
			# i = 0
			# time.sleep(0.3)
			# detector = driver.find_element_by_css_selector('.KekRP')
			# detectorclass = detector.get_attribute('class')
			# print(detectorclass)
			# if "_2KlCX" in detectorclass:
			# 	print("flagged")
			# 	recor = driver.find_element_by_css_selector('._75iiA')
			# 	wrongquestioncomp.append(shownword)
			# 	correctedanswercomp.append(recor.get_attribute('innerText'))
			# 	print(correctedanswercomp)
			# 	print(wrongquestioncomp)
			# driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]").click()
			# 	shownwords = driver.find_elements_by_css_selector("._1xgIc")
			# 	choicelist = []
			# 	i = 0
			# 	while i<len(shownwords):
			# 		choicelist.append(shownwords[i].get_attribute("innerText"))
			# 		i+=1
			# 	print(choicelist)
			# 	ratiolist = []
			# 	i = 0
			# 	while i<len(choicelist):
			# 		ratiolist.append(similar(choicelist[i], translated))
			# 		i+=1
			# 	print(ratiolist)
				
			# 	i = 0
			# 	if ratiolist[0]>ratiolist[1] and ratiolist[0]>ratiolist[2]:
			# 		key = 0
			# 	elif ratiolist[1]>ratiolist[2] and ratiolist[1]>ratiolist[0]:
			# 		key = 1
			# 	elif ratiolist[2]>ratiolist[0] and ratiolist[2]>ratiolist[1]:
			# 		key = 2

			# 	print(key)
			# 	driver.find_element_by_xpath("//*[text()[contains(., '"+choicelist[key]+"')]]").click()
			# 	driver.find_element_by_xpath("//*[text()[contains(., 'Check')]]").click()
			# 	time.sleep(0.3)
			# 	driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]").click()
			# time.sleep(0.3)	
			# btnclicker()
	looper+=1

print('program ended')


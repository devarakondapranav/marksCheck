import time
from selenium import webdriver
import webbrowser
from selenium.webdriver.firefox.options import Options


'''
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "C:/Users/devar/Pictures/chromedriver_win32"
browser = webdriver.Chrome()
browser.get('http://erp.cbit.org.in')
'''


browser = webdriver.Firefox()
print("Opening browser")
browser.get('http://erp.cbit.org.in')
emailElem = browser.find_element_by_id('txtUserName')
emailElem.send_keys('160116733042')

sendBtn = browser.find_element_by_id('btnNext')
sendBtn.click()
#sendBtn.submit()
time.sleep(2)


passwordElem = browser.find_element_by_id('txtPassword')
passwordElem.send_keys('160116733042')
print("Giving credentials...")
browser.find_element_by_id('btnSubmit').click()
time.sleep(5)

print("Logged in...")
browser.get("http://erp.cbit.org.in/StudentLogin/Student/OverallMarksSemwise.aspx")
time.sleep(8)

count = 0
while(True):
	print("Attempt No: " + str(count) + "Time: " + time.ctime())
	count+=1
	try:
		marks = browser.find_element_by_id("ctl00_cpStud_btn4")
		marks.click()
		print("Marks uploaded...")
		webbrowser.open('C:\\Users\\devar\\Pictures\\iphone_remix.mp3')
	except:
		print("Not yet available...")
		print("refreshing and trying again...")
		time.sleep(52)
		browser.get("http://erp.cbit.org.in/StudentLogin/Student/OverallMarksSemwise.aspx")
		time.sleep(8)






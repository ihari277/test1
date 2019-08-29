import xlutils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\administrator\\Desktop\\chromedriver.exe")


driver.get('http://www.rgbins.co.uk/ProductSpecFullForm.asp?SKUNumber=134261&Email=harii@latlontechnologies.com')
driver.maximize_window()

path = "C:\\Users\\administrator\\Desktop\\prj\\Book1.xlsx"
rows =


for r in range(1, rows+1):
    first  = xlutils.readData(path, "Sheet1", r, 3)
    driver.find_element_by_name("spec5").send_keys(first)
 #   a.send_keys(first)
    #a.send_keys(Keys.TAB)

driver.maximize_window()



#Log ins
#username= driver.find_element_by_name("Email")
#username.click();
#username.clear()
#username.send_keys("harii@latlontechnologies.com")
#submit = driver.find_element_by_name("Submit")
#submit.click()

#xs=driver.find_element_by_name("SKUNumber=134263").click()
#print(xs)

#path = "C:\\Users\\administrator\\Desktop\\prj\\Book1.xlsx"
#rows = xlutils.rowCount(path ,"Sheet1")

#xlutils.writeData(path, "Sheet1", xs, 3, "TC passed")
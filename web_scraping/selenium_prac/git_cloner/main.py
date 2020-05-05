from selenium import webdriver
import subprocess
import time 

driver = webdriver.Chrome("..\chromedriver.exe")
driver.set_page_load_timeout("20")

account_name = 'Chayan199916' # account name of the person
repo_name = 'play-with-python' # repo name to be cloned

search_url = 'https://github.com/' + account_name + '/' + repo_name

driver.get(search_url)
driver.implicitly_wait(10)
driver.maximize_window() 
driver.execute_script("window.scrollTo(0, 250);")
driver.implicitly_wait(5)
driver.find_element_by_xpath('''/html/body/div[4]/div/main/div[2]/div/div[4]/span/get-repo-controller/details/summary''').click()
time.sleep(0.3)
# driver.find_element_by_xpath('''/html/body/div[4]/div/main/div[2]/div/div[4]/span/get-repo-controller/details/div/div/div[1]/div[2]/a[2]''').click() # download the zip file

git_url = driver.find_element_by_xpath('''/html/body/div[4]/div/main/div[2]/div/div[4]/span/get-repo-controller/details/div/div/div[1]/div[1]/div/input''').get_attribute("value") # copy the git url
driver.quit()

git_clone_path = '/demo_git_cloner'
subprocess.call(['git', 'clone', git_url, git_clone_path]) # makes a directory named demo_git_cloner in the root directory and clone the files over there.

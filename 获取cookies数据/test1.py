from selenium import webdriver
browser = webdriver.PhantomJS()
browser.get("http://192.168.1.202:8108/#/Login")
cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
cookiestr = ';'.join(item for item in cookie)
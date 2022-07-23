# Python-Automation-WebDriver

### Table of Contents
- [Info](#Info)
- [Important Websites](#Websites)
- [Tools Needed](#Tools-Needed)
- [Web Driver Install](#Web-Driver-Install)
- [Properties of WebDriver class](#Properties-of-WebDriver-class)
- [Methods of the WebDriver class](#Methods-of-the-WebDriver-class)
- [WebElement class](#WebElement-class)
- [Methods of the WebElement class](#Methods-of-the-WebElement-class)
- [Properties of Select class](#Select-class)
- [Methods of the Select class](#Methods-of-the-Select-class)
- [Alert class](#Alert-class)
- [Methods of the Alert class](#Methods-of-the-Alert-class)
- [Browser Arguments](#Browser-Arguments)

# Info
Have you ever thought some college work can be automated using python? Rather than spending hours of looped days.  We got you, join our workshop, simplify your life and obviously chill out 😎  

This repository is for all Python enthusiasts who have a keen interest in automating the web browser using Python commands. No previous knowledge is required.  This repository will be useful for all the students who are not familiar with python as well as for those students who want to test their technical skills with hand-on-projects to solve complex and real-world problems. In this repository you will be going to learn about the new concept of how to use python commands for web automation, which is useful for testing, scraping data, getting concert tickets, filling in tedious forms using selenium. As a result, you will increase your knowledge and gain expertise in troubleshooting and debugging, python programming and version control. Moreover, this workshop is informative and fun.

# Websites
[Selenium Docs](https://selenium-python.readthedocs.io)


# Tools Needed
Selenium - 
Windows
``` py
pip install selenium
```

Mac
``` py
sudo pip3 install selenium
```

# Web Driver Install
[Web Driver](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)</br>
[Brew link](https://formulae.brew.sh/cask/chromedriver)

# Browser based setup
```
Firefox: firefoxdriver = webdriver.Firefox(executable_path=”Path to Firefox driver”)
Chrome: chromedriver = webdriver.Chrome(executable_path=”Path to Chrome driver”)
Internet Explorer: iedriver = webdriver.IE(executable_path=”­Pat­h To­ IEDriverServer.exe”)
Edge: edgedriver = webdriver.Edge(executable_path=”­Pat­h To­ MicrosoftWebDriver.exe”)
Opera: operadriver = webdriver.Opera(executable_path=”­Pat­h To­ operadriver”)
Safari: SafariDriver now requires manual installation of the extension prior to automation
```

# Properties of WebDriver class
```
current_url -> This gets the URL of the current page displayed in the browser.
current_window_handle -> This gets the handle of the current window.
name -> This gets the name of the underlying browser for this instance.
orientation -> This gets the current orientation of the device.
page_source -> This gets the source of the current page.
title -> This gets the title of the current page.
window_handles -> This gets the handles of all windows within the current session.

Example: driver.current_url
```


# Methods of the WebDriver class
```
back() -> This goes one step backward in the browser history in the current session.
close() -> This closes the current browser window.
forward() -> This goes one step forward in the browser history in the current session.
get(url) -> This navigates and loads a web page in the current browser session.
maximize_windows() -> This maximizes the current browser window.
quit() -> THis quits the driver and closes all the associated windows.
refresh() -> This refreshes the current page displayed in the browser.
switch_to.active_element() -> This returns the element with focus or the body if nothing else has focus.
switch.to_alert() -> This switches the focus to an alret on the page.
switch_to.default_content() -> This switches the focus to the default frame.
switch_to.frame(frame_reference) -> This switches the focus to the specified frame, bu index, name, or web-element. This method also works on IFRAMES.
switch_to.windows(window_name) -> This swtiches focus to the specifies window.
implicitly_wait(time_to_wait) -> This sets a sticky timeout to implicitly wait for an element to be found, or a command to complete. This method only needs to be called one time per session. To set the timeout for calls to execute_async_script, see set_script_timeout.
set_page_load_timeout(time_to_wait) -> This sets the amount of time to wait for a page load to complete.
set_script_timeout(time_to_wait) -> This sets the amount of time that the script should wait during an execute_async_script call before throwing an error.

Example: driver.set_script_timeout(30)
```


# WebElement class
```
Properties of the WebElement class
size -> This gets the size of the element.
tag_name -> This gets this element's HTML tag name.
text -> This gets the text of the element.
```


# Methods of the WebElement class
```
clear() -> This cleaars the content of the textbox or text area element.
click() -> This clicks the element.
get_attribute(name) -> This gets the attribute value from the element.
is_displayed() ->This chcecks whether the element is visible to the user.
is_enabled() -> This checks whether the element is enabled.
is_selected() -> This checks whether the element is selected. This method is used to check the selection of a radio button or checkbox.
send_keys(*value) -> This simulated typing into the element.
submit() -> This submits a form. If you call this method on the element, it will submit the parent form.
value_of_css_property(property_name) -> This gets the value of a CSS property.
```

# Select class
```
Properties of the Select class
all_selected_options -> This gets a list of all the selected options beloging to the dropdown or list.
first_selected_option -> This gets the first selected/currently selected option from the dropdown or list.
options -> This gets a list of all options from the dropdown or list.
```

# Methods of the Select class
```
deselect_all() -> This clears all the selected entries from a multiselect dropdown or list.
deselect_by_index(index) -> This deselects the option at the given index from the dropdown or list.
deselect_bu_value(value) -> This deselects all options that have a value matching the argument from the dropdown or list.
deselect_by_visible_text(text) -> This deselects all the options that display text matching the argument from the dropdown or list.
select_by_index(index) -> This selects an option at the given index from the dropdown or list.
select_by_value(value) -> This selects all the options that have a value matching the argument from the dropdown or list.
select_by_visible_text(text) -> This selects all the options that display the text matching the argument from the dropdown or list.
```

# Alert class
Properties of the Alert class
```
text -> This gets text from the alert window
```
# Methods of the Alert class
```
accept() -> This will accept the JavaScript alert box that is click on the OK button.
dismiss() -> This will dismiss the JavaScript alert box that is click on the Cancel button.
send_keys(*value) -> This simulates typing into the element.
```
# Browser Arguments
```
– headless
To open browser in headless mode. Works in both Chrome and Firefox browser
–start-maximized
To start browser maximized to screen. Requires only for Chrome browser. Firefox by default starts maximized
–incognito
To open private chrome browser
–disable-notifications
To disable notifications, works Only in Chrome browser
http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
```

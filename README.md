# lingoda-task-2

<p>How to run:</p>
<h5>Linux</h5>
<ul>Python and pip are already installed on Linux </ul>
<ul>Download and install <a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Java (JRE)</a></ul>
<ul>Install selenium using pip</ul>

```bash
$ pip install selenium
```

<ul>Download <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads">ChromeDriver</a> archive and unpack it to any directory. In my case in /opt/chromedriver</ul>
<ul>Download <a href="https://www.seleniumhq.org/download/">Selenium server</a> in any directory. In my case in /opt/SeleniumServer</ul>

<ul>Start chrome driver</ul>

```bash
denis@denis-PC:~$ java -Dwebdriver.chrome.driver=/opt/chromedriver/chromedriver -jar /opt/SeleniumServer/selenium-server-standalone-3.9.1.jar
```

<ul>Download the project from git, put files in one directory and start test</ul>

```bash
denis@denis-PC:~/Documents/PythonProjects/lingoda-task-2$ python runner.py
```

```bash
denis@denis-PC:~/Documents/PythonProjects/lingoda-task-2$ ls -l
total 16
-rw-rw-r-- 1 denis denis 2428 мар 17 20:16 README.md
-rw-rw-r-- 1 denis denis  214 мар 17 18:39 runner.py
-rw-rw-r-- 1 denis denis 3929 мар 17 19:21 search.py
-rw-rw-r-- 1 denis denis 3746 мар 17 19:21 search.pyc
```

<h5>Windows</h5>
<ul>Download and install <a href="http://www.python.org/download">Python 2.7</a></ul>
<ul>Download and install <a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Java (JRE)</a></ul>
<ul>Install selenium using pip</ul>

```bash
C:\Python27\Scripts\pip.exe install selenium
```

<ul>Download <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads">ChromeDriver</a> archive and unpack it to any directory.</ul>
<ul>Download <a href="https://www.seleniumhq.org/download/">Selenium server</a>.</ul>

<ul>Start chrome driver</ul>

```bash
C:\java -Dwebdriver.chrome.driver=chromedriver.exe -jar selenium-server-standalone-3.9.1.jar
```

<ul>Download the project from git, put files in one directory and start test</ul>

```bash
C:\Python27\python.exe C:\lingoda-task-2\runner.py
```

<h4>Test results</h4>
<h5>Test passed</h5>

```bash
denis@denis-PC:~/Documents/PythonProjects/lingoda-task-2$ python runner.py 
test_search_in_main_page (search.SearchItem) ... 
Going to https://www.amazon.de
Search for "Batman comics"
Check that results number above 0
Check that title contains "Batman" word
Check that price is above 0
Check that price has EUR postfix
Check that item has rating
Open 1st item page
Check that title and price are equal to the ones in result search
ok
----------------------------------------------------------------------
Ran 1 test in 24.936s
OK
```

<h5>Failed test. We tried to find "Neznaika na Lune"</h5>

```bash
denis@denis-PC:~/Documents/PythonProjects/lingoda-task-2$ python runner.py 
test_search_in_main_page (search.SearchItem) ... 
Going to https://www.amazon.de
Search for "Neznaika na Lune"
Check that results number above 0
Check that title contains "Batman" word
FAIL
======================================================================
FAIL: test_search_in_main_page (search.SearchItem)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/denis/Documents/PythonProjects/lingoda-task-2/search.py", line 45, in test_search_in_main_page
    self.assertIn("Batman", str(title_text))
AssertionError: 'Batman' not found in 'Neznaika na Lune. (in Russian)'
----------------------------------------------------------------------
Ran 1 test in 16.775s
FAILED (failures=1)
```

<h5>Failed test. We tried to find some trash on Amazon</h5>

```bash
denis@denis-PC:~/Documents/PythonProjects/lingoda-task-2$ python runner.py 
test_search_in_main_page (search.SearchItem) ... 
Going to https://www.amazon.de
Search for "try to find some trash results on Amazon"
Check that results number above 0
ERROR
======================================================================
ERROR: test_search_in_main_page (search.SearchItem)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/denis/Documents/PythonProjects/lingoda-task-2/search.py", line 35, in test_search_in_main_page
    self.assertTrue(driver.find_element_by_xpath("//ul[@id='s-results-list-atf']//li[@id='result_0']"))
  File "/home/denis/.local/lib/python2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 385, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "/home/denis/.local/lib/python2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 955, in find_element
    'value': value})['value']
  File "/home/denis/.local/lib/python2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "/home/denis/.local/lib/python2.7/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//ul[@id='s-results-list-atf']//li[@id='result_0']"}
  (Session info: chrome=64.0.3282.186)
  (Driver info: chromedriver=2.35.528139 (47ead77cb35ad2a9a83248b292151462a66cd881),platform=Linux 4.10.0-28-generic x86_64)
----------------------------------------------------------------------
Ran 1 test in 19.512s
FAILED (errors=1)
```

<h5>Failed test. We tried to find Batman comics without rating</h5>

```bash
denis@denis-PC:~/Documents/PythonProjects/lingoda-task-2$ python runner.py 
test_search_in_main_page (search.SearchItem) ... 
Going to https://www.amazon.de
Search for "Batman: Hush (Neuausgabe): Bd. 1 (von 2)"
Check that results number above 0
Check that title contains "Batman" word
Check that price is above 0
Check that price has EUR postfix
Check that item has rating
ERROR
======================================================================
ERROR: test_search_in_main_page (search.SearchItem)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/denis/Documents/PythonProjects/lingoda-task-2/search.py", line 65, in test_search_in_main_page
    self.assertTrue(driver.find_element_by_xpath("//ul[@id='s-results-list-atf']//li[@id='result_0']//span["
  File "/home/denis/.local/lib/python2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 385, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "/home/denis/.local/lib/python2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 955, in find_element
    'value': value})['value']
  File "/home/denis/.local/lib/python2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "/home/denis/.local/lib/python2.7/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//ul[@id='s-results-list-atf']//li[@id='result_0']//span[@class='a-declarative']//span[@class='a-icon-alt']"}
  (Session info: chrome=64.0.3282.186)
  (Driver info: chromedriver=2.35.528139 (47ead77cb35ad2a9a83248b292151462a66cd881),platform=Linux 4.10.0-28-generic x86_64)
----------------------------------------------------------------------
Ran 1 test in 24.056s
FAILED (errors=1)
```
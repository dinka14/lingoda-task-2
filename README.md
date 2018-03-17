# lingoda-task-2

<p>How to run:</p>
<b>Linux</b>
<ul>Python and pip are already installed on Linux </ul>
<ul>Download and install <a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Java (JRE)</a></ul>
<ul>Install selenium</ul>

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

<h5> Test passed: </h5>

```bash
denis@denis-PC:~/Documents/PythonProjects/lingoda-task-2$ python runner.py
test_search_in_main_page (search.SearchItem) ...
Going to https://www.amazon.de
Search for Batman comics
Check that results number above 0
Check that title contains "Batman" word
Check that price is above 0
Check that price has EUR postfix
Check that item has rating
Open 1st item page
Check that title and price are equal to the ones in result search
ok
----------------------------------------------------------------------
Ran 1 test in 33.774s
OK
```

<h5>Failed test (We tried to find "neznaika na lune"):</h5>

```bash
denis@denis-PC:~/Documents/PythonProjects/lingoda-task-2$ python runner.py
test_search_in_main_page (search.SearchItem) ...
Going to https://www.amazon.de
Search for Batman comics
Check that results number above 0
Check that title contains "Batman" word
FAIL
======================================================================
FAIL: test_search_in_main_page (search.SearchItem)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/denis/Documents/PythonProjects/lingoda-task-2/search.py", line 44, in test_search_in_main_page
    self.assertIn("Batman", str(title_text))
AssertionError: 'Batman' not found in 'Neznaika na Lune. (in Russian)'
----------------------------------------------------------------------
Ran 1 test in 23.058s
FAILED (failures=1)
```

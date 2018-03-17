# lingoda-task-2

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
```

<h5>Failed test (We try to find "neznaika na lune"):</h5>
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

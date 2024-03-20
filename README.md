# Python API automation
Hybrid custom framework to test REST API's


### Tech stack 
1. Python 3.12.2
2. Request - HTTP Requests
3. Pytest - Testing framework
4. Reporting - Allure & HTML
5. Test data - CSV, excel , json
6. Parallel execution - X distribute




### How to install packages
'''
pip install requests pytest pytest-html faker allure-pytest jsonschema
'''

### Tp freeze your package version
''' pip freeze > requirements.txt

### To install the freeze version 
''' pip install -r requirements.txt '''

### How to run test cases parallelly
''' pip install pytest-xdist --> Need to install this to run all testcases at once'''

'''pytest -n auto parallel/test_parallel.py ---> to run test cases'''

### to work with Excel
--- pip install openpyxl ---

### to work with json schema
--- pip install jsonschema ---



# aqa-academy-python-2024

#coding rules
## Excluded folders
1. .venv folder.
See link for venv creation https://docs.python.org/3/library/venv.html
2. reports
In order to avoid conflicts during git push

## Dep updates
1. Major ibs version needs to be revisited once per month

# How to
1. Setup your env
1.1 create venv into .venv folder
1.2 Install deps from requirements.txt file

2. Before commit
1. run black tool. LINK_ADDED
2. run flake8 tool. LINK_ADDED
3. run isort tool. LINK_ADDED

3. Run the tests
1. Execute `pytest . -s -v` command staying in the root of the framework
2. To form a report execute `pytest . -s -v --html=reports/report.html --self-contained-html` command

# Structure of framework
1. tests - folder for tests
2. reports - folder to store local reports
3. src/applications - folder for system under tests abstractions
4. src/config - folder for configuration of framework
5. src/helpers - folder for single-use functions, etc

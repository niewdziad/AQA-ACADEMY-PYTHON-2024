def test_positive_login():
""" Summary: Test negative login attemp
Steps:
1. Navigate to login page
2. Enter wrong creds
3. Click login/signin button

Expected result
Error saying ERROR MESSAGE appeared
"""

#1. Navigate to login page
chromeBrowser.open()
chromeBrowser.github_login_page.negative_to()

#2. Enter wrong creds
user_name_fld = gitub_login_page.find_username_fld()
user_name_fld.enter_text("wrongusrname")

password_fld = github_login_page.find_password_fld()
password_fld.enter_text("wrongpswd")

#3. Click login/signin button
signin_btn = github_login_page.find_signin_btn()
signin_btn.click()

# Expected result
error_message = github_login_page.find_error_message()
assert error_message.text() == "ERROR MESSAGE"

# wyrażenie do sprawdzania poprawności działania kodu:
#assert operation
#if operation is not True:
#    raise Exception

# CleanUP
chromeBrowser.close()

# test update
def test_positive_login_updated(GitHubUI):
""" Summary: Test negative login attemp
Steps:
1. Navigate to login page
2. Enter wrong creds
3. Click login/signin button

Expected result
Error saying ERROR MESSAGE appeared
"""

#1. Navigate to login page
GitHubUI.open()
GitHubUI.login_page.negative_to()

#2. Enter wrong creds
GitHubUI.try_login(username='wrongusername', password='wrongpswd')

# Expected result
assert GitHubUI.login_page.check_wrong_creds_message()

# CleanUP
GitHubUI.close()
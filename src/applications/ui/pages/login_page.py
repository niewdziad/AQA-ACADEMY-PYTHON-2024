class LoginPage:
    #URL of the page
    URL = "https://github.com/login"
    # Elements of the page (pobieram ze strony z pomocą devtools)
    LOGIN_FLD = '//*[@id="login_field"]'
    PASSWORD_FLD = '//*[@id="password"]'
    SIGNIN_BTN = '//*[@id="login"]/div[4]/from/div/input[13]'

    #user methods
    def try_login(username: str, password: str):
        pass

    # check functions
    def check_wrong_creds_message(self):
        # find error message
        # check if message is equal to "ERROR MESSAGE" text
        return False

    def check_documentation_link(self):
        pass
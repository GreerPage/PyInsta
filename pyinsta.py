from selenium import webdriver
from time import sleep

class Instagram:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.password = password
        self.username = username
    
    def loadAccount(self, username):
        self.driver.get('https://instagram.com/{}/'.format(username))
        print("Reached {}'s account".format(username))

    def login(self):
        self.driver.get('https://instagram.com')
        sleep(3)
        logInLink = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        logInLink.click()
        print('Redirected to Log in page')
        sleep(3)
        enterUsername = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        enterPassword = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        enterUsername.send_keys(self.username)
        enterPassword.send_keys(self.password)
        sleep(1)
        logInButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
        logInButton.click()
        sleep(3)
        notNowButton = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        notNowButton.click()
        print('logged in successfully as {}'.format(self.username))
        sleep(1)

    def follow(self, username):
        self.loadAccount(username)
        sleep(2)
        followButtons = self.driver.find_elements_by_css_selector('button')
        if followButtons[0].text in ['Following', 'Follow', 'Follow Back', 'Requested']:
            if followButtons[0].text in ['Requested', 'Following']:
                print('you already follow {}'.format(username))
            else:
                followButtons[0].click()
                print('followed {}'.format(username))
        else:
            if followButtons[1].text in ['Requested', 'Following']:
                print('you already follow {}'.format(username))
            else:    
                followButtons[1].click()
                print('followed {}'.format(username))

    def unfollow(self, username):
        self.loadAccount(username)
        sleep(2)
        followButtons = self.driver.find_elements_by_css_selector('button')
        if followButtons[0].text in ['Following', 'Follow', 'Follow Back', 'Requested']:
            if followButtons[0].text in ['Requested', 'Following']:
                followButtons[0].click()
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
                print('unfollowed {}'.format(username))
            else:    
                print('you do not follow {}'.format(username))
        else:
            if followButtons[1].text in ['Requested', 'Following']:
                followButtons[1].click()
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
                print('unfollowed {}'.format(username))
            else:    
                print('you do not follow {}'.format(username))
    
if __name__=='__main__':
    bot = Instagram('your Insta Username', 'your Insta Password')
    bot.login()
    
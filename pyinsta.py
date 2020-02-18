from selenium import webdriver
from time import sleep

class Instagram:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome('C:/Users/Greer/Documents/chromedriver_win32/chromedriver')
        self.password = password
        self.username = username
    
    def loadAccount(self, username):
        self.driver.get('https://instagram.com/{}/'.format(username))
        return "Reached {}'s account".format(username)

    def login(self):
        self.driver.get('https://instagram.com')
        sleep(3)
        logInLink = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        logInLink.click()
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
        return 'logged in successfully as {}'.format(self.username)
        sleep(1)

    def follow(self, username):
        self.loadAccount(username)
        sleep(2)
        followButtons = self.driver.find_elements_by_css_selector('button')
        if followButtons[0].text in ['Following', 'Follow', 'Follow Back', 'Requested']:
            if followButtons[0].text in ['Requested', 'Following']:
               return 'you already follow {}'.format(username)
            else:
                followButtons[0].click()
                return 'followed {}'.format(username)
        else:
            if followButtons[1].text in ['Requested', 'Following']:
                return 'you already follow {}'.format(username)
            else:    
                followButtons[1].click()
                return 'followed {}'.format(username)

    def unfollow(self, username):
        self.loadAccount(username)
        sleep(2)
        followButtons = self.driver.find_elements_by_css_selector('button')
        if followButtons[0].text in ['Following', 'Follow', 'Follow Back', 'Requested']:
            if followButtons[0].text in ['Requested', 'Following']:
                followButtons[0].click()
                sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
                return 'unfollowed {}'.format(username)
            else:    
                return 'you do not follow {}'.format(username)
        else:
            if followButtons[1].text in ['Requested', 'Following']:
                followButtons[1].click()
                sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
                return 'unfollowed {}'.format(username)
            else:    
                return 'you do not follow {}'.format(username)
        
    def viewPost(self, username, postnumber):
        self.loadAccount(username)
        sleep(3)
        post = self.driver.find_elements_by_xpath('//*[@class="_9AhH0"]')
        post = list(reversed(post))
        post = post[postnumber - 1]
        post.click()
        return "opened {}'s post".format(username)
    
    def likePost(self, username, postnum):
        self.viewPost(username, postnum) 
        sleep(4)  
        likeButton = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
        likeButton.click()
        return "liked {}'s post".format(username)
        sleep(1)

    def getNumberOfPosts(self, username):
        self.loadAccount(username)
        sleep(3)
        post = self.driver.find_elements_by_xpath('//*[@class="_9AhH0"]')
        return len(post)

if __name__=='__main__':
    bot = Instagram(input('your username '), input('your password '))
    
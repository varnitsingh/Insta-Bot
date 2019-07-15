from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class Instagram :

    def __init__(self , username , password) :
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()


    def Login(self) :
        bot = self.bot
        bot.get(" https://www.instagram.com/ ")

        time.sleep(7)

        element1 = bot.find_element_by_link_text("Log in")
        element1.click()

        time.sleep(4)

        user = bot.find_element_by_name("username")
        pass_user = bot.find_element_by_name("password")

        user.clear()
        pass_user.clear()


        user.send_keys(self.username)
        pass_user.send_keys(self.password)
        pass_user.send_keys(Keys.RETURN)

        time.sleep(6)


    def find_posts(self , hashtag) :
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        time.sleep(5)

        pic_hrefs = []
        for i in range(1, 3):

            
            #bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #time.sleep(2)
            # get tags
            hrefs_in_view = bot.find_elements_by_tag_name('a')
            # finding relevant hrefs
            hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                             if '.com/p/' in elem.get_attribute('href')]
            # building list of unique photos
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            print("Check: pic href length " + str(len(pic_hrefs)))
            for pic_href in pic_hrefs :

                bot.get(pic_href)
                time.sleep(random.randint(2 , 4))
                bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                like_button = lambda: bot.find_element_by_xpath('//span[@aria-label="Like"]')
                like_button().click()
                print("Liked")
                
                time.sleep(random.randint(3 , 6))  
            
    
    

hashtags = ['basketball', 'football', 'writers', 'photography', 'nofilter',
                'newyork', 'art', 'alumni', 'lion', 'best', 'fun', 'happy',
                'art', 'funny', 'me', 'followme', 'follow', 'boring', 'cinema',
                'love', 'instagood', 'insta', 'followme', 'fashion', 'sun', 'holy',
                'street', 'canon', 'meme', 'funny', 'pretty', 'vintage', 'fierce']


hashtag = random.choice(hashtags)


    
ri = Instagram('Your username' , 'Your password')
ri.Login()
ri.find_posts(hashtag)
    


    

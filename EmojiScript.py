# -*- coding: utf-8 -*-

import glob as glob
import os 
from selenium import webdriver



# this method cheaks if slack throws the the enoji name exists error, it recusivly calls itself,  
# if present it will add an incremented count depending how many times called to the end of the
# emoji name 
# for example:
#       somegif 
#           EXISTS
#       somegif1
#           EXSIST
#       somegif2
#           EXISTS
#           ect...
#       somegif34
#           return

def error_test(file_path, emoji_name, count):
    
    
    #this tests for the error message you get when you have a redundant name
    element = driver.find_elements_by_class_name("alert_error");
    
    #if the error messege exists it will execute the file upload process again
    if element:
        count = count + 1
        
        #grabs the element feilds, they go stale when entering a new method
        name_feild = driver.find_element_by_name('name')
        file_feild = driver.find_element_by_name('img')
        
        #clears the emoji name feild
        driver.find_element_by_name('name').clear()
        
        
        #sends the file path and the emojiname with the increment
        name_feild.send_keys(emoji_name + (str(count)))
        file_feild.send_keys(file_path)
        file_feild.submit()
        
        #wait one second
        driver.implicitly_wait(1)
        #retest
        error_test(file_path, emoji_name, count)
    else:
        return

        
def file_upload(filepath,extention):
    
    
   # using glob and os it will find the gifs/png/jpgs in the pathways specified in the variables 
   # passed in from the assisgments in the main method
   
    for filename in glob.glob(os.path.join(filepath, extention)):
        
   # IMPORTANT the string formating [43:-4] is a substring expression that will pull the file name
   # and assign it to the emjois name for slack, the [43:-4] is for my orginal path 
   # you will need to find it for your specific path
   # for example: 
   # filename = C:\Users\someuser\Desktop\gifs\somegif.gif 
   # filename[31:-3] will assign the name "somegif" as the name for the emoji
   # emoji_name = str(filename[31:-4])
        
        emoji_name = str(filename[33:-4])
        file_path = str(filename)
   
        name_feild = driver.find_element_by_name('name')
        name_feild.send_keys(emoji_name)
   
   # the file submission takes whole filename variable
        file_feild = driver.find_element_by_name('img')
        file_feild.send_keys(file_path)
   
   # submit
        file_feild.submit()
   
   # wait for page to refresh
        driver.implicitly_wait(1)
   
    
    # in the event of a rredundant name, slack will kick you an error, this will test for that error
        error_test(file_path, emoji_name, 0)
        
    

# if you have all your files in the same folder just fill in the same path way for each
# WINDOWS USERS slashes need to be / not \ 
gif = 'Path to gifs'
jpg = 'Path to jpg'
png = 'Path to pngs'

# fill in your username and password
username_keys = 'your_email@emial.com' 
password_keys = 'P@$$W0rd'

# if you google the selenum chrome driver its pretty easy to find
chromepath = 'C:/Users/username/Downloads/chromedriver_win32/chromedriver'


# start the chrome driver
# important that if you execute this script more than once youll need to close
# the chrome driver manually its easy find in task manager
# otherwise after a certian number of driver instatances it will fail to run
driver = webdriver.Chrome(chromepath)

# go to this page
driver.get('https://yourchannel.slack.com/customize/emoji')

# find both the email and password fields, dont change
email = driver.find_element_by_name('email')
password = driver.find_element_by_name('password')

# send your email and password to the fields and submit
email.send_keys(username_keys)
password.send_keys(password_keys)
password.submit()

# wait 5 seconds
driver.implicitly_wait(5)


# cals the function above, does all the work
file_upload(gif, '*.gif')
file_upload(jpg, '*.jpg')
file_upload(png, '*.png')

   

    
    


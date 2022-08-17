from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager 
print('''                                                                           
            )           )                             )                  )  
 (  (    ( /(     )  ( /(        )                 ( /(          )    ( /(  
 )\))(   )\()) ( /(  )\())(   ( /(  `  )   `  )    )\())  (     (     )\()) 
((_)()\ ((_)\  )(_))(_))/ )\  )(_)) /(/(   /(/(   ((_)\   )\    )\  '((_)\  
_(()((_)| |(_)((_)_ | |_ ((_)((_)_ ((_)_\ ((_)_\  | |(_) ((_) _((_)) | |(_) 
\ V  V /| ' \ / _` ||  _|(_-</ _` || '_ \)| '_ \) | '_ \/ _ \| '  \()| '_ \ 
 \_/\_/ |_||_|\__,_| \__|/__/\__,_|| .__/ | .__/  |_.__/\___/|_|_|_| |_.__/ 
                                   |_|    |_|                              
		''')
web = webdriver.Chrome(ChromeDriverManager().install())
web.get('https://web.whatsapp.com/')
name = input('Enter the name of user or group: ')
msg = input('Enter your message: ')
count = int(input('Enter the count: '))
input('Enter any key after scanning QR code')
web.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
web.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(msg)
web.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
for i in range(count):
    web.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(msg)
    web.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    print('Bombing Complete!!')
web.close()
'''
Author: Edward_LA
Email: wowofla@sina.com
Date: 2023-04-05 13:28:25
Description: 
Note: 
LastEditor: Edward_LA
LastEditTime: 2023-04-05 14:20:31
'''
import os
import sys
import openai

from PyQt6.QtWidgets import QApplication, QWidget

'''
------
OpenAI
------
openai.api_key = 'xx'

# Image generate
response = openai.Image.create(
    prompt = 'Caudate', 
    n=1, 
    size = '1024x1024'
    )

url = response['data'][0]['url']
print(url)

# Chat
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo", 
    messages=[
    {"role": "user", "content":"python is the best language?"}
    ]
    )
'''

'''
-----
PyQt6
-----
'''
app = QApplication(sys.argv)
window = QWidget()
window.show()
app.exec()




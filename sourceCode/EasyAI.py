'''
Author: Edward_LA
Email: wowofla@sina.com
Date: 2023-04-05 13:28:25
Description: 
Note: 
LastEditor: Edward_LA
LastEditTime: 2023-04-11 14:19:29
'''
import os
import sys
import openai
import base64
import pdb
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdksis.v1.region.sis_region import SisRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdksis.v1 import *

from PyQt6.QtWidgets import QApplication, QWidget



'''
------
OpenAI
------
openai.api_key = ''
'''
'''
# Image generate
response = openai.Image.create(
    prompt = '给我设计一个关于彗星的logo', 
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
------
HuaWei
------
hwak = ""
hwsk = ""
'''
'''
# Audio generate
credentials = BasicCredentials(hwak, hwsk) 

client = SisClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(SisRegion.value_of("cn-east-3")) \
    .build()


request = RunTtsRequest()
request.body = PostCustomTTSReq(
    text="你觉得我温柔吗",
    config={'property':'chinese_huaxiaoru_common'}
)
response = client.run_tts(request)
encode_string = response.result.data
wav_file = open("temp.wav", "wb")
decode_string = base64.b64decode(encode_string)
wav_file.write(decode_string)

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
print('test')




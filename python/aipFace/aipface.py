from aip import AipFace
from requests.api import options
import base64

APP_ID = '16850595'
API_KEY = '6uhScb0HHcPHLGXFMYUOglEp'
SECRET_KEY = 'TiTuvl5mUupxxvsBTq9HH6R6tCZZcMf8'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(image):
    with open(image,'rb') as fp:
        content = base64.b64encode(fp.read())
        return content.decode('utf-8')

for i in range(1,50):
    image = (str(i) + ".jpg")

    imageType = "BASE64"

    options = {}
    options['face_field'] = 'age,gender,beauty'

    # options = {}
    # options["face_field"] = "age"
    # options["max_face_num"] = 2
    # options["face_type"] = "LIVE"
    # options["liveness_control"] = "LOW"


    """ 调用人脸检测 """
    result = client.detect(get_file_content(image), imageType,options);

    print(result['result']['face_list'][0]['beauty'])
# """ 如果有可选参数 """

# """ 带参数调用人脸检测 """
# client.detect(image, imageType, options)
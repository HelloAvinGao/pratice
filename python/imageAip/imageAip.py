from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '24309663'
API_KEY = '7EFH7NfxBynGzcVGTDGocvRX'
SECRET_KEY = 'GM1zZR4qjHr9xmoNrAlzygoZVKig2uk5'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

#通用物体识别
# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()

# image = get_file_content('1.jpg')

# """ 调用通用物体识别 """
# client.advancedGeneral(image);

# """ 如果有可选参数 """
# options = {}
# options["baike_num"] = 5

# """ 带参数调用通用物体识别 """
# result = client.advancedGeneral(image, options)

# print(result)
#车辆识别
# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()

# image = get_file_content('car1.jpg')

# """ 调用车辆识别 """
# client.carDetect(image);

# """ 如果有可选参数 """
# options = {}
# options["top_num"] = 3
# options["baike_num"] = 5

# """ 带参数调用车辆识别 """
# result = client.carDetect(image, options)

# print(result)

# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()

# image = get_file_content('7.jpg')

# """ 调用菜品识别 """
# client.dishDetect(image);

# """ 如果有可选参数 """
# options = {}
# options["top_num"] = 3
# options["filter_threshold"] = "0.7"
# options["baike_num"] = 5

# """ 带参数调用菜品识别 """
# result = client.dishDetect(image, options)
# print(result)

""" 读取动物 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('11.jpg')

""" 调用动物识别 """
client.animalDetect(image);

""" 如果有可选参数 """
options = {}
options["top_num"] = 3
options["baike_num"] = 5

""" 带参数调用动物识别 """
result = client.animalDetect(image, options)
print(result)
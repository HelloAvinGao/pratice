from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '24309870'
API_KEY = 'Ni0vYj87wQCGmlrMfOQK4ZsP'
SECRET_KEY = 'ncUG6KleOSGOV4yyRGXwKIuLHawFExvm'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# #车牌识别
# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()

# image = get_file_content('car2.jpg')

# """ 调用车牌识别 """
# client.licensePlate(image);

# """ 如果有可选参数 """
# options = {}
# options["multi_detect"] = "true"

# """ 带参数调用车牌识别 """
# result = client.licensePlate(image, options)
# print(result)
#银行卡识别
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
for i in range(1,5):
    image = get_file_content('bank%d.jpg'%(i))

    """ 调用银行卡识别 """
    result = client.bankcard(image);
    print(result)
import easyocr
reader = easyocr.Reader(['ch_sim','en'],gpu = False) 
result = reader.readtext('test.png',detail = 0)
print(result)
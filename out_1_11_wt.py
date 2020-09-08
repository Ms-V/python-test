import json#导入JSON模块
# num=[2,3,5,7,11,13]
# fn='num.json'
# with open(fn,'w',encoding='utf-8') as jfile:
#     json.dump(num,jfile)

un=input('Name?')
fn='name.json'
with open(fn,'w',encoding='utf-8') as jfile:
    json.dump(un,jfile)
    print('Write in!')
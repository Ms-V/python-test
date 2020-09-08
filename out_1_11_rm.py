import json
def userg():
    fn='name.json'
    try:
        with open(fn) as jf:
            un=json.load(jf)
    except FileNotFoundError:
        un=input('Name?')
        with open(fn,'w',encoding='utf-8') as jf:
            json.dump(un,jf)
            print('Write in!')
    else:
        print('Emmm.'+un+' nice one!')
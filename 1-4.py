caijitaunhuo=['liqi','yinyangren','zhuzhu','niubi!']
print(caijitaunhuo)
print(caijitaunhuo[0]+" and "+caijitaunhuo[1])
print(caijitaunhuo[0].upper()+" and "+caijitaunhuo[1].upper())
print(caijitaunhuo[-1].title())
smg="cai ji "+caijitaunhuo[0].upper()+"!"
print(smg)
caijitaunhuo[0]="cai qi"
print(caijitaunhuo)
caijitaunhuo.append('erzi')
print(caijitaunhuo)
nt=[]
nt.append('m')
nt.append('m')
nt.append('a')
print(nt)
nt.insert(1,"p")
print(nt)
del nt[1]
print(nt)
pop_nt = nt.pop()
print(nt)
print(pop_nt)
nt.insert(2,'a')
print(nt," "+nt.pop(0))
nt.insert(0,'m')
nt.remove('a')
print(nt)
nt.insert(2,'a')
dsm='a'
print(nt)
nt.remove(dsm)
print(nt)
print('is this '+dsm.upper())
px=['gg','gb','ac','ag']
px.sort()
print(px)
px.sort(reverse=True)
print(px)
px=['gg','gb','ac','ag']
print(sorted(px))
print(sorted(px,reverse=True))
print(px)
elrs=['bc','af','aa','dg','bb']
print(elrs)
elrs.reverse()
print(elrs)
elrs.reverse()
print(elrs)
len_elrs=len(elrs)
print("is long ",len_elrs)
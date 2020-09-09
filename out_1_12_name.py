def get_name(fname,lname,mname=''):
    if mname:
        allname=fname+' '+mname+' '+lname
    else:
        allname=fname+' '+lname
    return allname
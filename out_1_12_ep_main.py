from out_1_12_ep import Employees
ep=Employees()
print('q to exit')
while True:
    ep.name=input('name:')
    if ep.name=='q':
        break
    ep.payment=input('payment:')
    if ep.payment=='q':
        break
    epadd=input('add payment:')
    if epadd=='q':
        break
    else:
        ep.addpayment==epadd
    ep.print_info()
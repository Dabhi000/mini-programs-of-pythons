import employee
print('salary program')
name = str(input('enter name of employee: '))
basic = float(input('enter basic salary: '))
netpay = employee.netpay(basic)
print(f'net salary: {netpay}')
grosspay = employee.grosspay(basic,netpay)
print(f'gross salary:{grosspay}')
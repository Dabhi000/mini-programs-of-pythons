#positional arguement
def positional(ram,shyam,harish):
    print('ram,shyan,harish')
a='ram'
b='shyam'
c='harish'
positional(a,b,c)

#keyword arguement
def keyword(ram,shyam,harish):
    print('ram,shyam,harish')
a='ram'
b='shyam'
c='harish'
keyword(ram=a,harish=c,shyam=b)

#default arguement
def keyword(ram,shyam,harish='harish'):
    print('ram,shyan,harish')

a='ram'
b='shyam'

keyword(ram=a,shyam=b)
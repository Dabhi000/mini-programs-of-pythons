def search(list,n):
    for i in range (len(list)):
        if list [i] == n:
            return true
        return False

list = [1,2,'sachin',4,'cricket',6]
n = 'sachin'
if search(list,n):
       print("found")
else:
       print("unfound")

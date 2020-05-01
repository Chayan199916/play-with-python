D = input("Enter the Date: ")
lis = D.split('/')
no_of_odds = 0
for i in range(3):
    lis[i] = int(lis[i])
mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if lis[2] % 4 == 0:
    mon[1] = 29
lis[2] = lis[2] - 1
lis[2] = lis[2] % 400
res1 = lis[2] % 100 
res2 = int(lis[2] / 100) 
no_of_odds = no_of_odds + res2 * 5
no_of_odds = no_of_odds % 7
res3 = int(res1 / 4)
res4 = res1 - res3
no_of_odds = no_of_odds + (res3 * 2) + res4
no_of_odds = no_of_odds % 7
lis[1] = lis[1] - 1
for i in range(lis[1]):
    no_of_odds = no_of_odds + mon[i]
no_of_odds += lis[0]
no_of_odds = no_of_odds % 7
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
if no_of_odds == 0 or no_of_odds == 6:
    print("It's weekend")
else:
    print("It is",days[no_of_odds])

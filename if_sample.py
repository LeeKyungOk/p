#if ~ else 구문
a = 120
if a> 100:
    print('a가 100보다 크다')
else :
    print('a가 100보다 같거나 작다')

#if ~ elif 구문
carSpeed = 80
lane = "비전용"
if lane == "전용":
    print('전용차선')
elif carSpeed > 100 :
    print('속도위반')
else :
    print('제한속도미만')

#for문
    for element in [1,2,3]:
        print(element)
#-------------------------------
    for k in range(5):
        print(k)
#-------------------------------
    a = [1,2,3,4,5]
    for k in range(len(a)) :
        print(k)
#-------------------------------
    for j in range(1,5) : 
        for k in range(j) :
            print(k)
        print()

#-------------------------------
    a = [[1,2,3],[4,5,6],[7,8,9]]
    for j in range(len(a)) :
        for k in range(len(a[j])) :
            print(a[j][k])
        print()
        
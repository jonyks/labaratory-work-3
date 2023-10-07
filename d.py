m,n=input('Введите позицию поля ').split()
k,l=input('Введите позицию фигуры ').split()
n,l=map(int, [n,l])
try:
    if int(m)>0 and int (m)< 9 and (n)>0 and  (n)< 9 : m= int (m)
except: 
    if m in 'ABCDEFGH': m=ord(m)-64
    else:
        print('Введите правильную позицию поля')
        quit()
try:
    if int(k)>0 and int (k)< 9 and (l)>0 and  (l)< 9 : k= int (k)
except: 
    if k in 'ABCDEFGH': k=ord(k)-64
    else:
        print('Введите правильную позицию поля')
        quit()
    
f=1
if (m+n)%2==(k+l)%2:print('Находятся на полях одного цвета')
else:
    print('Находятся на полях разного цвета')
    f=0

a=input('Введите название фигуры ').lower()
if a=='конь':
    if abs(m-k)==1 and abs(n-l)==2 or abs(m-k)==2 and abs(n-l)==1:
        print ('Есть угроза')
    else: print('Угрозы нет')
elif a=='ладья':
    if m==k or n==l:
        print ('Есть угроза')
    else: print('Угрозы нет')
elif a=='ферзь':
    if abs(m-k)==abs(n-l) or m==k or n==l:
        print ('Есть угроза')
    else: print('Угрозы нет')
elif a=='слон':
    if abs(m-k)==abs(n-l):
        print ('Есть угроза')
    else: print('Угрозы нет')
else: 
    print ('Введите правильное название фигуры')
    quit()

a=input('Введите название фигуры ').lower()
if a=='ладья':
    if m==k or n==l:print ('Можно дойти одним ходом')
    else:print ('Сходите на :', k,n)
elif a=='ферзь':
    if abs(m-k)==abs(n-l) or m==k or n==l:print ('Можно дойти одним ходом')
    else: print('Сходите на :',  k,n)
elif a=='слон':
    if abs(m-k)==abs(n-l):print ('Можно дойти одним ходом')
    elif f==0:print('Невозможно')
    else:
        for i in range(-7,7):
            if abs(m+i-k)==abs(n+i-l) and 0<m+i<9 and 0<n+i<9:
                print('Сходите на :',m+i,n+i )
                break
            elif abs(m+i-k)==abs(n-i-l) and 0<m+i<9 and 0<n-i<9:
                print('Сходите на :',m+i,n-i )
                break
else: 
    print ('Введите правильное название фигуры')
    quit()
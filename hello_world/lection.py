# N=int(input('Введите день недели ')) #задача №1 - определить выходной
# #print(N==6 or N==7)
# if N==6 or N==7:
#     print('да')
# else:
#     print('нет')

# X=int(input('Введите значение X '))  #задача №2 - определение четверть точки
# Y=int(input('Введите значение Y '))
# if X>0 and Y>0:
#     print('1')
# elif X<0 and Y>0:
#     print('2')
# elif X<0 and Y<0:
#     print('3')
# elif X>0 and Y<0:
#     print('4')
# else:
#     print('проверьте значения, X и Y не равны 0')

# N=int(input('Введите номер четверти ')) #задача№1 - определение диапазона значений координат по номеру четверти
# if N==1:
#     print('координаты точки: X(0,+infinity), Y(0,+infinity)') #не нашла, можно ли поставить знак бесконечности
# elif N==2:
#     print('координаты точки: X(-infinity,0) Y(0,+infinity)')
# elif N==3:
#     print('координаты точки: X(-infinity,0) Y(-infinity,0)')
# elif N==4:
#     print('координаты точки: X(0,+infinity), Y(-infinity,0)')
# else:
#     print('проверьте вводимые данные')

X1=int(input('Введите значение X первой точки ')) #задача№2 - нахождение расстояния между двумя точками
Y1=int(input('Введите значение Y первой точки '))
X2=int(input('Введите значение X второй точки '))
Y2=int(input('Введите значение Y второй точки '))
Disstance = round(pow(((X2-X1)**2+(Y2-Y1)**2), 0.5), 2) #не понимаю, почему math.sqrt((X2-X1)**2+(Y2-Y1)**2) не работает
print(Disstance)






from ast import Try


try:
    a= int(input('nhap a: '))
    b= int(input('nhap b: '))
    c= a/b
    print('a/b = %d'%c)
except Exception:
    print('không thê chia cho số 0')

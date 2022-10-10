try:
    age= int(input('nhap age:   '))
    if age<18:
        raise ValueError
    else:
        print('tuổi không hợp lệ!')
except ValueError:
    print('tuổi còn quá nhỏ')
def nhap_database():
    """Hàm nhập dữ liệu"""
    global listNum
    while True:
        try:
            tmp = input('nhập vào một số nguyên: ')
            if tmp == 'exit':
                break
            tmp = int(tmp)
            listNum.append(tmp)
        except ValueError:
            print('bạn phải nhập vào một số nguyên: ')


def in_chan(listNum):
    '''hàm in ra số chẳn'''
    for i in listNum:
        if i % 2 == 0:
            print(i, end=' ')


listNum = []
nhap_database()
in_chan(listNum)

from unittest import result


def nhapDatabase():
    '''hàm nhâp dữ liệu vào mảng'''
    global listStudent
    while True:
        tmp = input('nhập sinh viên: ')
        if tmp == '0':
            break
        listStudent.append(tmp)


def timStudent(name, listStudent):
    '''hàm tìm tên sinh viên'''
    result = 1
    for i in range(0, len(listStudent)):
        if listStudent[i] == name:
            result = i
            break
    return result


print('Quản lý sinh viên')
print('nhấn 1 để nhập sinh viên')
print('nhấn 0 để thoát')
listStudent = []
nhapDatabase()
name = input('nhap tên sinh viên muốn tìm: ')
index = timStudent(name, listStudent)
if index == 1:
    print('tên sinh viên không có')
else:
    print('tên sinh viên có ở vị trí: ', index)

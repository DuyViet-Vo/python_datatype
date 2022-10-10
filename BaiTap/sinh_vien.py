

print('Chương trình quản lý sinh viên')


def addStudent():
    '''hàm thêm sinh viên'''
    print('thêm sinh viên')
    # danh sách sinh viên
    global listStudent
    # cấu trúc lưu trữ
    info = {
        'id': '',
        'name': ''
    }
    # nhập ID kiểm tra xem id có bị trùng không
    id = input('nhâp id sinh viên: ')
    while True:
        student = findStudent(id)
        if student != False:
            id = input('id này đã có! mời nhập id khác!: ')
        else:
            break
    info['id'] = id
    info['name'] = input('Nhập tên sinh viên: ')
    listStudent.append(info)


def findStudent(id):
    '''hàm id sinh viên'''
    global listStudent
    for i in range(0, len(listStudent)):
        if listStudent[i]['id'] == id:
            # trả về mang gồm 2 phần tử
            return [i, listStudent[i]]
    return False


def showStudent():
    '''hàm hiển thị thông tin sinh viên'''
    print('---------danh sách sinh viên--------')
    global listStudent
    for i in range(0, len(listStudent)):
        print(listStudent[i]['id'], ':', listStudent[i]['name'])

def deleteStudent():
    '''hàm xoá sinh viên'''
    id = input('nhập id cần xoá : ')
    global listStudent
    student =findStudent(id)
    if student !=False:
        listStudent.remove(student[1])
        print('xoá sinh viên thành công')
    else:
        print('không tìm thấy sinh viên cần xoá')
        
def editStudent():
    global listStudent
    id = input('nhâp id sinh viên cần sửa')
    student= findStudent(id)
    if student!=False:
        name = input('nhập tên sinh viên: ')
        student[1]['name'] = name
        listStudent[student[0]] = student[1]
# main
listStudent = []
action = 0
while action >= 0:
    if action == 1:
        addStudent()
    elif action == 2:
        deleteStudent()
    elif action == 3:
        editStudent()
    elif action == 4:
        showStudent()
    print("Chọn chức năng muốn thực hiện:")
    print("Nhập 1: Thêm sinh viên")
    print("Nhập 2: Xóa sinh viên")
    print("Nhập 3: Sửa sinh viên")
    print("Nhập 4: Xem danh sách sinh viên")
    print("Nhập 0: Thoát khỏi chương trình")
    action = int(input())
    if action == 0:
        break

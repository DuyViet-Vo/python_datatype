def sap_xep_tang_dan(numbers):
 
    lenth = len(numbers)
 
    # Lặp từ phần tử đầu đến kế cuối,
    # Vì khi đến phần tử cuối là đã sắp xếp thànhcông
    for i in range(0, lenth - 1):
        for j in range(i + 1, lenth):
            if (numbers[i] > numbers[j]):
                # Hoán đổi vị trí
                tmp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp
 
    return numbers
 
# Chương trình chính
print("Chương trình sắp xếp mảng Python")
print("Bạn muốn tạo mảng có bao nhiêu phần tử", end=":")
 
length = int(input())
numbers = []
 
for i in range(0, length):
    print("Nhập phần tử thứ ", (i + 1), end=":")
    numbers.append(int(input()))
 
print("Mảng trước khi sắp xếp")
print(numbers)
 
print("Mảng sau khi sắp xếp")
print(sap_xep_tang_dan(numbers))
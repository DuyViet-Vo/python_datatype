try:  
    fileptr = open("file.txt","r")    
    try:  
        fileptr.write("Nội dung ghi vào file")  
    finally:  
        fileptr.close()  
        print("Đóng file")  
except:  
    print("Mở file lỗi")
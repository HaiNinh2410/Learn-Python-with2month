#Viết một chương trình có thể tính giai thừa của một số cho trước. 
# Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. 
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320

# #Cách 1:
# import  math
# numbers = input ('Nhap so de tinh giai thua:')
# n = int(numbers)
# print(n)
# giaithua=math.factorial(n)
# print(giaithua)

# #Cách 2:
# numbers = input ('Nhap so de tinh giai thua:')
# n = int(numbers)
# def a(x):
#     giaithua=giaithua 1*2*...*(x-1)*x
# print()

def ninhnguxi(n):
    if n==1:
        return 1
    else:
        return n*ninhnguxi(n-1)

v = ninhnguxi(3)
print(v)



    

         




#Tạo 1 biến x chạy từ phần tử đầu tiên trong list (có index[0]) đến phần tử gần cuối của list (có index[4])
#Tạo 1 biến y chạy từ phần từ thứ 2 trong list, có index[1] đến phần tử cuối cùng của list (có index[5])
#Nếu x<y thì đổi chỗ x và y bằng cách sử dụng 1 biến trung gian z

Dayso = [2,5,1,8,6,3]
a = len(Dayso)
print(a)
for x in range(0,a-1):
    print(x)
    for y in range(x+1,a):
        print(y)
        if (Dayso[x]<Dayso[y]):
            z = Dayso[x]
            Dayso[x]=Dayso[y]
            Dayso[y] = z
print(Dayso)
            


#Tạo x biến chạy từ phần tử đầu tiên đến phần tử sát cuối cùng
#Tạo y biến chạy từ phần tử thứ 2 đến phần tử cuối cùng 
#So sánh 2 biến, nếu x > y thì đổi chỗ 2 biến với nhau bằng cách dùng 1 biến trung gian z

Dayso = [2,5,1,8,6,3]
b = len(Dayso)
for x in range(0,b-1):
    for y in range(x+1,b):
        if (Dayso[x]>Dayso[y]):
            z = Dayso[x]
            Dayso[x]=Dayso[y]
            Dayso[y] =z
print(Dayso)

            

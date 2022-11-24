#Tạo 1 biến min, gán min =0 
#Tạo 1 biến x, cho x chạy từ đầu mảng tới cuối mảng 
#Nếu Mang(x)<min -> Gán min = Mang(x)
Mang = [50,30,20,100,15]
a = len(Mang)
min = Mang[1]
print(min)
for x in range(0,a):
    if (Mang[x]<min):
        min = Mang[x]
print(min)
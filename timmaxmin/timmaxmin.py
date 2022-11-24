#Gán 1 biến = max
#Cho max chạy từ đầu -> cuối mảng
#Nếu có phần tử > max thì gán max = phần tử đó 
Mang = [50,30,20,100,15]
a = len(Mang)

max=0
for x in range(0,a):
    if(Mang[x]>max):
        max=Mang[x]
print(max)
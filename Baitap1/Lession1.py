#Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, 
# nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). 
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
a=[]
for x in range(1999,3201):
    if (x%7==0) and (x%5!=0):
        a.append(x)
print(a) 

        
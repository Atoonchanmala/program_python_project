                       #   ຂໍ້ທີ 10         
                                    
number = int(input("ກະລຸນາປ້ອນຕົວເລກທີ່ທ່ານຕ້ອງການບວກແບບ factorial = "))
print("input = ",number)
fact = 1
sum = 0
result = 0
for i in range(1,number+1):
    fact = 1         
    # sum += fact
    for j in range(1,i+1): 
        fact = fact*j       # ສູດຄິດໄລ່ໃນການຄຳນວນແບບ factorial ເພາະວ່າການຄຳນວນແບບນີ້ມັນຈະເປັນການຄຳນວນແບບຄູນ
    sum += fact
    print(str(i)+"!",end = "")
    if i!=number:
        print("+",end="")
print(" Output = ",end = "")
print(fact)

while fact > 0:
    digit = fact%10
    result = digit + result
    print(digit,'+',end='')
    fact = fact//10
print('Output: ',result)

            # ຄ່າ sum ຂອງມັນຍັງປີ້ນຄ່າຢູ່ ກັບມາແກ້ໄຂໃຫມ່ 
# print(sum)               
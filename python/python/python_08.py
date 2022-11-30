                                    #  ຂໍ້ 8

min = 2
print("ກຳນົດໃຫ້ 2 ແມ່ນ min")
max = 1000
print("ກຳນົດໃຫ້ 1000 ແມ່ນ max")
print("ການກວດສອບຈຳນວນມູນແຕ່ 2 ຫາ 1000 ຂອງຕົວເລກແຕ່ : ", min ,"ຫາ",max,"ແມ່ນມີດັ່ງນີ້:")


for number in range(min,max + 1):
    # ຈຳນວນມູນທີ່ຫລາຍກວ່າ 1 
    
    if number > 1:
        for i in range(2,number):
            if(number % i) == 0:
                break
        else:
            
            print("%d " %number,end = '')

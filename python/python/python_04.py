                #  ຂໍ້ 4 
                
number = int(input("ກະລຸນາປ້ອນຕົວເລກ = "))   
result = 0
while number > 0:
    digit = number%10        
    print('digital: ',digit)
    result = result + digit    
    print("result: ",result)
    number = number//10       
    print("number: ",number)
print("Output : ",result)
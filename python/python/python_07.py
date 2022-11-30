                                #   ຂໍ້ 7

print("Enter times: ")
value = int(input())
if value >= 60:
    time = value // 60
    day = time // 24
    print(day, "day:", time % 24, "h:", value % 60, "mn")
else:
    print("0 day:", "0 h:", value % 60, "mn")
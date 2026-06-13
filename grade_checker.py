score= int(input("你的成绩是几分？"))
if score>= 90 and score<=100:
    print("汝有大帝之资")
elif score>=80 and score<90:
    print("汝有王侯之资")
elif score>=70 and score<80:
    print("汝有士大夫之资")
elif score>=60 and score<70:
    print("汝有平民之资")    
elif score<60 and score >0:
    print("汝有贱民之资")  
else:
    print("你个刁民")

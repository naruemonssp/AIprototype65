import subprocess #สำหรับรัน terminal command

if __name__ == "__main__":
    ## basic
#     subprocess.run(["ls", "-ltr"])
#     subprocess.run(["python", "python_script101.py", "--x","8"])
    
    ## use output of subprocess
#     process1 = subprocess.Popen(["python", "python_script101.py", "--x","8"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     out, err = process1.communicate()
#     print(out.decode('utf-8'))


#HW สั่งรัน python_script101.py 50 รอบ โดย x = 1,3,5,7,... 
        
    sum = 0 
    round = 0
    for x in range(1, 100, 2):  # ( เริ่มรอบที่ 1, หยุดรอบที่ 100, โดยข้ามทีละ 2 )
            round += 1   # เริ่มตั้งแต่รอบที่ 1 และเพิ่มขึ้นทีละ 1
            process2 = subprocess.Popen(["python", "python_script101.py", "--x",f'{x}'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process2.communicate()
            print(f"({round}) x = {x}")
            print(out.decode('utf-8'))
            sum += (x)

#แล้วให้เอา output ของ xt มารวมกัน แล้ว print ออกมา
       
    print(f'sum of x = {sum}')
    print(f'sum of xt = {sum + sum}')
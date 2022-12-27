from collections import OrderedDict
#Example: Giveaway; N person joining ; X person is your ; D times to draw
danhsach = {}

def solve(a,b,c):
    for i in range(c+1):
        #i += 1
        Pa = (b/a)**i
        Pa_ = ((a-b)/a)**(c-i)
        result = Chập(i, c) * Pa * Pa_

        percent = result*100
        #print(f"Rút trúng {i} người: " +str(result)+ f" ->{percent:.3f}%")
        danhsach.update({percent:i})

def Chập(k,n):
    res = int(giaiThua(n) / ((giaiThua(n-k))*giaiThua(k)))
    return(res)

def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)

def main():
    total = int(input('Enter the total number of participants: '))
    acc = int(input("Enter your entries (How many people do you have): "))
    times = int(input("How many times for withdraw?: "))
    solve(a=total, b=acc, c=times)
    sorting()
    
#Xắp xếp tỷ lệ nhỏ dần 
def sorting():
    dict1 =dict(OrderedDict(sorted(danhsach.items(), reverse=True)))
    for item in dict1.items():
        print(f"Chances of winning {item[1]} account(s): {item[0]:.3f}% ")

if __name__ == "__main__":
    main()
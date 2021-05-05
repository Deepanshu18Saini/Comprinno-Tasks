#enter number of strips
no_of_strips=input()
if (int(no_of_strips)>=1) and (int(no_of_strips)<=100):
    for strip in range(int(no_of_strips)):
        len_of_strip=input("Enter length of strip")
        if (int(len_of_strip)>=3) and (int(len_of_strip)<=100):
            height_strips=input(" Enter the no of hieght mentioned ")
            height_strip = a = [c for c in str(height_strips)]
            height_of_strip=list(map(int, height_strip))
            if height_of_strip[0]==1:
                check=1
                for k in range(int(len_of_strip)):
                    if (height_of_strip[k]>=1) and (height_of_strip[k]<=100):
                        continue
                    else:
                        check=0
                        break
                if check==1:
                    c=1
                    for i in range(int(len_of_strip)):
                        if height_of_strip[i]==height_of_strip[int(len_of_strip)-i-1]:
                            continue
                        else:
                            c=0
                            break
                    if c==1:
                        print("yes")
                    else:
                        print("no")
        else:
            print("no")

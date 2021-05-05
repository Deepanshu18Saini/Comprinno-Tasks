no_of_testcases=input()
#check constraint on number of testcases

if (int(no_of_testcases)>=1) and (int(no_of_testcases)<=1000000):
    test_case_list=[]
    array_list=[]
#Enter no of testcases
    for t in range(int(no_of_testcases)):
        testcases=input()
        test_case_list.append(testcases)
        array=input()
        array_list.append(array)
    for i,testcase in enumerate(test_case_list):
        if (int(testcase)>=1) and (int(testcase)<=100000) : # check constraint on each test cases
           
            st=list(map(int, array_list[i].split(" ")))
            
            if (sum(st)<=1000000 ) and (len(st)>1):
                check=1
                for i in range(len(st)):
                    if (st[i]>=-1000000000) and (st[i]<=1000000000):
                        for j in range(i+1,len(st)):
                            prod=st[i]*st[j]
                            if prod in st:
                                continue
                            else:
                                check=0
                                break
                if check==1:
                    print("yes")
                else:
                    print("no")

            else:
                print("no")
        
        else:
            print("no")
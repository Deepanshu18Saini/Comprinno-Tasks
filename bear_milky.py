no_of_testcases=input()
#check constraint on number of testcases

if (int(no_of_testcases)>=1) and (int(no_of_testcases)<=50):
    test_case_list=[]
    strings_list=[]
#Enter no of testcases
    for t in range(int(no_of_testcases)):
        testcases=input()
        test_case_list.append(testcases)
        strings=input()
        strings_list.append(strings)
    for i,testcase in enumerate(test_case_list):
        if (int(testcase)>=1) and (int(testcase)<=50) : # check constraint on each test cases
            st=strings_list[i].split(" ")
            if (len(st)>=1) and (len(st)<=50) and ( '"' not in st ) and  (int(testcase)==len(st)):
                check=1
                for i in st:
                    if i in ['cookie','milk']:
                        continue
                    else:
                        check=0
                if check==1:
                    t=1
                    for i,val in enumerate(st):
                        if val =="cookie":
                            if i+1<len(st):
                                if st[i+1]=="milk":
                                    continue
                                else:
                                    t=0
                                    break
                    if t==1:
                        print("yes")
                    else:
                        print("no")
                else:
                    print("no")

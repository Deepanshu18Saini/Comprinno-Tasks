no_of_testcases=input()
#check constraint on number of testcases

if (int(no_of_testcases)>=1) and (int(no_of_testcases)<=10):
    test_case_list=[]
    sticks=[]
#Enter no of testcases
    for t in range(int(no_of_testcases)):
        testcases=input()
        test_case_list.append(testcases)
        array=input()
        sticks.append(array)
        
    for i,testcase in enumerate(test_case_list):
        if (int(testcase)>=2) and (int(testcase)<=50000)  : # check constraint on each test cases
           
            st=list(map(int, sticks[i].split(" ")))
     
            if (st[i]>=1) and (st[i]<=100000):
                print(min(st)*(len(st)-1))
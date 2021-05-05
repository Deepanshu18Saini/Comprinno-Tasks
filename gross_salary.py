no_of_testcases=input()
#check constraint on number of testcases

if (int(no_of_testcases)>=1) and (int(no_of_testcases)<=1000):
    test_case_list=[]
    
#Enter no of testcases
    for t in range(int(no_of_testcases)):
        testcases=input()
        test_case_list.append(testcases)
    
    for i,testcase in enumerate(test_case_list):
        salary=list(map(int, testcase.split(" ")))
        for sal in salary:
            if (sal>=1) and (sal<=100000)  :
                if sal <=1500:
                    HRA=sal*(10/100)
                    DA=sal*(90/100)
                else:
                    HRA=500
                    DA=sal*(98/100)
                gross_sal=sal + HRA + DA
                print(gross_sal)
            else:
                print("Not Applicable")
        
            
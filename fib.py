#print number of testcases
no_of_testcases=input()
#check constraint on number of testcases

if (int(no_of_testcases)>=1) and (int(no_of_testcases)<=10):
    test_case_list=[]
#Enter no of testcases
    for t in range(int(no_of_testcases)):
        testcases=input()
        test_case_list.append(testcases)
    for testcase in test_case_list:
        if (len(testcase)>=1) and (len(testcase)<=100000) and (testcase.islower()): # check constraint on each test cases
            occurence_record={} #Creating a hash map for the string getting occurence of each testcase
            for alp in testcase:
                if alp in occurence_record:
                    occurence_record[alp]+=1
                else:
                    occurence_record[alp]=1
            sorted_table=dict(sorted(occurence_record.items(), key=lambda item: item[1])) #Sorting the hash table so that we can check fibinocci series
            value_list=[]
            for key, value in sorted_table.items():
                value_list.append(value)
            
            if len(value_list)<=3:# condition if lenght is less than or equal to three , its dynamic
                print("Dynamic")
            else:
                check=0
                for i in range(2,len(value_list)):
                    if (value_list[i]==value_list[i-1] + value_list[i-2] ):
                        check=1
                    else:
                        break
                if check==0:
                    print("Not")
                else:
                    print("Dynamic")
                

                    
no_of_testcases=input()
#check constraint on number of testcases

if (int(no_of_testcases)>=1) and (int(no_of_testcases)<=100):
    test_case_list=[]
    sticks=[]
#Enter no of testcases
    for t in range(int(no_of_testcases)):
        testcases=input()
        test_case_list.append(testcases)
        array=input()
        sticks.append(array)
        sum_testcases=list(map(int, array.split(" ")))
    for i,testcase in enumerate(test_case_list):
        if (int(testcase)>=1) and (int(testcase)<=1000) and (sum(sum_testcases)>=1) and (sum(sum_testcases)<=1000) : # check constraint on each test cases
           
            st=list(map(int, sticks[i].split(" ")))
            check=1
            occurence_record={}
            for i in range(len(st)):
                if (st[i]>=1) and (st[i]<=1000):
                    
                    if st[i] in occurence_record:
                        occurence_record[st[i]]+=1
                    else:
                        occurence_record[st[i]]=1
                
            width=-1
            length=-1
            
            for key,value in occurence_record.items():
                if value >=2:
                    if key>=width:
                        width=key
                    if key>=length:
                        length=key
                
            
            area=width*length
           
            if area>1:
                print(area)
            else:
                print("-1")


        
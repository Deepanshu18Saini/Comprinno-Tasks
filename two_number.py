no_of_testcases=input()
#check constraint on number of testcases

if (int(no_of_testcases)>=1) and (int(no_of_testcases)<=100):
    test_case_list=[]
    
#Enter no of testcases
    for t in range(int(no_of_testcases)):
        testcases=input()
        test_case_list.append(testcases)
    
    for i,testcase in enumerate(test_case_list):
        st=list(map(int, testcase.split(" ")))
        alice_count=st[0]
        bob_count=st[1]
        total_count=st[2]
        if (alice_count>=0) and (alice_count<=1000000000) and (bob_count>=0) and (bob_count<=1000000000) and (total_count>=0) and (total_count<=1000000000) :
            for j in range(total_count):
                if (j%2==0):
                    alice_count*=2
                else:
                    bob_count*=2
        print(max(alice_count,bob_count)//min(alice_count,bob_count))

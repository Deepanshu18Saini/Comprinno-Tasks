no_of_testcases=input()
#check constraint on number of testcases

if (int(no_of_testcases)>=1) and (int(no_of_testcases)<=1000):
    test_case_list=[]
    
#Enter no of testcases
    for t in range(int(no_of_testcases)):
        testcases=input()
        test_case_list.append(testcases)
    
    for i,testcase in enumerate(test_case_list):
        if testcase in ['b','B','c','C','d','D','f','F']:
            if (testcase=='b') or (testcase=='B'):
                print("BattleShip")
            elif (testcase=='c') or (testcase=='C'):
                print("Cruiser")
            elif (testcase=='d') or (testcase=='D'):
                print("Destroyer")
            else:
                print("Frigate")
        else:
            print("not valid")
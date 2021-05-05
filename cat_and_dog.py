no_of_testcases=input()
#check constraint on number of testcases

if (int(no_of_testcases)>=1) and (int(no_of_testcases)<=100000):
    test_case_list=[]
    
#Enter no of testcases
    for t in range(int(no_of_testcases)):
        testcases=input()
        test_case_list.append(testcases)
    
    for i,testcase in enumerate(test_case_list):
        st=list(map(int, testcase.split(" ")))
        cat_count=st[0]
        dog_count=st[1]
        leg_count=st[2]
        if (cat_count>=0) and (cat_count<=1000000000) and (dog_count>=0) and (dog_count<=1000000000) and (leg_count>=0) and (leg_count<=1000000000) and (leg_count%4==0):
            total_animal=cat_count+ dog_count
            total_legs=4*total_animal
            counted_animal=leg_count/4
            remaining_animal=total_animal-counted_animal
            remaining_leg=total_legs - leg_count

            if (remaining_leg<=8*remaining_animal):
                print("yes")
            else:
                print("no")
        else:
            print("no")
else:
    print("no")


with open("test.csv",'r') as f:
    with open("cut_test.csv",'w') as f1:
        next(f) #skip first line
        for line in f:
            f1.write(line)

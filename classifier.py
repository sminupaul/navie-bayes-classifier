import csv
with open('new_set.csv','rb')as f:
    count_yes=0
    count_no=0
    reader =csv.reader(f)
    dataset = list(reader)
    for row in dataset:
        if(row[4]=='yes'):
            count_yes=count_yes+1
        else:
            count_no=count_no+1
    size=len(dataset)

    x1=raw_input("property1\t")
    #print x1
    x2 = raw_input("property2\t")
    x3= raw_input("property3\t")
    x4 = raw_input("property4\t")
    c=0
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    c7=0
    for row in dataset:
        #print row[1]
        if(row[0]==x1):
            if(row[4]=='yes'):
                c+=1
            else:
               c1+=1

        if row[1]==x2:
            #print row[1]
            if (row[4] == 'yes'):
                c2+= 1
            else:
                c3+= 1
        if row[2]==x3:
            if (row[4] == 'yes'):
                c4+= 1
            else:
                c5+= 1
        if row[3]==x4:
            if (row[4] == 'yes'):
                c6+= 1
            else:
                c7+= 1

    cx1=float(c)/count_yes
    c1x1=float(c1)/count_no
    cx2=float(c2)/count_yes
    c1x2=float(c3)/count_no
    cx3 = float(c4) / count_yes
    c1x3 = float(c5) / count_no
    cx4=float(c6)/count_yes
    c1x4=float(c7)/count_no
    print x1,"and yes ",cx1
    print x1,"and no " , c1x1
    print x2,"and yes " , cx2
    print x2 , "and yes " , c1x2
    print x3, "and yes ", cx3
    print x3, "and no ", c1x3
    print x4, "and yes ", cx4
    print x4, "and no ", c1x4
    a=float(count_yes)/size
    b=float(count_no)/size
    class_yes=cx1*cx2*cx3*cx4*a
    class_no=c1x1*c1x2*c1x3*c1x4*b
    print "class No: ",class_no
    print "class Yes: ",class_yes
    import csv
    with open('ne.csv', 'wb') as fp:
        write = csv.writer(fp)
        data=[x1,x2,x3,x4,'yes']
        if (class_yes >class_no ):
            data = [x1, x2, x3, x4, 'yes']
            print "Belong to class yes"
            write.writerow(data)
        else:
            data = [x1, x2, x3, x4, 'no']
            print"Belong to class no"
            write.writerow(data)




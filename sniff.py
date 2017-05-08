import csv
with open('/home/kgecit/Desktop/chatbot/output.csv') as csvin:
    readfile = csv.reader(csvin, delimiter=";")
    with open('/home/kgecit/Desktop/chatbot/output1.csv', 'wb') as csvout:
        writefile = csv.writer(csvout, delimiter=";", lineterminator='\n')
	flag=0
	i=0
        for row in readfile:
            if(flag==0):
		row.extend(["last name"])
		flag=1
	    else:
		row.extend(["random_last_name"+str(i)])
	    i=i+1
            writefile.writerow(row)

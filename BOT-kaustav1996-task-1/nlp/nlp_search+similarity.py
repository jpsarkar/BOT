#imported os to use clear screen
import os
#the package nltk is imported 
import nltk
#text is a specefic datatype used in the nltk package
from nltk.text import Text
data=""
#UI -->
#while loop used for reapeted drawing odf the UI from begining
while(1):
	os.system('clear')
	border=80
	heading="Natural Language Processing Search Engine"
	print("*"*border)
	print(" "*int((border-len(heading))/2)+heading+" "*int((border-len(heading))/2))
	print("*"*border)
	print("\n")
	print("\n")
	print("1.Enter File\n")
	print("\n")
	print("2.Search String\n")
	print("\n")
	print("3.Exit\n")
	print("\n")
	print("*"*border)
	n=int(input())
	if n==3:
		exit()
	if n==1 :
		print("Enter File Path:")
		#file input
		file_path=input()
		with open (file_path, "r") as myfile:
			data=data+myfile.read()
		data_text=Text(nltk.word_tokenize(data))
		print(data_text)
	if n==2 :
		strr=input()
		#used nltk.concordance to search
		data_text.concordance(strr)
		print("\nSIMILAR\n")
		#used nltk.similar to search similar texts
		data_text.similar(strr)
	if n!=1 and n!=2 and n!=3 :
		os.system('clear')
		print("Wrong Input. press ENTER to continue...")
	#used a dummy input to note pause the while loop in the end
	z=input()

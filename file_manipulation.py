#assignment-3 file manipulation
#author Menelik Belete
import codecs
import re
import string
def file_manipulation():
	
	line_count=1;count1,count2,count3=0,0,0
	total_line,total_char,total_word,i,j=0,0,0,0,0
	word_frequency=[];word_list=[];word_deposit=[]
	word_frequency_dictionary={}
	last_value=0
	special_char='[\s,.#@%^&*:_();/\'!~`+-]'
	try:
		file_name=raw_input("Please Enter File Name:")
		display_word=input("Enter Number of Words You Want Display:-")
		text_file=codecs.open(file_name,'r',encoding='utf-8')
	except IOError:
		print "The File Can't Be Open!!!"
	all_line=text_file.read().rstrip()
	#removing unwanted char from the file using regula expression
	'''for ch in all_line:
		if (re.match(special_char,ch) is not None):
			all_line=all_line.replace(ch,' ')'''
	#replacing all punctuation with space by using the string.punctuation method
	for ch in all_line:
		if ch in string.punctuation:
			all_line=all_line.replace(ch,' ')
	#-----------------------------------------
	all_words=all_line.lower().split()
	for ch in all_words:
		if count2<=len(all_words):
			word_count=all_words.count(ch)
			if ch not in word_frequency_dictionary:
			  word_frequency_dictionary[ch]=word_count
		count2=count2+1
	'''Sort a dictionar for displaying in desending order'''
	sort_dictionary=word_frequency_dictionary.items()
	sort_dictionary.sort()
	print "Most five frequent words and their frequency\n------------------------------"
	print "Frequency\t\tWrods\n----------------------------"
	'''for y in range(len(sort_dictionary)):
		print "[",sort_dictionary[i][1],"-------------------->",sort_dictionary[i][0],"]"
		i=i+1'''
	'''Here the display is based on the user input, but if there is the same value words appear in the last,
	they will be display'''

	for key, value in sorted(word_frequency_dictionary.iteritems(), key=lambda (k,v): (v,k),reverse=True):		
		if i<display_word:	# words
			print "[",value,"-------------------->",key,"]"
			last_value=value
		elif display_word==i and value==last_value:
			print "[",value,"-------------------->",key,"]" #the last words will be display if theye are the same value
			last_value=value
			i-=1
		else:
			break	#break the loop while i=display_word-1
		i+=1

	#-------Most Frequent Characters-----------
	char_freq_counter(file_name)

	#count total number of lines in the file	
	total_line=total_line_counter(file_name)
	total_char=total_char_counter(file_name)
	#---------------------------------------
	print "Statistical Information\n-------------------------"
	print "File Name------------------>",file_name
	print "Total Number of Line------->",total_line
	print "Total Number Of Wrods------>",len(sort_dictionary)
	print "Total Number of Characters->",total_char
	
	text_file.close()

#-------------------------------------------
def total_line_counter(file_name):

	i,total_line=0,0
	text_file=codecs.open(file_name,'r',encoding='utf-8')
	all_line=text_file.read().strip().split('\n')
	'''line=text_file.readline().strip()
	while line!='':		
		total_line=total_line+1
		line=text_file.readline().strip()'''
	for line in range(len(all_line)):		
		if all_line[line]=='':
			#all_line.remove(all_line[line]) #remove white space from the list
			i+=1 #number if newline in the file
	total_line=len(all_line)-i	#substract the total number of newline form the total line
	text_file.close()
	return total_line
#-----------------------------------------
def total_char_counter(file_name):	
	total_char=0
	special_char='[\s,.#@%^&*:_();/\'!~`+-]'
	text_file=codecs.open(file_name,'r',encoding='utf-8')
	#all_line=text_file.read().strip().split()
	all_line=text_file.read().strip().lower()
	for ch in all_line:
		if ch.isspace()==False and (re.match(special_char,ch)) is None:
			char_count=len(ch)
			total_char=total_char+char_count
	text_file.close()
	return total_char
#-----------------------------------------
def char_freq_counter(file_name):

	total_char=0
	special_char='[\s,.#@%^&*:_();/\'!~`+-]'
	text_file=codecs.open(file_name,'r',encoding='utf-8')
	all_line=text_file.read().strip().lower()
	counter_list=[];item_deposit=[];item_freq=[]
	item_dictionary={}
	counter=1;counter2=0;counter3=0;i=0
	#-------------------------------------
	#count the frequency of the characters
	file_lower=all_line
	for ch in file_lower:
		if counter2<=len(file_lower):
			item_count=file_lower.count(ch)
			if (ch not in item_dictionary) and ch.isspace()==False and ch!='\n' and (re.match(special_char,ch) is None):
			  item_dictionary[ch]=item_count
		counter2=counter2+1	
	sort_dictionary=item_dictionary.items()
	sort_dictionary.sort()
	print "Most five frequent characters and their Frequency\n------------------------------"
	print "Frequency     Character\n------------------------------"
	'''for y in range(len(sort_dictionary)):
		print sort_dictionary[i][0].upper(),"---------->",sort_dictionary[i][1],""
		i=i+1'''
	for key, value in sorted(item_dictionary.iteritems(), key=lambda (k,v): (v,k)):
		if i<=5:
			print "[",value,"------------->",key,"]"
		else:
			break	#break the loop while i=6
		i+=1
#-------------------------------------------
def main():
	print "Python Text File Manipulation\n------------------------------"
	print "1. To Open File"
	print "2. To Exit"
	c=raw_input("Please Your Choice:")
	if int(c)==1:
	  file_manipulation()
	  y_or_n=raw_input("Do You Want Open Another File? (Y/N): ")
	  while y_or_n=='y' or y_or_n=='Y':
	    file_manipulation()
	    y_or_n=raw_input("Do You Want Open Another File? (Y/N): ")
	else:
	  exit()
	
	
#calling main function
main()

from bs4 import BeautifulSoup
import requests
import csv

#get and parse the html data, keeping just <label> tags
url = "http://osoc.berkeley.edu/OSOC/osoc?p_term=FL&p_list_all=Y"
r = requests.get(url)
data = r.text
soup=BeautifulSoup(data)
soup = soup.find_all('label')
soup_list = [item.get_text() for item in soup]

#remove extra <label> elements from the front of the HTML
new_list = soup_list[3:]


#remove unicode junk in front of course numbers
for i in range(len(new_list)):
	if (i - 1) % 3 == 0:
		new_list[i] = new_list[i][3:]

#remove unicode u' tags
new_list = [str(item) for item in new_list]

#prepare the list, list_to_csv, which holds a sublist for each file
#each sublist is of the form [department, number, description]

list_to_csv = []
for i in range(len(new_list) / 3):
	sub_list = [new_list[i], new_list[i+1], new_list[i+2]]
	list_to_csv.append(sub_list)

#write the csv file
resultFyle = open("output.csv",'wb')
wr = csv.writer(resultFyle, dialect='excel')
for course in list_to_csv:
	wr.writerow(course)
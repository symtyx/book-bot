import json
import pandas

file = open('catalog_data.json')
data = json.load(file)
new_csv = open("json.csv", 'w')


# print(data[0]['name'])
# print(data[0]['courses'][0]['code'])
# print(data[0]['courses'][0]['sections'][0]['name'])

for i in range(len(data)):
	line = '' #line to write
	#through each course number for a department
	for j in range(len(data[i]['courses'])):
		#through each section for a course
		for k in range(len(data[i]['courses'][j]['sections'])):
			line += data[i]['name']
			line += " "
			line += data[i]['courses'][j]['code']
			line += " "
			line += data[i]['courses'][j]['sections'][k]['name']
			line += "\n"
			# print(line)
			new_csv.writelines(line) #writes to new csv file here
			line = ''

file.close()
new_csv.close()
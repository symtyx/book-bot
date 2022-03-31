import json

file = open('catalog_data.json')
data = json.load(file)

for i in data:
	# i['name'] for department name
	print(i['name'])
	for j in i['courses']:
		# j['name'] to get each course number
		print("\n=&= Course Number =&=")
		print(j['name'])
		print("=&= Section Numbers =&=")
		for z in j['sections']:
			# z['name'] to get each section number of course
			print(z['name'])
	break

file.close()
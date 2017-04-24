import json

one_json = open('one_json.json', 'r').readlines()

for i in one_json:
	data = json.loads(i)


#for i in data:
#	print i

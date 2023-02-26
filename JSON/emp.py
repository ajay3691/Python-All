import json

fp = open('emp.json', 'r')
emp_dict=json.load(fp)
fp.close()

print(emp_dict)
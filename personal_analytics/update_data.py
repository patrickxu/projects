from tempfile import NamedTemporaryFile
import shutil
import csv
import datetime
import sys
import ast

today = datetime.date.today()
fieldnames = ['date', 'run', 'sleep', 'read', 'watch', 'hoop']

def create_file(file_):
	"""
		to create initial data file
	"""

	with open(file_, 'w') as csvFile:
		writer = csv.DictWriter(csvFile, delimiter=',', quotechar='"', fieldnames=fieldnames)
		writer.writeheader()

def append_list(arg, in_, out_):
	"""
		used to either create or append to watch/read
	"""
	if in_[arg] == '':
		in_[arg] = [out_[arg]]
	else:
		lst = ast.literal_eval(in_[arg])
		lst.append(out_[arg])
		in_[arg] = lst


def update_row(in_, update_):
	"""
		update row if the dates match
	"""
	if 'run' in update_.keys():
		in_['run'] = float(in_['run']) + update_['run']
	if 'sleep' in update_.keys():
		in_['sleep'] = float(in_['sleep']) + update_['sleep']
	if 'read' in update_.keys():
		append_list('read', in_, update_)
	if 'watch' in update_.keys():
		append_list('watch', in_, update_)

def clean_row(in_):
	"""
		clean the row to append
	"""
	if 'date' not in in_.keys():
		in_['date'] = today
	if 'read' in in_.keys() and '[' not in in_['read']:
		in_['read'] = [in_['read']]
	if 'watch' in in_.keys() and '[' not in in_['watch']:
		in_['watch'] = [in_['watch']]
	if 'sleep' not in in_.keys():
		in_['sleep'] = 0
	if 'run' not in in_.keys():
		in_['run'] = 0
	if 'hoop' not in in_.keys():
		in_['hoop'] = 0

def update(file_, update_):
	"""
		update file by adding or updating row
	"""
	tempfile = NamedTemporaryFile(delete=False)
	old_entry = False
	with open(file_, 'rb') as csvFile, tempfile:
		reader = csv.reader(csvFile, delimiter=',', quotechar='"')
		writer = csv.DictWriter(tempfile, delimiter=',', quotechar='"', fieldnames=fieldnames)
		for row in reader:
			to_write = dict(zip(fieldnames, row))
			if str(today) == to_write['date']:
				print "Checks out"
				old_entry = True
				update_row(to_write, update_)		
		writer.writerow(to_write)
		if old_entry == False:
			clean_row(update_)		
			writer.writerow(update_)
	shutil.move(tempfile.name, file_)

def print_file(file_):
	"""
		print the data
	"""
	with open(file_, 'r') as csvFile:
		reader = csv.reader(csvFile, delimiter=',', quotechar='"')	
		for row in reader:
			print row

if __name__ == '__main__':
	if sys.argv[1] == 'create':
		var = raw_input("Please Enter Filename: ")
		if '.csv' not in var:
			var = var + '.csv'
		create_file(var)
		print "You created", var
	elif sys.argv[1] == 'update':
		cols = raw_input("Please Enter Columns To Update: ")
		vals = raw_input("Please Enter Values To Update: ")
		var = dict(zip(cols.split(','), vals.split(',')))
		update('pers_data.csv', var)
	elif sys.argv[1] == 'print':
		print_file('p_data.csv')
	else:
		print "Sorry, I Don't Recognize That Function"
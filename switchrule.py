def getKeys(key_list):
	return key_list + ['protocol_param']
	#return key_list + ['plan'] # append the column name 'plan'

def isTurnOn(row):
	return True
	#return row['plan'] == 'B' # then judge here


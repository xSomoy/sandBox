# Demonstrated Python Program
# to read file character by character


from xml.dom.minidom import TypeInfo


file = open('demo', 'r')
blob = ''
while 1:
	
	# read by character
	char = file.read(1)		
	if not char:
		break
	if char == '\n':
		char = '_'
	blob = blob + char
print(blob)
file.close()

from string import ascii_lowercase, ascii_uppercase

_alphabet = ascii_lowercase+ascii_uppercase+"1234567890"
_specials = ",./;'[]\*+-!@#$%^&*()"
print(_alphabet)

def divide_into_parts(line):
	result = []
	string = ""
	for symbol in line:
		if symbol in _alphabet:
			string += symbol

		else:
			result.append(string)
			string = ''
			string += symbol
			result.append(string)
			string = ''
	
	return result
print(divide_into_parts("1+11"))
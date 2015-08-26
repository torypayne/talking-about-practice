def unique_chars(my_string):
	string_dict = {}
	for letter in my_string:
		try: 
			string_dict[letter]
			return False
		except:
			string_dict[letter] = 1
	return True

def custom_reverse(my_string):
	return my_string[::-1]

def permutation(string1,string2):
	string_dict = {}
	for letter in string1:
		try:
			string_dict[letter] += 1
		except:
			string_dict[letter] = 1
	for letter in string2:
		try:
			string_dict[letter] -= 1
			if string_dict[letter] < 0:
				return False
		except:
			return False
	return True

def twenty_percent(my_string):
	string_list = my_string.split(" ")
	my_string = "%20".join(string_list)
	return my_string

def compressed_word(my_string):
	active_letter = my_string[0]
	active_letter_count = 0
	new_string = ""
	for letter in my_string:
		if letter == active_letter:
			active_letter_count += 1
		else:
			new_string = new_string + active_letter + str(active_letter_count)
			active_letter = letter
			active_letter_count = 1
	new_string = new_string + active_letter + str(active_letter_count)
	if len(my_string) < len(new_string):
		return my_string
	else:
		return new_string

def rotated_by_90(my_matrix):
	rotation = zip(*(my_matrix)[::-1])
	return rotation
def numbers_to_message(pressed_sequence):
	message = []

	lowercased_keypad = [[" "], [], ['a', 'b', 'c'], ['d', 'e', 'f'],\
	['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],\
	['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

	uppercased_keypad = [[" "], [], ['A', 'B', 'C'], ['D', 'E', 'F'],\
	['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],\
	['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

	previous = -1

	keypad = lowercased_keypad

	j = 0

	letter_is_picked = False

	for i in pressed_sequence:
		print(message, "previous: ", previous, 'picked: ', letter_is_picked)

		if i == 1:
			keypad = uppercased_keypad
			previous = 1
			continue

		if i == -1:
			j = 0
			previous = -1
			continue

		if i == previous:
			j += 1
			message.pop()
		else:
			j = 0
			if previous != 1:
				letter_is_picked = True

		try:
			message.append(keypad[i][j])
		except IndexError:
			j = 0
			message.append(keypad[i][j])

		if letter_is_picked and keypad is uppercased_keypad:
			keypad = lowercased_keypad

		previous = i

	return "".join(message)


print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))
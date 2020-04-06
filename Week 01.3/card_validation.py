def is_credit_card_valid(number):
	number = list(str(number))

	if len(number) % 2:

		the_undoubled_half = [int(i) for i in number[::-2]]
		the_doubled_half = ''.join([str(int(i) * 2) for i in number[-2::-2]])
		the_doubled_half = [int(i) for i in the_doubled_half]

		return sum(the_undoubled_half + the_doubled_half) % 10 == 0
	else:
		return False


print(is_credit_card_valid(79927398713))
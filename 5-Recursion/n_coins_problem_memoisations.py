# Given a list of possible dominations of conis and a target value find the smallest possible number of conis that will add up to the target
# eg coins = [1, 5, 10, 25] target = 26 ans = 2 ----> 25 + 1


def n_coins_memoised(target, coins, known_values={}):
	if target in coins:
		return 1
	if target <= 0:
		return 0
	if target in known_values.keys():
		return known_values[target]
	min_coin = target
	for i in [c for c in coins if c < target]:
		num_coin = 1 + n_coins_memoised(target - i, coins, known_values)
		if num_coin < min_coin:
			min_coin = num_coin
			known_values[target] = min_coin
	return min_coin
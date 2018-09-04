def multiple(value):
	mult = 0
    counter = 1
    while ab < value or ac < value:
        ab = counter*3
        ac = counter*5
        mult += (ab+ac)
        counter += 1
	return mult

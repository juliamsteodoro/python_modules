def ft_count_harvest_iterative():
	days_until_harvest = int(input("Days until harvest: "))
	i = 1
	while(days_until_harvest >= i):
		print("Day", i)
		i += 1
	print("Harvest time!")

if __name__ == "__main__":
	ft_count_harvest_iterative()

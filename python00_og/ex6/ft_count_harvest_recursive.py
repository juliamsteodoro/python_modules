def ft_count_harvest_recursive(days=None):
    if days is None:
        days = int(input("Days until harvest: "))
    if (days == 0):
        print("Harvest time!")
        return
    elif (days > 0):
        print("Day", days)
        ft_count_harvest_recursive(days - 1)

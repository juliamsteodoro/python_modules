# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jumoreir <jumoreir@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/14 10:57:56 by jumoreir          #+#    #+#              #
#    Updated: 2026/09/14 11:18:05 by jumoreir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	def show(self):
		print(f"Created: {self.name}: {round(self.height, 1)}cm, {self.age} days old")

if __name__ == "__main__":
	print("=== Plant Factory Output ===")
	plants = [
		Plant("Rose", 25, 30),
		Plant("Oak", 200, 365),
		Plant("Cactus", 5, 90),
		Plant("Sunflower", 80, 45),
		Plant("Fern", 15, 120),
	]
	for plant in plants:
		plant.show()
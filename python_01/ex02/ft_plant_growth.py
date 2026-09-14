# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jumoreir <jumoreir@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/14 10:58:04 by jumoreir          #+#    #+#              #
#    Updated: 2026/09/14 10:58:06 by jumoreir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
		
	def grow(self):
		self.height += 0.8

	def age_up(self):
		self.age += 1
	def show(self):
		print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

if __name__ == "__main__":
	print("=== Garden Plant Growth ===")
	rose = Plant("Rose", 25, 30)
	initial_height = rose.height
	rose.show()
	for i in range(1, 8):
		print(f"=== Day {i} ===")
		rose.grow()
		rose.age_up()
		rose.show()
	print(f"Growth this week: {round((rose.height - initial_height), 1)}cm")
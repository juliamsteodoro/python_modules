# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jumoreir <jumoreir@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/14 10:58:12 by jumoreir          #+#    #+#              #
#    Updated: 2026/09/14 11:12:18 by jumoreir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	def show(self):
		print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
	print("=== Garden Plant Registry ===")
	rose = Plant("Rose", 25, 30)
	sunflower = Plant("Sunflower", 80, 45)
	cactus = Plant("Cactus", 15, 120)
	rose.show()
	sunflower.show()
	cactus.show()
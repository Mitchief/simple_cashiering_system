class cashieringsystem:

	def __init__(self, a=0, r=0, receive=0, change=0, temp=0):

		print("\n\n*****WELCOME TO SIMPLE CASHIERING SYSTEM*****\n")

		self.a = a
		self.r = r
		self.receive = receive
		self.change = change
		self.temp = temp

	def foods(self):

		print("*****MY CONVENIENT STORE*****")

		print("1.Mars--------->£10", "\n"
		      "2.Sneakers----->£7", "\n"
		      "3.Twix--------->£9", "\n"
		      "4.KitKat------->£5","\n"
		      "5.Cash Out: £","\n"
		      "6.Exit")

		while 1:

			c = int(input("Shopped:\n"))

			if c == 1:

				d = int(input("Enter the quantity:\n"))
				self.r = self.r + 10 * d

			elif c == 2:
				d = int(input("Enter the quantity:\n"))
				self.r = self.r + 7 * d

			elif c == 3:
				d = int(input("Enter the quantity:\n"))
				self.r = self.r + 9 * d

			elif c == 4:
				d = int(input("Enter the quantity:\n"))
				self.r = self.r + 5 * d

			elif c == 5:
				print("total:", self.r)
				if self.r > 0:
					recieve = int(input("Money Recieved:\n"))
					print("Change:", recieve - self.r)
					print("*****Thank You, Come Again!!!*****")
					quit()
			elif c == 6:
				quit()
			else:
				print("Invalid option")


def main():
	a = cashieringsystem()

	while 1:
		a.foods()


main()

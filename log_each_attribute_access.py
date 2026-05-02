from datetime import datetime
class AuditClass:

	def __init__(self, user=None):
		self._user = user or "Unknown"


	def __getattribute__(self, name):
		# avoid logging internal attributes to prevent recursion
		if not name.startswith("_"):
			timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

			# safely fetching the user without recursion
			user_name = super().__getattribute__("_user")

			print(f"[{timestamp}] {user_name} has accessed the {name}")

		return super().__getattribute__(name)



	def __getattr__(self, name):
		timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

		# safely fetching the user without recursion
		user_name = super().__getattribute__("_user")

		print(f"[{timestamp}] {user_name} tried to access the {name}, which is not available!")



class BankAccount(AuditClass):
	bank_name = "SBI"
	def __init__(self, name, age, balance):
		super().__init__(name)
		self.name = name
		self.age = age
		self.account_balace = balance




b = BankAccount("Harsh", 26, 2928394898)

b.name
b.age
b.account_balace
b.abc
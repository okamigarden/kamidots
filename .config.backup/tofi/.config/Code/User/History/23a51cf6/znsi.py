from L8_Lib import BankAccount

acc1 = BankAccount(1, 100)
acc2 = BankAccount(2, 100)

# INITIAL BALANCE
print()
print(f"Current Balance Account 1: {acc1.get_balance()}")
print(f"Current Balance Account 2: {acc2.get_balance()}")


# WITHDRAW
acc1.withdraw(40)
acc2.withdraw(40)

# BALANCE
print()
print(f"Current Balance Account 1: {acc1.get_balance()}")
print(f"Current Balance Account 2: {acc2.get_balance()}")

# DEPOSIT
acc1.deposit(20)
acc2.deposit(20)

# BALANCE
print()
print(f"Current Balance Account 1: {acc1.get_balance()}")
print(f"Current Balance Account 2: {acc2.get_balance()}")

# TRANSFER
acc2.transfer(20, acc1)

# BALANCE
print()
print(f"Current Balance Account 1: {acc1.get_balance()}")
print(f"Current Balance Account 2: {acc2.get_balance()}")


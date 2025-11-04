# ==========================================
# 🧠 ENCAPSULATION IN PYTHON
# ==========================================
# Encapsulation is the concept of bundling data (variables)
# and methods (functions) together into a single unit — a class.
# It also restricts direct access to some of the object's data
# to protect it from accidental modification.

# Python does not have strict access modifiers like Java,
# but it uses naming conventions:
#   public    → variable/method is accessible everywhere
#   protected → variable/method name starts with single underscore _
#   private   → variable/method name starts with double underscore __

# ==========================================
# Example: BankAccount Class
# ==========================================

class BankAccount:
    def __init__(self, account_holder, balance):
        # Public attribute
        self.account_holder = account_holder

        # Protected attribute (should not be modified directly)
        self._account_type = "Savings"

        # Private attribute (cannot be accessed directly outside)
        self.__balance = balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited: ₹{amount}")
        else:
            print("❌ Invalid deposit amount")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"💸 Withdrawn: ₹{amount}")
        else:
            print("❌ Insufficient balance or invalid amount")

    # Public method to check balance
    def check_balance(self):
        print(f"💰 Available Balance: ₹{self.__balance}")

    # Protected method (meant for internal or subclass use)
    def _show_account_type(self):
        print(f"🏦 Account Type: {self._account_type}")

    # Private method (fully hidden from outside access)
    def __secret_method(self):
        print("🔒 This is a private method")

# ==========================================
# Main Program
# ==========================================

account = BankAccount("Lokii", 5000)

# Public access (Allowed)
print("👤 Account Holder:", account.account_holder)

# Protected access (Allowed but discouraged)
print("⚠️ Protected (accessing _account_type):", account._account_type)

# Private access (NOT allowed directly)
# print(account.__balance)  # ❌ Error: AttributeError

# Accessing via public methods (Recommended)
account.deposit(2000)
account.withdraw(1500)
account.check_balance()

# Trying to access private variable (Trick: name mangling)
print("🔍 Accessing private balance using name mangling:",
      account._BankAccount__balance)

# Protected method (technically allowed)
account._show_account_type()

# Private method (cannot access directly)
# account.__secret_method()   # ❌ Error
# But can be accessed using name mangling (not recommended)
account._BankAccount__secret_method()


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
    

#     def deposit(self, amount):
        
#         if amount < 0 :
#             print("Invalid Amount")
#         else:
#             self.balance += amount
#         print(f'Your balance has been updated with {amount} naira')
        

#     def withdraw(self,amount):
#         self.balance -=  amount
#         print(f'You withdraw {amount} naira')




# tola_account = BankAccount("Tolani Mujeeb", 29999)
# ola_account = BankAccount('Ola Mide',5008)

# print(tola_account.owner)
# tola_account.deposit(2000)
# print(tola_account.balance)
# tola_account.withdraw(4000)
# print(tola_account.balance)




# # Fill in the class
import math

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        

    def volume (self):
        return math.pi * (self.radius **2) * self.height

    def surface_area(self):
        return 2 * math.pi * (self.radius **2) + 2 * math.pi * self.radius * self.height

# EXAMPLE EXECUTION

cylinder = Cylinder(2,3)
cylinder1 = Cylinder(5,7)
print(cylinder.volume())  # 56.52
print(cylinder.surface_area())  # 94.2




# You are building a simple simulation of a fantasy battle. Create different types of game 
# characters.

# 1. Create a base class
# Create a class called GameCharacter that has:
# Attributes:
# name (string)
# health (integer)
# attack_power (integer)

# Methods:
# A method attack(target) that reduces the target's health by self.attack_power.

# 2. Create subclasses
# Warrior
# Has an extra attribute: armor (integer)
# Override attack(target) so that it deals extra 10 damage.

# Mage
# Has an extra attribute: mana (integer)
# Override attack(target) so that it uses 5 mana each time it attacks. 
# If mana is less than 5, print "Not enough mana to attack".

# 3. Handle cases where the target is the same as the attacker


# class GameCharacter:


    
#     def __init__(self, name, health, attack_power):
#         self.name = name 
#         self.health = health
#         self.attack_power = attack_power



#         def 


# def get_sum(*args):
#     result=0
#     for num in args:
#         if not isinstance(num,(float, int)):
#             return -1
#         result+=num
#     return result/len(args)
# print(get_sum(1,4,7))


# class BankAccount:
#     def __init__(self,owner, balance=0) :
#         self.owner=owner
#         self.balance=balance
#     def deposit(self, amount):
#         if amount>=0:
#             self.balance += amount
#         else:
#             print("amount must be positive")

#     def withdraw (self, amount):
#         if amount>self.balance:
#             print("Insufficient funds")
#         elif amount>0:
#             self.balance-=amount
#         else:
#             print("amount must be positive")
#     def get_balance(self):
#         return self.balance
#     def  __str__(self):
#         return f'BankAccount({self.owner}, balance={self.balance})'

# class Book:
#     def __init__(self,title,autor, available=True):
#         self.title=title
#         self.autor=autor
#         def __str__(self):
#             return f'Book({self.title})'


# class Library:
#     def __init__(self):
#         self.books=[]
#     def add_book(self, book):
        # pass
#     def borrow_book(self,title):
#         pass
#     def return_book(self,title):
#         pass


def palindrome(text):
    if not isinstance(text,str):
        return False
    left, right = 0, len(text)-1
    while left < right:
        if text[left] != text[right]:
            return False
        left +=1
        right-=1
    return True

print(palindrome("racecar"))
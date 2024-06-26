#!/usr/bin/env python3

# =============================================================================
# bankaccount.py
#
# A file containing the BankAccount class.
#
# Noah S. Roberts
# 04/19/2024
# Assignment 12
# for Module 10
# =============================================================================


from __future__ import \
    annotations  # allows type annotations in method definition within the same class; see BankAccount.transfer() on line 136

import stdarray
import stdio


class Name:
	"""
	Name object
	
	Arguments
	---------
		first (str): first name
		last (str): last name
		middle (str; default ''): middle name or initial
	"""

	def __init__(self, first: str, last: str, middle=''):
		self.first = first
		self.last = last
		self._middle = middle

	
	def middle(self, initial=False):
		if self._middle == '':
			return ''
		elif len(self._middle) == 1 or initial == True:
			return f'{self._middle[0]}. '
		else:
			return f'{self._middle} '


	def fullName(self, useMiddleInitial=False):
		middle = self.middle(initial=useMiddleInitial)
		return f'{self.first} {middle}{self.last}'
	

	# special methods
	def __str__(self):
		return self.fullName()
	

	def __repr__(self):
		return f'Name(first={self.first} last={self.last} _middle={self._middle})'




class BankAccount:
	"""
	A new bank account
	
	Arguments
	---------
		account_number (int): account number
		account_holder (str): account holder name
		balance (float; default 0.0): account balance
	"""

	def __init__(self, account_number: int, account_holder: Name, balance=0.0):
		self.account_number = int(account_number)
		self._acctHolder: Name = account_holder
		self._balance = float(balance)

		stdio.writeln(str(self))


	def balance(self) -> float:
		"""
		Account balance. Implemented as a method, as actual variable may be obfuscated in the future.
		"""
		return self._balance
	

	def account_holder(self) -> str:
		"""
		Account holder. Returns __str__ of the account holder Name object.
		"""
		return str(self._acctHolder)


	def deposit(self, amount: float | int, quiet=False) -> float | None:
		"""
		Depost the specified amount into the account, then prints account details post-deposit (can be disabled).

		Arguments
		---------
			amount (float or int): amount to deposit; most be positive.

		Returns
		-------
			account balance post-deposit (float) if successful.
		"""

		if type(amount) not in [float, int] or amount <= 0:
			stdio.writeln('Invalid deposit amount. Deposit amount must be a positive number.')
		else:
			self._balance += amount
			if quiet != True:
				stdio.writef('Successful deposit of $%.2f.\n', amount)
				stdio.writeln(self)
			return self._balance
	

	def withdraw(self, amount: float | int, quiet=False) -> float | None:
		"""
		Withdraw the specified amount from the account, then print account details post-withdrawal (can be disabled).

		Arguments
		---------
			amount (float or int): amount to withdraw; must be positive, and the amount must not exceed the current account balance.

		Returns
		-------
			account balance post-withdrawal (float) if successful.
		"""
		if type(amount) not in [float, int] or amount <= 0:
			stdio.writeln('Invalid withdraw amount. Withdraw amount must be a positive number.')
		elif self.balance() - amount < 0:
			stdio.writeln('Insufficient funds.')
		else:
			self._balance -= amount
			if quiet != True:
				stdio.writef('Successful withdrawal of $%.2f.\n', amount)
				stdio.writeln(self)
			return self._balance
	
	
	def transfer(self, recipient: BankAccount, amount: float | int) -> None:
		"""
		Transfer the specified amount to the specified account, then print the balances of each account post-transfer.

		Arguments
		---------
			recipient (BankAccount): bank account to transfer ot
			amount (float or int): amount to transfer		
		"""

		if type(amount) not in [float, int] or amount <= 0:
			stdio.writeln('Invalid transfer amount. Withdraw amount must be a positive number.')
		elif self.balance() - amount < 0:
			stdio.writef('Attempted to transfer $%.2f from %s to %s, but %s has insufficient funds.\n', amount, self.account_holder(), recipient.account_holder(), self.account_holder())
		else:
			# check if withdrawal was successful. only continue if yes.
			if self.withdraw(amount, quiet=True) != None:
				# check if deposit was successful. only continue if yes.
				if recipient.deposit(amount, quiet=True) != None:
					stdio.writef('Successfully transfered $%.2f from %s to %s.\n', amount, self.account_holder(), recipient.account_holder())

					# because trial withdrawals and deposits were ran quietly, we need to print the __str__ of both self and recipient manually
					stdio.writeln(self)
					stdio.writeln(recipient)
				else:
					stdio.writef('Transfer from %s to %s failed. Account balances will remain unchanged.\n', self.account_holder(), recipient.account_holder())
					# revert withdrawal from self, as deposit to recipient failed.
					self.deposit(amount, quiet=True)
			else:
				stdio.writef('Transfer from %s to %s failed. Account balances will remain unchanged.\n', self.account_holder(), recipient.account_holder())

	
	# special methods
	def __str__(self):
		return f'Acct. number: {self.account_number:<6d} Acct. holder: {self.account_holder():23s} Balance: {self.balance():.2f}'
	

	def __repr__(self):
		return f'BankAccount(account_number={self.account_number} _acctHolder={repr(self._acctHolder)} _balance={self._balance})'



# test client stuff
def _tcsection(text: str):
	"""
	Test client output section. Has a two-line gap above. Format example:
	```
————————————————————————————————————
 * Printing final account details * 
————————————————————————————————————
	```
	"""
	bar = ''.join(stdarray.create1D(len(text) + 6, '—'))
	return f'\n\n{bar}\n * {text} * \n{bar}'


def _tcsubsection(text: str):
	"""
	Test client output sub-section. Has a one-line gap above. Format example:
	```
 * Testing valid transfer * 
————————————————————————————
	```
	"""
	bar = ''.join(stdarray.create1D(len(text) + 6, '—'))
	return f'\n * {text} * \n{bar}'


def _tc():
	"""
	Test client. Not part of the API, so don't use it!
	"""

	stdio.writeln('NOTE: Output from test client will have an asterisk on each end and either bars above and/or below each line.')


	# creation
	stdio.writeln(_tcsection('Creating new accounts for testing'))
	a = BankAccount(
		297,
		Name('Alice', 'Eckert'),
		balance=1000.00
	)
	b = BankAccount(
		4971,
		Name('Bob', 'Smith', middle='J'),
		balance=500
	)
	c = BankAccount(
		23,
		Name('Kurop', 'Чunjał', middle='Jan'),
		balance=120954686
	)


	# deposit
	stdio.writeln(_tcsection('Testing invalid deposits'))
	a.deposit(-2374.23456234862)
	b.deposit('this is not a float')

	stdio.writeln(_tcsubsection('Testing valid deposit'))
	a.deposit(784.32)


	# withdrawal
	stdio.writeln(_tcsection('Testing invalid withdrawals'))
	c.withdraw(-125234.64)
	a.withdraw(268347962.43)
	a.withdraw('this is not a float')

	stdio.writeln(_tcsubsection('Testing valid withdrawal'))
	b.withdraw(2.17)


	# transfer
	stdio.writeln(_tcsection('Testing invalid transfers'))
	c.transfer(a, -2498234.53)
	a.transfer(b, 283472.56)
	b.transfer(c, 'this is not a float')

	stdio.writeln(_tcsubsection('Testing valid transfer'))
	c.transfer(b, 32621.14)

	
	# final account details
	stdio.writeln(_tcsection('Printing final account details'))
	stdio.writef('%s\n', a)
	stdio.writef('%s\n', b)
	stdio.writef('%s\n', c)

	stdio.writeln(_tcsection('End test client.'))


if __name__ == '__main__':
	_tc()


# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
# 
# $ python bankaccount.py 
#	[too lorge to fit here]
#
# -----------------------------------------------------------------------------
# EXTRA NOTES
# -----------------------------------------------------------------------------
#
# 1. Yes, the account holder of account number 23 is, in fact, Kurop Jan 
#	 Чunjał. It's written in a conlang.
#
# =============================================================================

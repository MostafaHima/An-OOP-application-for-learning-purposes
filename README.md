# OOP Applications for Account and Student Management

## Description

This is an OOP application for learning purposes, developed in Python. It covers two main areas:

1. **Bank Account Management**: 
   - Supports banking operations such as deposit, withdrawal, and transfer between accounts.
   - Keeps track of account balances and ensures transactions are valid.

2. **Student Management**: 
   - Tracks student information, including name, age, and grade.
   - Determines whether a student is passing based on their grade.

## Features

- **Bank Account Operations**:
  - Deposit funds into an account.
  - Withdraw funds from an account if the balance is sufficient.
  - Transfer money between accounts.
  
- **Student Management**:
  - Displays student information.
  - Checks if a student is passing based on their grade (passing grade is 50 or above).

## Usage

1. **Bank Account**:
   - Create a bank account using a unique account number.
   - Perform deposit, withdrawal, and transfer operations.

2. **Student**:
   - Create a student with a name, grade, and age.
   - Check if the student is passing by calling the `get_info()` method.

## Example

```python
# Create bank accounts
account1 = BankAccount(1)
account1.deposit(1000)

# Create students
student1 = Student("Mohamed", 80, 20)
student1.get_info()

# Transfer between accounts
account2 = BankAccount(2)
account1.transform(2, 500)
```


## Output
  ```python
        Name: Mohamed
        Age: 20
        Grade: 80
        Stats = successful

  +----------------+----------------------+
| Account Number |       Balance        |
+----------------+----------------------+
|       1        |         500          |
|  Transactions  |   Deposited: 1000    |
|                |    Withdrew: 500     |
|                | Transferred 500 to 2 |
+----------------+----------------------+


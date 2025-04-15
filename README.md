# 🏧 SimpleATMSystem

A basic command-line ATM simulation in Python. It allows users to register, log in, deposit money, withdraw funds, and check their balance. Ideal for learning file handling, basic authentication, and modular programming.

---

## 📂 Project Structure

| File / Module            | Description |
|--------------------------|-------------|
| [Menu.py](project/Menu.py)         | 🔷 **Main entry point**: Displays menu and connects all modules |
| [Register.py](project/Register.py) | 📝 **Handles user registration** (username + PIN) |
| [Login.py](project/Login.py)       | 🔐 **Validates user login** using username and PIN |
| [Deposit.py](project/Deposit.py)   | 💰 **Lets users deposit money** after login |
| [Withdraw.py](project/Withdraw.py) | 💸 **Allows users to withdraw money** |
| [Viewbalance.py](project/Viewbalance.py) | 📊 **Displays current account balance** |
| [session.py](project/session.py)   | 🧠 **Manages session**: Stores currently logged-in user (e.g. in `session.txt`) |
| [users](project/users)   | 🗃️ **Stores user data**: username, PIN, and balance |
| `__pycache__/`               | ⚙️ Auto-generated bytecode (you can ignore this folder) |

---
->Run the main program
python Menu.py

->Example commands:
1 - Register a new account
2 - Login to your account
3 - Deposit money
4 - Withdraw money
5 - Check balance
6 - Exit

->No additional dependencies required - uses Python standard library only


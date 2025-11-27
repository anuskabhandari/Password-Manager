# Password Manager

##  Project Overview
The *Password Manager* is a Python application that lets users *store, manage, and retrieve passwords securely*.  
Passwords are *encrypted* using the `cryptography` library to protect user data.

## Demo Video 
Watch the demo of the Password Manager here: [Demo Video](https://drive.google.com/file/d/1p4WwMAgpA_7vLZ40Id8NjMhvMsmPhSLc/view?usp=sharing)


This project demonstrates:
- File handling (`json`)  
- Functions and modular code design  
- Encryption and decryption  
- Loops, conditionals, and menu-based interaction  
- Optional automated testing

---

##  Features
# Core Features
1. Add New Passwords  
   - Save credentials for websites (site, username, password).  

2. View Saved Passwords  
   - Decrypt and display stored passwords safely.  

3. Encryption 
   - Uses `Fernet` encryption from the `cryptography` library.  

4. File Storage 
   - Saves credentials in `passwords.json` in a structured format.  

5. Automated Tests (Optional) 
   - `test_project.py` can verify encryption, decryption, and file handling.

---

##  Requirements
- Python 3.10+  
- Python libraries:
  - `cryptography` → `pip install cryptography`  
  - `pytest` → for running tests
---


## File Structure

PasswordManager/
├─ project.py           # Main program
├─ test_project.py      # Optional tests
├─ requirements.txt     # Dependencies
├─ README.md            # This file

## AUTHOR 
Anuska Bhandari


##  How to Run
1. Install dependencies
```bash
pip install -r requirements.txt
2. Run The program
python project.py

3.Menu Options:

[A] Add a new password

[V] View saved passwords

[Q] Quit



from cryptography.fernet import Fernet
import json
import os

# Global key variable
key = None

#Generate key only once and save it to file
def generate_key():
    if not os.path.exists("key.key"):
        key= Fernet.generate_key()
        with open("key.key","wb") as key_file:
            key_file.write(key)


def load_key():
    return open("key.key", "rb").read()

def encrypt_password(password ,key):
    return Fernet(key).encrypt(password.encode()).decode()

def decrypt_password(encrypted , key):
    return Fernet(key).decrypt(encrypted.encode()).decode()

#Main program
def main():
    generate_key()
    key = load_key()

    if not os.path.exists("passwords.json"):
        with open("passwords.json","w") as f:
            json.dump({}, f)

    while True:
        choice= input("\nChoose: [A]dd , [v]iew ,[Q]uit:").lower()
        if choice == "q":
          break
        elif choice =="a":
          site =input("Website: ")
          user = input("Username: ")
          pwd = input("Password: ")

          encrypted_pwd = encrypt_password(pwd ,key)


          with open("passwords.json" ,"r") as f:
              data= json.load(f)

              data[site] = {"username": user , "password":encrypted_pwd}
              with open("passwords.json","w") as f:
                  json.dump(data, f, indent=4)

              print("Password saved successfully!")
        elif choice =="v":
          with open("passwords.json","r") as f:

            data = json.load(f)

          for site , info in data.items():
            print(f"\n🌐 {site}")
            print(f"👤 {info['username']}")
            print(f"🔑 {decrypt_password(info['password'], key)}")

        else:
            print("Invalid choice! Please select A, V, or Q.")    
if __name__=="__main__":
  main()            





        
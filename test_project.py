import pytest
import json
import os
from project import encrypt_password, decrypt_password, load_key

# Load encryption key
key = load_key()

def test_encryption_decryption():
    original = "MySecret123!"
    encrypted = encrypt_password(original, key)
    decrypted = decrypt_password(encrypted, key)
    assert decrypted == original, "Decryption should return original password"

def test_add_and_retrieve_password():
    test_site = "TestSite"
    test_user = "testuser"
    test_pwd = "TestPass123!"

    # Encrypt password
    encrypted_pwd = encrypt_password(test_pwd, key)

    # Add to temporary JSON
    temp_file = "temp_passwords.json"
    data = {}
    data[test_site] = {"username": test_user, "password": encrypted_pwd}
    with open(temp_file, "w") as f:
        json.dump(data, f)

    # Retrieve and decrypt
    with open(temp_file, "r") as f:
        stored_data = json.load(f)
    retrieved_pwd = decrypt_password(stored_data[test_site]["password"], key)

    assert retrieved_pwd == test_pwd, "Retrieved password should match original"

    # Cleanup
    os.remove(temp_file)

def test_file_creation():
    temp_file = "temp_passwords.json"
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    # Create file
    with open(temp_file, "w") as f:
        json.dump({}, f)

    assert os.path.exists(temp_file), "File should be created"
    os.remove(temp_file)

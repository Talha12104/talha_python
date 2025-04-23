from hashlib import sha256

def login(emails, saved_login, password_to_check):
    if saved_login[emails] == hash_password(password_to_check):
        return True
    return False

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def main():
    saved_login ={
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }

    print(login("example@gmail.com", saved_login, "word"))
    print(login("example@gmail.com", saved_login, "password"))
    
    print(login("code_in_placer@cip.org", saved_login, "Karel"))
    print(login("code_in_placer@cip.org", saved_login, "karel"))
    
    print(login("student@stanford.edu", saved_login, "password"))
    print(login("student@stanford.edu", saved_login, "123!456?789"))

if __name__ == "__main__":
    main()
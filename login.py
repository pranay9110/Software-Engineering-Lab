def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Invalid username or password"


# Test the login function
print(login("admin", "1234"))
print(login("user", "123"))
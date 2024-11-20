import requests
from colorama import Fore, init
import time

# Initialize colorama for colored text output
init(autoreset=True)

# Logo function to display at the beginning
def show_logo():
    logo = """
\033[1;36m$$$$$$$\   $$$$$$\     $$$$$\ 
\033[1;36m$$  __$$\ $$  __$$\    \__$$ |
\033[1;34m$$ |  $$ |$$ /  $$ |      $$ |
\033[1;34m$$$$$$$  |$$$$$$$$ |      $$ |
\033[1;36m$$  __$$< $$  __$$ |$$\   $$ |
\033[1;32m$$ |  $$ |$$ |  $$ |$$ |  $$ |
\033[1;33m$$ |  $$ |$$ |  $$ |\$$$$$$  |
\033[1;33m\__|  \__|\__|  \__| \______/ 
 
        \033[1;34m  /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$   /$$  /$$$$$$  /$$   /$$
          \033[1;33m| $$__  $$ /$$__  $$|__  $$__/| $$  | $$ /$$__  $$| $$  /$$/
          \033[1;36m| $$  \ $$| $$  \ $$   | $$   | $$  | $$| $$  \ $$| $$ /$$/ 
          \033[1;36m| $$$$$$$/| $$$$$$$$   | $$   | $$$$$$$$| $$$$$$$$| $$$$$/  
          \033[1;33m| $$____/ | $$__  $$   | $$   | $$__  $$| $$__  $$| $$  $$  
          |\033[1;35m $$      | $$  | $$   | $$   | $$  | $$| $$  | $$| $$\  $$ 
          \033[1;36m| $$      | $$  | $$   | $$   | $$  | $$| $$  | $$| $$ \  $$
          \033[1;53m|__/      |__/  |__/   |__/   |__/  |__/|__/  |__/|__/  \__/
          
╔═════════════════════════════════════════════════════════════╗
║  \033[1;31mTOOLS      : GUROP UID + RAJ               
║  \033[1;32mLOGIN      : PAGE TOKEN EXTRACTOR
║  \033[1;32mRULEX      : UP FIRE RUL3X
║  \033[1;34mBR9ND      : MR D R9J PATHAK
║  \033[1;37mGitHub     : https://github.com/Raj-Thakur420
║  \033[1;32mWH9TS9P    : +919695003501
╚═════════════════════════════════════════════════════════════╝
    """
    print(Fore.YELLOW + logo)
    print(Fore.CYAN + "Welcome to Facebook Access Token Tool!")
    time.sleep(1)  # Add a small delay to make the logo visible

# Function to fetch and list all Messenger Groups for a given Facebook Access Token
def get_messenger_groups(access_token):
    url = f'https://graph.facebook.com/v17.0/me/conversations?access_token={access_token}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            print(Fore.GREEN + "\nList of Messenger Groups and their UIDs:")
            for conversation in data['data']:
                conversation_id = conversation['id']
                conversation_name = conversation.get('name', 'No name available')
                print(Fore.CYAN + f"Group Name: {conversation_name} | Group UID: {conversation_id}")
        else:
            print(Fore.YELLOW + "No Messenger groups found or unable to access group data.")
    else:
        print(Fore.RED + f"Error: {response.status_code}")
        print(response.text)

# Function to fetch pages managed by the user and their access tokens
def get_facebook_pages(access_token):
    url = f'https://graph.facebook.com/me/accounts?access_token={access_token}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            print(Fore.GREEN + "\nList of Pages and their Tokens:")
            for page in data['data']:
                page_name = page['name']
                page_id = page['id']
                page_token = page['access_token']
                print(Fore.CYAN + f"Page Name: {page_name} | Page ID: {page_id} | Page Token: {page_token}")
        else:
            print(Fore.YELLOW + "No pages found or unable to access page data.")
    else:
        print(Fore.RED + f"Error: {response.status_code}")
        print(response.text)

# Function to fetch cookies associated with the Access Token
def get_facebook_cookies(access_token):
    session = requests.Session()
    url = f'https://graph.facebook.com/me?access_token={access_token}'
    response = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if session.cookies:
        print(Fore.GREEN + "\nCookies found for the session:")
        for cookie in session.cookies:
            print(Fore.CYAN + f"Cookie Name: {cookie.name} | Cookie Value: {cookie.value}")
    else:
        print(Fore.YELLOW + "No cookies found in the session.")
    return session.cookies

# Function to display the token details (user info)
def get_token_details(access_token):
    url = f'https://graph.facebook.com/me?access_token={access_token}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'name' in data:
            print(Fore.GREEN + f"\nLogged in as: {data['name']} (User ID: {data['id']})")
        else:
            print(Fore.YELLOW + "Unable to retrieve user details from the access token.")
    else:
        print(Fore.RED + f"Error: {response.status_code}")
        print(response.text)

# Main function to execute the script
def main():
    # Display logo
    show_logo()

    # Input Facebook Access Token
    access_token = input(Fore.MAGENTA + "Enter your Facebook Access Token: ")

    if not access_token:
        print(Fore.RED + "Error: The access token is empty or invalid.")
        return

    # Display a preview of the token (first 10 characters)
    token_name = access_token[:10]
    print(Fore.YELLOW + f"\nFacebook Access Token (Name Preview): {token_name}...")

    # Fetch and display token details (user info)
    get_token_details(access_token)

    # Fetch and list Messenger Groups
    get_messenger_groups(access_token)

    # Fetch and list Facebook pages and their access tokens
    get_facebook_pages(access_token)

    # Fetch cookies from the session (example)
    get_facebook_cookies(access_token)

if __name__ == "__main__":
    main()
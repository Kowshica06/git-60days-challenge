# day3.py
# Day 3: Python Scripting Challenges Collection

# Challenge 1: Greeting message
def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome!")

# Challenge 2: Count words in a text file
def count_words_in_file(filename='sample.txt'):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print(f"Total words in '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Challenge 3: Generate a random password
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated password: {password}")

# Challenge 4: Check for prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime():
    number = int(input("Enter a number: "))
    print(f"{number} is {'a prime' if is_prime(number) else 'not a prime'} number.")

# Challenge 5: Ping server list
import os

def ping_servers(filename='servers.txt'):
    try:
        with open(filename, 'r') as file:
            servers = file.read().splitlines()
            for server in servers:
                response = os.system(f"ping -c 1 {server}")
                status = "reachable" if response == 0 else "unreachable"
                print(f"{server} is {status}")
    except FileNotFoundError:
        print(f"Server list file '{filename}' not found.")

# Challenge 6: Fetch public API using requests
import requests

def fetch_api_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            data = response.json()
            print("Title:", data['title'])
            print("Body:", data['body'])
        else:
            print("Failed to fetch API data")
    except Exception as e:
        print("Error:", e)

# Challenge 7: Automate file renaming
import os

def rename_files(directory='.'):
    try:
        for idx, filename in enumerate(os.listdir(directory)):
            if os.path.isfile(os.path.join(directory, filename)):
                ext = filename.split('.')[-1]
                new_name = f"file_{idx}.{ext}"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
                print(f"Renamed {filename} to {new_name}")
    except Exception as e:
        print("Error:", e)

# Challenge 8: Monitor CPU and memory
import psutil
import time

def monitor_usage(interval=5, iterations=3):
    for _ in range(iterations):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu}% | Memory Usage: {memory}%")
        time.sleep(interval)

# Challenge 9: Create a Linux user using subprocess
import subprocess

def create_linux_user(username='testuser'):
    try:
        subprocess.run(['sudo', 'useradd', username], check=True)
        print(f"User '{username}' created successfully.")
        result = subprocess.run(['id', username], check=True, capture_output=True, text=True)
        print("Verification:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error occurred:", e)

# Driver section to test all
if __name__ == "__main__":
    print("Running all Day 3 challenges...")

    # 1. Greet user
    greet_user()

    # 2. Count words in file
    count_words_in_file()

    # 3. Generate password
    generate_password()

    # 4. Check prime
    check_prime()

    # 5. Ping servers
    ping_servers()

    # 6. Fetch API
    fetch_api_data()

    # 7. Rename files
    rename_files()

    # 8. Monitor system
    monitor_usage()

    # 9. Create Linux user (requires sudo)
    create_linux_user()

import csv
import os
import subprocess

def add_user(username):
    subprocess.run(["useradd", username])

def add_group(groupname):
    subprocess.run(["groupadd", groupname])

def add_user_to_group(username, groupname)
    subprocess.run("usermod", "-aG", groupname, username)

def main(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row['username']
            groups = row['groups'].split(',')

            Joe
            if not os.system(f"id {username} > /dev/null 2>&1"):
                add_user(username)
            
            Susan
            for group in groups:
                if not os.system(f"getent group {group} > /dev/null 2>&1"):
                    add_group(group)
            
            Frank
            for group in groups:
                if username not in subprocess.getoutput(f"getent group {group} | cut -d: -f4").split(','):
                    add_user_to_group(username, group)

if __name__ == "__main__":
    csv_file = "user_groups.csv"  # Replace with your CSV file's path
    main(csv_file)

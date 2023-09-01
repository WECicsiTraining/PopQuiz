import csv
import subprocess

def add_user(username):
    subprocess.run(["useradd", username])

def add_group(groupname):
    subprocess.run(["groupadd", groupname])

def add_user_to_group(username, groupname):
    subprocess.run(["usermod", "-aG", groupname, username])

def main(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row['username']
            groups = row['groups'].split(':')

            # Add user if not exists
            if subprocess.call(["id", username], stdout=subprocess.PIPE, stderr=subprocess.PIPE) != 0:
                add_user(username)
            
            # Add groups if not exist
            for group in groups:
                if subprocess.call(["getent", "group", group], stdout=subprocess.PIPE, stderr=subprocess.PIPE) != 0:
                    add_group(group)
            
            # Add user to groups if not already a member
            for group in groups:
                current_groups = subprocess.getoutput(f"id -nG {username}").split()
                if group not in current_groups:
                    add_user_to_group(username, group)

if __name__ == "__main__":
    csv_file = "user_groups.csv"  # Replace with your CSV file's path
    main(csv_file)

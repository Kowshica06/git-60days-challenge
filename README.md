
# git-60days-challenge
Documenting my 60-day journey to learn and practice Git and GitHub through daily challenges.

Challenge 1: List all files (including hidden ones) in your home directory and sort them by modification time.

Answer:

ls -laht ~
Explanation:

ls → List directory contents
-l → Use a long listing format
-a → Show hidden files (files starting with .)
-h → Display sizes in human-readable format (e.g., KB, MB)
-t → Sort by modification time (newest first)
~ → Home directory

✅ Challenge 2: Create a directory named devops_challenge_day_1, navigate into it, and create an empty file named day1.txt.

Answer:

# Step 1: Create a directory named devops_challenge_day_1
mkdir devops_challenge_day_1

# Step 2: Navigate into the directory
cd devops_challenge_day_1

# Step 3: Create an empty file named day1.txt
touch day1.txt

✅ Challenge 3: Find the total disk usage of the /var/log directory in human-readable format.

Answer:

du -sh /var/log
Explanation:

du → Disk usage command
-s → Summarize total size instead of listing all files
-h → Human-readable format (e.g., KB, MB, GB)

✅ Challenge 4: Create a new user called devops_user and add them to the sudo group.

Answer:

# Step 1: Create a new user called devops_user
sudo adduser devops_user

# Step 2: Add the user to the sudo group
sudo usermod -aG sudo devops_user

# Optional: Verify the user is in the sudo group
getent group sudo
Run the below command to verify it:

id devops_user
Explanation:

sudo useradd -m -s /bin/bash -G sudo devops_user
useradd → Creates a new user.
-m → Creates a home directory for the user.
-s /bin/bash → Sets Bash as the default shell.
-G sudo → Adds the user to the sudo group for administrative privileges.
devops_user → The username being created.
sudo passwd devops_user
Sets a password for devops_user (you’ll be prompted to enter a password).

✅ Challenge 5: Create a group called devops_team and add devops_user to that group.

Answer:

sudo groupadd devops_team

sudo usermod -aG devops_team devops_user
Verify using the below command:

groups devops_user
Explanation:

sudo groupadd devops_team
Creates a new group named devops_team.
sudo usermod -aG devops_team devops_user
Adds devops_user to the devops_team group.
-aG → Appends (-a) the user to the specified group (-G devops_team) without removing them from other groups.

✅ Challenge 6: Change the permissions of day1.txt to allow only the owner to read and write, but no permissions for others.

Answer:

chmod 600 day1.txt
Verify using the command:

ls -l day1.txt
Explanation:

Octal	Symbolic	Description
000	----------	No permissions (no read, write, or execute)
100	--x------	Execute only for owner
200	-w-------	Write only for owner
300	-wx------	Write and execute for owner
400	r--------	Read only for owner
500	r-x------	Read and execute for owner
600	rw-------	Read and write for owner (commonly used for private files)
700	rwx------	Full access for owner
644	rw-r--r--	Read/write for owner, read-only for group and others (text files)
655	rw-r-xr-x	Read/write for owner, read/execute for group and others
660	rw-rw----	Read/write for owner and group, no access for others
664	rw-rw-r--	Read/write for owner and group, read-only for others
666	rw-rw-rw-	Read/write for everyone (not recommended for security reasons)
700	rwx------	Full access for owner (private executables)
744	rwxr--r--	Full access for owner, read-only for group and others
755	rwxr-xr-x	Full access for owner, read/execute for group and others
770	rwxrwx---	Full access for owner and group, no access for others
775	rwxrwxr-x	Full access for owner and group, read/execute for others
777	rwxrwxrwx	Full access for everyone (very insecure, not recommended)
Key Points:

First digit: Owner permissions
Second digit: Group permissions
Third digit: Others' permissions
r (4) = Read permission
w (2) = Write permission
x (1) = Execute permission
Sum of values (rwx = 4+2+1 = 7) = All allowed

✅ Challenge 7: Find all files in /etc that were modified in the last 7 days.

Answer:

find /etc -type f -mtime -7
Explanation:

find → Command to search for files and directories.
/etc → The directory to search in.
-type f → Searches for files only (not directories).
-mtime -7 → Finds files modified in the last 7 days (-7 means less than 7 days old).

✅ Challenge 8: Write a one-liner command to find the most frequently used command in your shell history.

Answer:

history | awk '{CMD[$2]++;} END {for (a in CMD) print CMD[a], a;}' | sort -nr | head -1
Explanation:

history → Lists the command history.
awk '{CMD[$2]++;} END {for (a in CMD) print CMD[a], a;}'
Extracts and counts occurrences of each command.
sort -nr → Sorts the commands by frequency in descending order.
head -1 → Displays the most frequently used command.
>>>>>>> 7e05941 (Initial commit with challenge solutions)
=======
# 💻 DevOps Bash Script Challenges

This repository contains 10 beginner-friendly **DevOps Bash scripting challenges**, each designed to build fundamental Linux scripting and automation skills. Every script is simple, self-contained, and executable on a typical Linux environment.

---

## 📁 Challenge List

| #  | Script Filename             | Description |
|----|-----------------------------|-------------|
| 1  | `01_hello_devops.sh`        | Prints "Hello DevOps" with the current date and time |
| 2  | `02_check_website.sh`       | Checks if a given website is reachable using `curl` |
| 3  | `03_check_file.sh`          | Checks if a filename exists and displays its contents |
| 4  | `04_list_processes.sh`      | Lists all running processes and saves to `process_list.txt` |
| 5  | `05_install_packages.sh`    | Installs `git`, `vim`, `curl` only if not already installed |
| 6  | `06_monitor_system.sh`      | Logs CPU and memory usage every 5 seconds |
| 7  | `07_cleanup_logs.sh`        | Deletes `.log` files older than 7 days from `/var/log` |
| 8  | `08_create_user.sh`         | Creates a new user and adds them to the `devops` group |
| 9  | `09_extract_errors.sh`      | Extracts only lines with the word "error" from a log file |
| 10 | `10_backup_directory.sh`    | Archives a directory and can be scheduled with a cron job |

---

## ✅ How to Run Scripts

Make the script executable:

```bash
chmod +x script_name.sh
>>>>>>> dac4b21 (Add README with all 10 Bash challenges)

Display the name of the current user
```bash
whoami
```

Get basic information about the operating system.
Option `-a` prints all the system information (Kernel name, network node hostname, kernel release date, kernel version, machine hardware name, hardware platform, operating system)
```bash
uname
uname -a
uname -r
```

Obtain the user and group identity information
```bash
id
```

Get available disk space
```bash
df
df -h
```

View currently running processes (owned by current user).
Option `-e` displays all of the processes running on the system(also from other users)
```bash
ps
ps -e
```

Get information on the running processes and system resources
```bash
top
htop
```

Display Messages.
Use the `-e` option of the echo command when working with special characters
```bash
echo "Hello Linux"
echo -e "This will be printed \n in two lines"
```

Display date and time
```bash
date
date "+%D"
```
`%d - Display the day of the month (01 to 31)`

`%h - Displays the abbreviated month name (Jan to Dec)`

`%m - Displays the month of year (01 to 12)`

`%Y - Displays the four-digit year`

`%T - Displays the time in 24 hour format as HH MM SS`

`%H - Displays the hour`

View the Reference Manual For a Command
```bash
man
```

Get the location of the current working directory
```bash
pwd
```

List the files and directories
```bash
ls
ls -<option>
```
options:

`-a	list all files, including hidden files`

`-d	list directories only, do not include files`

`-h	with -l and -s, print sizes like 1K, 234M, 2G`

`-l	include attributes like permissions, owner, size, and last-modified date`

`-S	sort by file size, largest first`

`-t	sort by last-modified date, newest first`

`-r	reverse the sort order`


Create a directory
```bash
mkdir
```

Change current working directory
```bash
cd
```

Create an empty file
```bash
touch filename.txt
```

Search and locate files
```bash
find
find /etc -name '*.txt' 
```

Remove files.
Option `-i` asks for confirmation before every deletion
```bash
rm
rm -i filename.txt
```

Move, Rename a file
```bash
mv
```
Rename file:
```bash
mv users.txt user-info.txt
```

Copy files
```bash
cp
cp /tmp/user-info.txt user-info.txt
cp /etc/passwd users.txt
```

Access control commands:

Permissions set for each file and directory:

```
read        r
write       w
execute     x
```

See permission set for a file:
```bash
ls -l myfile.txt
```

Change permissions
```bash
chmod
```

```
option              description
r w x               permissions: read, write and execute, respectively
u g o               user categories: owner, group and all others, respectively
+ -                 operations: grant and revoke, respectively
```

Remove read permission for all users (user, group and other) on the file: 
```bash
chmod -r testfile.txt
```

Add read access to all users 
```bash
chmod +r testfile.txt                
```

Now verify the changed permissions:
```bash
ls -l testfile.txt
```

Remove the read permission for ‘all other users’ 
```bash
chmod o-r usdoi.txt
```


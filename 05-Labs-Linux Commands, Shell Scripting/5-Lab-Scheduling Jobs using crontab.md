Cron is a system daemon used to execute desired tasks in the background at designated times.
A crontab file is a simple text file containing a list of commands meant to be run at specified times. It is edited using the `crontab` command.
Each line in a crontab file has five time-and-date fields, followed by a command, followed by a newline character (\n). The fields are separated by spaces.
The five time-and-date fields cannot contain spaces and their allowed values are as follows:

```
Field	    Allowed values
minute	    0-59
hour	    0-23, 0 = midnight
day	        1-31
month	    1-12
weekday	    0-6, 0 = Sunday
```

## List cron jobs

```
crontab -l
```

## Add a job in the crontab file

```
crontab -e
```
Scroll down to the end of the file using the arrow keys and add the following line:
```
0 21 * * * echo "Welcome to cron" >> /tmp/echo.txt
```
The above job specifies that the `echo` command should run when the minute is 0 and the hour is 21. 
It effectively means the job runs at 9.00 p.m every day.
The output of the command should be sent to a file `/tmp/echo.txt`


## Schedule a shell script
Create a simple shell script that prints the current time and the current disk usage statistics.

Create a file named `diskusage.sh `
```bash
#! /bin/bash
# print the current date time
date
# print the disk free statistics
df -h
```

Schedule this script to be run everyday at midnight 12:00 (when the hour is 0 on the 24 hour clock).

```
crontab -e
```
Add the following line to the end of the file::

```bash
0 0 * * * /home/project/diskusage.sh >>/home/project/diskusage.log
```

## Remove the current crontab
The `-r` option causes the current crontab to be removed.
```bash
crontab -r
```

Create a cron job that runs the task date >> /tmp/everymin.txt every minute.
```
crontab -e
* * * * * date >> /tmp/everymin.txt
```
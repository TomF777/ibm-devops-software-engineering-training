Display all file contents
```
cat
```

Display file contents page-wise
```bash
more
```

Display first 10 lines of a file
```bash
head filename.txt
```

Display first 3 lines of a file
```bash
head -3 filename.txt
```

Display last 10 lines of a file
```bash
tail filename.txt
```

Display last 2 lines of a file
```bash
tail -2 usdoi.txt
```

Count lines, words or characters in a file:
```bash
wc filename
```

Print only the number of line
```bash
wc -l filename
```

Print only the number of words 
```bash
wc -w filename
```

Print only the number of characters 
```bash
wc -c filename
```

View sorted file lines
```bash
sort filename
sort -r usdoi.txt       #reverse-sorted
```

View the contents of `filename.txt` with equal and consecutive lines merged into one

```bash
uniq filename.txt
```

Extract lines matching specified criteria (word)
```bash
grep word filename
```
Options for `grep`:

`-n             Along with the matching lines, also print the line numbers`

`-c             Get the count of matching lines`

`-i             Ignore the case of the text while matching`

`-v             Print all lines which do not contain the pattern`

`-w             Match only if the pattern matches whole words`

<br>

View lines of file with filter applied to each line.
Option `-c -2` to view first two character of each line.
Option `-c 2-` for each line starting from second character.
```bash
cut
cut -c -2 filename
cut -c 2- filename
```

<br>

View multiple files side by side.
Option `-d ","` to customize the delimiter (defautl `tab`)
```bash
paste file1 file2
paste -d "," zoo.txt zoo_ages.txt
```

<br>

Create and manage file archives

Pack multiple files and directories into a single archive file:

```bash
tar
```
Options for `tar`:

`-c             Create new archive file`

`-v             Verbosely list files processed`

`-f             Archive file name`


```bash
tar -cvf bin.tar /bin
```

To see the list of files in the archive, use the `-t` option
```bash
tar -tvf bin.tar
```

To untar the archive or extract files from the archive, use the `-x` option:

```bash
tar -xvf bin.tar
```

<br>
Package and compress archive files

Compress file. Option `-r` to zip an entire directory:
```bash
zip
zip config.zip /etc/*.conf
zip -r bin.zip /bin
```

<br>
Extract, list, or test compressed files in a ZIP archive

Option `-l` to list the files of the archive

Option `-o` to extract all files in the archive
```bash
unzip
unzip -l config.zip
unzip -o bin.zip
```

<br>
Networking commands

To view the current host name.
Option `-i` to view the IP of the host
```bash
hostname
hostname -i
```

Test if a host is reachable.
Option `-c` to limit the number of times

```bash
ping
ping -c 5 www.google.com
```

Display network interface configuration

```bash
ifconfig
```

Display the configuration of an ethernet adapter eth0:

```bash
ifconfoig eth0
```

<br>
Transfer data from or to a server
Access the file at the given URL and display the file’s contents

```bash
curl
curl https://url_path_to_file
```

Access the file at the given URL and save it in current working directory:

```bash
curl -O https://url_path_to_file
```

<br>

Downloading file(s) from a URL
```bash
wget https://url_path_to_file
```

bash script `greet.sh`

```bash
echo -n "enter your name"
read name
echo "hello $name"
```

run the script from command line:

```
bash greet.sh
```

Find the path to interpreter:
```bash
which bash
```

Adding `shebang` line lets you specify the path to the interpreter of the script, which is the Bash Shell in this case.
```bash
#! /bin/bash
echo -n "enter your name"
read name
echo "hello $name"
```

Add execute permission:
```bash
chmod +x greet.sh
chmod u+x greet.sh
```

Execute the script
```bash
./greet.sh
```

Create `greetnew.sh`
```bash
#! /bin/bash
page{title="This script accepts the user's name and prints"}
## a message greeting the user
::page{title="Print the prompt message on screen"}
echo -n "Enter your firstname :"	  	
::page{title="Wait for user to enter a name, and save the entered name into the variable 'name'"}
read firstname
::page{title="Print the prompt message on screen"}
echo -n "Enter your lastname :"	  	
::page{title="Wait for user to enter a name, and save the entered name into the variable 'name'"}
read lastname	
::page{title="Print the welcome message followed by the name"}
echo "Hello $firstname $lastname."
```






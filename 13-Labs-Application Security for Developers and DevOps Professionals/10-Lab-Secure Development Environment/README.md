Simple steps you can use to secure your development environment against risk:

- Securely storing secrets required for your production application.
- Secure the internet connection. Use a VPN, if necessary.
- Implement a firewall with strong ingress/egress policies.
- Regularly check for open ports and closing ports not needed.
- Use Docker containers for development, if possible, and use separate computers for development tasks and business tasks.
- Logging the behaviors in your developer's environments.
- Use multifactor authentication to prevent identity theft.
- Add additional security for developers who need to access the production environment from their developer machines.
- Track all commits and changes made by developers, for future reference, in case problems arise.

See `insecure.txt`. The file is storing important secrets in plain text. This is certainly not a desirable situation.

## Securing the secrets using pass
```
sudo apt update
sudo apt install -y pass
```

Use the `gpg` command to generate a secret GPG key on your local machine
```
gpg --full-generate-key
```

Follow all of the installation prompts until the installation and configuration process is complete. Press `[enter]` to accept the default options for the key type, and the other remaining settings. Then press `y` to confirm.

Then enter a passphrase(password) which is recommended to have at least 8 characters and contain at least 1 digit or special character.

With this, your GPG key will be generated.

## Initializing Pass
After the GPG key was genereted, you can initilize `pass` with GPG ID.

Use the ID of the GPG key created in previous step:
```
gpg --list-secret-keys --keyid-format LONG | grep sec
```


In the resulting output this line contains the GPG key ID:
```
sec   rsa3072/B804AA08E31EB362 2025-07-07 [SC]
```
In this example the GPG key ID is `B804AA08E31EB362`

Copy the key's ID to the clipboard and init the pass:

```
pass init <insert gpg key>
```

## Creating secrets
Now you can create secrets and store them securely.

Run command to obtain the value for the key `IBM_CLOUD_API_KEY` from the `./insecure.txt` file:
```
cat ./insecure.txt| grep IBM_CLOUD_API_KEY | grep -o "\".*" | grep -o "[a-z,A-Z,0-9]*"
```

Create a new secret called `IBM_CLOUD_API_KEY` in `pass`:
```
pass insert IBM_CLOUD_API_KEY
```
Then copy and paste the value for `IBM_CLOUD_API_KEY` obtained with `cat` command before.

This way it's possible to create and insert multiple secrets into `pass`.

## Retrieving secrets

```
pass show IBM_CLOUD_API_KEY
pass show [SECRET_KEY_NAME]
```
You may be asked to enter your master password (GPG key). 
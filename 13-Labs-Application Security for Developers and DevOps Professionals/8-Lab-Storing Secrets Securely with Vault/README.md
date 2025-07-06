Secrets should be stored securely to protect private data and prevent people from gaining unauthorized access to your application(s). 
`Vault` is a token-based storage solution for managing secrets. There are four stages of security for Vault:
- Authentication
- Validation
- Authorization
- Access

## Install Vault
```
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg >/dev/null
```

```
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
```

```
sudo apt update
sudo apt install vault
```

Verify that it was installed properly by running the `vault` command.
This should show a list of commands you can use with the tool.


## Setting up the Dev Server

Use the `vault server` command with the `-dev` flag to run the vault server in development mode:
```
vault server -dev
```

At the end of the output, you should see a warning message and `Unseal Key` and `Root Token`. Copy it inot safe place.

Next, open a new terminal and run the following shell command to specify port 8200 for Vault:
```
export VAULT_ADDR='http://127.0.0.1:8200'
```

`Unseal Key` and `Root Token` are used to authenticate the user - the first step of security in Vault. The root token is regenerated every time you start the server, so be sure to edit and run the statement below according to the most updated root token displayed on your terminal:
```
export VAULT_TOKEN="YOUR ROOT TOKEN HERE"
```

## Check the Server

Use the `vault status` command to check that the server is running:
```
vault status
```

The output should look something like this:


|Key           | Value         | 
|--------------|---------------|
|Seal Type     | shamir        |
|Initialized   | true          |
|Sealed        | false         |
|Total Shares  | 1              |
|Threshold     | 1              |
|Version       | 1.20.0         |
|Build Date    | 2025-06-23T10:21:30Z   |
|Storage Type  | inmem                  |
|Cluster Name  | vault-cluster-389df63a |
|Cluster ID    | a0854cd2-769c-87f5-4ce2-97d47d8149b7   |
|HA Enabled    | false  |


## Access the Vault UI

```
http://localhost:8200
```

You will be presented with a logon page. From here, you can input the root token that you copied to the `VAULT_TOKEN` environment variable to login.
You can display your token from a terminal with:
```
echo $VAULT_TOKEN
```

Once you are logged in, you can access secrets stored in  by clicking the `secret/` in tab `Dashboard`


## Installing HVAC

By default, Vault’s dev server includes `KV v2 Secrets Engines` at the path secret/, storing secrets within its configured physical storage. Secrets are encrypted before writing to backend storage, so it can never decrypt these values without Vault.

```
python3 -m pip install hvac
```


## Write Secret to Vault
Use Python file `read_write_vault.py` that will be used to write, read and delete secrets from Vault.

```
python3 read_write_vault.py write_secret myapp user_tom mypassword
```

## Double-check Written Secret

Ppen up the `Vault UI` to double-check that the secret is stored in the right place.
Click the `secret/` link. This will show all secrets.

Then click `myapp/` link. This will show secrets under myapp.


## Read Secret from Vault

```
python3 read_write_vault.py read_secret myapp
```
The output returns information about all the data stored under `secret/myapp`. Notice, you can see the key/value pair you just wrote.


## Delete Secret from Vault

```
python3 read_write_vault.py delete_secret myapp
```

## Double-check Deleted Secret

Check the Vault UI. Revisiting the Vault UI, you can see this change reflected, too.









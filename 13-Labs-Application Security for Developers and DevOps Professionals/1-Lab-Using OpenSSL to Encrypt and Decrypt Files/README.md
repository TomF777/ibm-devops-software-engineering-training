## Decrypting a simple file

See `encrypted_secretfile`. 
You will see that the content is not readable, and is all encrypted.
This has been encoded using `aes-256-cbc` cipher.
Each cipher has its own algorithm.
`aes-256-cbc` is one of the older and simpler ciphers, and there are now much better algorithms to encrypt the data.

Run the command to decrypt the file.
```
openssl aes-256-cbc -d -a -pbkdf2 -in encrypted_secretfile -out secrets.txt
```

| Command option           | Meaning                                      |
| -------------------------| -------------------------------------------- |
| aes-256-cbc              | The cipher algorithm                         |
| -d                       | Decrypt                                      |
| -a                       | Base64 decode                                |
| -pbkdf2                  | Use password-based key derivation function 2 |
| -in encrypted_secretfile | Input file                                   |


The file has been encrypted with the password `adios`

## Encrypt the file
Make changes, as you require, to the `secret.txt` file and encrypt it with a new password. It will prompt you to enter and renter the same password to verify. Make sure you remember the password.

```
openssl aes-256-cbc -a -pbkdf2 -in secrets.txt -out secrets.txt.enc
```

## Changing the decrypt options
To encrypt the file in a manner that is not easily decryptable, we can also set the iterations to higher numbers. Many iterations increase the time required to brute-force the encrypted file.
```
openssl aes-256-cbc -a -pbkdf2 -iter 2500 -in secrets.txt -out secrets.txt.enc
```
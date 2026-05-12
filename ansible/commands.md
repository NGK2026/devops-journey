#### Generate SSH key /w comment and passphrase
```sh
ssh-keygen -t ed25519 -C "default"
# Enter passphrase: ******
```
#### copy key to server
```sh
# -i (input file), to example IP
ssh-copy-id -i ~/.ssh/id_ed25519.pub 172.16.250.133
```
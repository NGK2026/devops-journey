#### Generate SSH key /w comment and passphrase
```sh
ssh-keygen -t ed25519 -C "default"
# Enter passphrase: ******
```
#### copy key to server
```sh
# -i (input file)
ssh-copy-id -i ~/.ssh/id_ed25519.pub
```
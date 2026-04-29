## EC2 instance - Setup
```sh
# install git
sudo dnf install git

# clone website repo
git clone https://github.com/NGK2026/onyxcore-website.git
cd onyxcore-website

# set AWS S3 variables
aws configure
#AWS Access Key ID [None]: 
AK--snip--N3
#AWS Secret Access Key [None]: 
Mx+--snip--hcRv
#Default region name [None]: 
us-east-1
#Default output format [None]: 
press 'enter' for default json

# upload html files 
aws s3 sync . s3://onyx-core-system/ --exclude "README.md" --exclude ".git/*"
```
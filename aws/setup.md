##### NB. The following steps were created with IAM User account

## Create EC2 instance - (Virtual Servers in the Cloud)
1. AWS *Dashboard*
2. View all services
3. **EC2**
4. **Launch instance**
5. Launch without walkthrough
6. Enter instance *Name*
7. Select Application and OS Image: default **'Amazon Linux'** - *(Free tier eligible)*
8. Instance type: default **'t3.micro'** - *(Free tier eligible)*
9. Key pair: select *Proceed without a key pair (Not recommended)*
10. Keep everything else *Default*
11. **Launch instance**
12. Click on instance *link*
13. Find *Security* tab and open it
14. Click *Security groups*: **launch-wizard-1**
15. To create new rule for inbound *HTTP* traffic, click **Edit inbound rules**
16. **Add rule**
17. Enter *port range*: **8080** 
18. Select *Source*: **Anywhere-IPv4**, will create *IP* **0.0.0.0/0**
19. **Save rules**

## Create S3 - (Scalable Storage in the Cloud)
1. AWS *Dashboard*
2. View all services
3. **S3**
4. **Create bucket**
5. Keep *default*
6. Enter *Bucket name*
7. Uncheck *Block all public access* - Check *"I Aknowledge ...."*
8. **Tags**: Help organize for grouping and searching between projects with same **tags**
9. Add 2 tags: 
- (Key: application, Value: onyxcoresystem)
- (Key: environment, Value: service)
10. Everything else leave as *default*
11. **Create bucket**
12. Open bucket > Open *Permissions* tab > *Bucket policy* > Click **Edit**
13. To allow *read* public access, add:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::onyx-core-system/*"
    }
  ]
}
```
14. **Save changes**

## Create Access Key (For instance permission to connect to bucket)
1. Click *Account menu* (username) at top right of page
2. Select **Security credentials**
3. *Access keys* section > **Create access key**
4. Select *Application running on an AWS compute service*
5. Check *"I understand the above recommendation ..."*
6. **Next**
7. Enter *Description tag value - Optional*
8. **Create access key** 
9. Copy / Save *Access key & Secret access key* somewhere safe, or *download .csv*
10. **Done**

### Skip RDS Database *for now*

## Connect to EC2 instance
1. AWS *Dashboard*
2. View all services
3. **EC2**
4. **View dashboard**
5. **Instances (running)**
6. Select instance and click **Connect**
7. **Connect** again
8. *Terminal* launches in new web browser tab

## Static website hosting
1. AWS *Dashboard*
2. View all services
3. **S3**
4. Click to open bucket
5. Navigate to *Properties*
6. Scroll to *Static website hosting*
7. **Edit** > *Enable*
8. Set *Index document* to homepage .html file
9. **Save changes**
10. Scroll to bottom of *Properties* tab again
11. Use *Bucket website endpoint*
12. http://onyx-core-system.s3-website-us-east-1.amazonaws.com/


## Create EC2 instance - (Virtual Servers in the Cloud)
1. AWS *Dashboard*
2. View all services
3. **EC2**
4. *Launch* instance
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

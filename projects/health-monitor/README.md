## Health Monitor App
. Monitor's the system's CPU, Memory & Disk usage % using a Python app.
. The App is located inside a Docker container, deploying a Python Flask server.

#### How to use
1. Pull the files and app folder
2. Run 
```sh
╰─❯ docker-compose up

╰─❯ curl http://localhost:5000/metrics
{"CPU":1.0,"Home":45.4,"RAM":18.8,"Root":45.4}

```

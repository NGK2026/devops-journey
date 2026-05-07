# uses HTTP to return system metrics gathered by process utility library
from flask import Flask, jsonify
import psutil as ps
import prometheus_client as pc

app = Flask(__name__)

# define gauge
cpu_gauge = pc.Gauge('cpu_percent', 'Current CPU percent')
mem_gauge = pc.Gauge('mem_percent', 'Current RAM percent')
root_gauge = pc.Gauge('root_percent', 'Current Root percent')
home_gauge = pc.Gauge('home_percent', 'Current Home percent')

@app.route('/metrics')
def metrics():
    # variables storing metrics:
    # CPU, RAM, DISK (ROOT, HOME)
    # cpuPercent = ps.cpu_percent(interval=1)
    # memCurr = ps.virtual_memory().percent
    # rootDiskCurr = ps.disk_usage('/').percent
    # homeDiskCurr = ps.disk_usage('/home').percent
    
    # set gauge
    cpu_gauge.set(ps.cpu_percent(interval=1))
    mem_gauge.set(ps.virtual_memory().percent)
    root_gauge.set(ps.disk_usage('/').percent)
    home_gauge.set(ps.disk_usage('/home').percent)

    # Store data in dictionary
    # data = {
    #     'CPU': cpuPercent,
    #     'RAM': memCurr,
    #     'Root': rootDiskCurr,
    #     'Home': homeDiskCurr
    # }
    # return latest gauge           # return data as JSON
    return pc.generate_latest()     # jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
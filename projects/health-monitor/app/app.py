# uses HTTP to return system metrics gathered by process utility library
from flask import Flask, jsonify
import psutil as ps

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    # variables storing metrics:
    # CPU, RAM, DISK (ROOT, HOME)
    cpuPercent = ps.cpu_percent(interval=1)
    memCurr = ps.virtual_memory().percent
    rootDiskCurr = ps.disk_usage('/').percent
    homeDiskCurr = ps.disk_usage('/home').percent

    # Store data in dictionary
    data = {
        'CPU': cpuPercent,
        'RAM': memCurr,
        'Root': rootDiskCurr,
        'Home': homeDiskCurr
    }
    # return data as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
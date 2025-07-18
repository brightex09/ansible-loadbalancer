from flask import Flask, render_template
import socket
import requests

app = Flask(__name__)

# List of upstream servers (VMs or containers)
upstream_servers = [
    "172.31.29.44",
    "172.31.23.244",
    "172.31.83.250",
    "172.31.94.107",
    "172.31.84.240"
]

# Check if the server is healthy by calling its /health endpoint
def check_server(ip):
    try:
        res = requests.get(f"http://{ip}:5000/health", timeout=1)
        return res.status_code == 200
    except requests.exceptions.RequestException:
        return False

@app.route('/')
def home():
    hostname = socket.gethostname().upper()
    healthy = []
    unhealthy = []

    for ip in upstream_servers:
        if check_server(ip):
            healthy.append(ip)
        else:
            unhealthy.append(ip)

    return render_template("index.html", hostname=hostname, healthy=healthy, unhealthy=unhealthy)

# Simple health check for this Flask app
@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


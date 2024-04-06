from flask import Flask, render_template, request
import socket
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/host_details')
def host_details():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return render_template('host_details.html', hostname=hostname, local_ip=local_ip)

@app.route('/speed_test')
def speed_test():
    return render_template('speed_test.html')

@app.route('/run_speedtest', methods=['POST'])
def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping
    return render_template('speedtest_result.html', download_speed=download_speed, upload_speed=upload_speed, ping=ping)

@app.route('/scan_ports', methods=['GET', 'POST'])
def scan_ports():
    if request.method == 'POST':
        ip_address = request.form['ip_address']
        port_range_choice = request.form['port_range_choice']
        
        if port_range_choice == 'common':
            start_port, end_port = 21, 995
        elif port_range_choice == 'reserved':
            start_port, end_port = 0, 1023
        elif port_range_choice == 'all':
            start_port, end_port = 1, 65535
        else:
            start_port = int(request.form['start_port'])
            end_port = int(request.form['end_port'])
        
        open_ports = scan_ports_helper(ip_address, start_port, end_port)
        
        if not open_ports:
            message = "No open ports found in the specified range."
            return render_template('scan_results.html', ip_address=ip_address, message=message)
        else:
            return render_template('scan_results.html', ip_address=ip_address, open_ports=open_ports)
    else:
        return render_template('scan_form.html')

def scan_ports_helper(ip_address, start_port, end_port):
    open_ports = []
    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            s.close()
    except Exception as e:
        print("An error occurred:", e)
    return open_ports

if __name__ == '__main__':
    app.run(debug=True)

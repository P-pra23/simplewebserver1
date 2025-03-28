# EX01 Developing a Simple Webserver
## Date:25/03/2025
## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html>
<body>
<h1>
24007902
</h1>
<ol>
<li>IP (Internet Protocol) – Defines addressing and routing.</li>
<li>TCP (Transmission Control Protocol) – Ensures reliable data delivery.</li>
<li>UDP (User Datagram Protocol) – Used for fast, unreliable data transfer.</li>
<li>HTTP/HTTPS – Used for web browsing.</li>
<li>FTP (File Transfer Protocol) – Transfers files between devices.</li>
<li>SMTP/POP3/IMAP – Email communication protocols.</li>
<li>DNS (Domain Name System) – Converts domain names to IP addresses.</li>
</ol>
</body>	
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2025-03-25 144254.png>)
![alt text](<Screenshot 2025-03-25 144404.png>)
![alt text](<Screenshot 2025-03-25 144436.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

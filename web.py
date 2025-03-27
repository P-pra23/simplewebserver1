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
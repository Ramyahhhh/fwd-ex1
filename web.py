from http.server import HTTPServer, BaseHTTPRequestHandler
content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TCP/IP Protocols</title>
</head>
<body>
  <h1>Protocols in the TCP/IP Model</h1>

  <h2>Application Layer</h2>
  <ul>
    <li>HTTP / HTTPS</li>
    <li>FTP / SFTP</li>
    <li>SMTP / POP3 / IMAP</li>
    <li>DNS</li>
    <li>DHCP</li>
    <li>SSH / Telnet</li>
    <li>SNMP</li>
  </ul>

  <h2>Transport Layer</h2>
  <ul>
    <li>TCP</li>
    <li>UDP</li>
  </ul>

  <h2>Internet Layer</h2>
  <ul>
    <li>IP (IPv4 / IPv6)</li>
    <li>ICMP</li>
    <li>ARP</li>
    <li>IGMP</li>
    <li>IPsec</li>
  </ul>

  <h2>Network Access (Link) Layer</h2>
  <ul>
    <li>Ethernet</li>
    <li>Wi-Fi (IEEE 802.11)</li>
    <li>PPP</li>
    <li>Frame Relay</li>
  </ul>
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
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
    <title>Pc Spec</title>
</head>
<body>

    <p><b>Name:</b> Tharun</p>
    <p><b>Ref No:</b> 26016280</p>

    <table border="1" cellspacing="5" cellpadding="5">
        <caption>My Device Specification</caption>

        <tr>
            <th>Sno</th>
            <th>Device info</th>
            <th>Device spec</th>
        </tr>

        <tr>
            <td>1</td>
            <td>Device Name</td>
            <td>TL15-53M-G2</td>
        </tr>

        <tr>
            <td>2</td>
            <td>Processor</td>
            <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
        </tr>

        <tr>
            <td>3</td>
            <td>Installed Ram</td>
            <td>16GB</td>
        </tr>

        <tr>
            <td>4</td>
            <td>Graphics Card</td>
            <td>Intel(R) Graphics (128 MB)</td>
        </tr>

        <tr>
            <td>5</td>
            <td>Storage</td>
            <td>119 GB of 477 GB used</td>
        </tr>

    </table>

</body>
</html>
        

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()
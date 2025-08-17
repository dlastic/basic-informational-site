from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        routes = {
            "/": "index.html",
            "/about": "about.html",
            "/contact-me": "contact-me.html",
        }

        filename = routes.get(self.path, "404.html")
        if filename == "404.html":
            self.send_response(404)
        else:
            self.send_response(200)

        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open(filename, "rb") as f:
            self.wfile.write(f.read())

        print("Served: ", filename)


server_address = ("", 8080)
httpd = HTTPServer(server_address, MyHandler)

print("Server running on http://localhost:8080")
httpd.serve_forever()

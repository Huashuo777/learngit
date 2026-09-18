from http.server import BaseHTTPRequestHandler, HTTPServer
import json

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.headers)         # 收到的请求头
        print(self.client_address)  # 请求的地址来源
        if self.path == '/api/profile':
            self.send_response(200)
            self.send_header("Content-Type", "application/json") # text/html 就当网页渲染，application/json 就当数据处理
            self.end_headers()
            body = json.dumps(profile, ensure_ascii=False)
            self.wfile.write(body.encode("utf-8"))
        elif self.path == "/hello":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8") # 头是关于内容的说明
            self.end_headers()
            self.wfile.write("<h1>你好，HTTP</h1>".encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

print("后端已启动：http://localhost:8000/api/profile")
HTTPServer(("", 8000), Handler).serve_forever()
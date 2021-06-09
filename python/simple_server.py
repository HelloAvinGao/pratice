from http.server import HTTPServer, CGIHTTPRequestHandler
 
# 端口
port = 9000
# 允许任何设备都可访问该服务器，访问方式为http请求
server = HTTPServer(('', port), CGIHTTPRequestHandler)
 
print('Starting simple httpd on port: ' + str(server.server_port))
# 启动服务器
server.serve_forever()

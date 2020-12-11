import http.client

import msgpack

HOST = "192.168.1.164"
PORT = "55553"

headers = {"Content-type": "binary/message-pack"}

# 连接MSF RPC Socket
req = http.client.HTTPConnection(HOST, PORT)
options = ["auth.login", "msf", "rpcdadmin"]
# options = ["group.command", "msf", "rpcdadmin"]

# 对参数进行序列化（编码）
options = msgpack.packb(options)

# 发送请求，序列化之后的数据包
req.request("POST", "/api/1.0", body=options, headers=headers)

# 获取返回
res = req.getresponse().read()

# 对返回进行反序列户（解码）
res = msgpack.unpackb(res)
# res = res['token'].decode()
print(res)

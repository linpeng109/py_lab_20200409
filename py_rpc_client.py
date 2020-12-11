import xmlrpc.client

client = xmlrpc.client.ServerProxy('http://192.168.1.164:55553')
exploit = client.modules.use('unix/ftp/vsftpd_234_backdoor')
# print(exploit.description)
print(exploit)


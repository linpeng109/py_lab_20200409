from pymetasploit3.msfrpc import MsfRpcClient

# 配置rpc的用户名和密码
client = MsfRpcClient(server='192.168.124.12', username='msf', password='rpcdadmin')
exploit = client.modules.use(mtype='auxiliary', mname='scanner/discovery/arp_sweep')
exploit['RHOSTS'] = '192.168.124.7'
client.modules.exploits

#
# exsploit = client.modules.use('auxiliary', 'scanner/discovery/arp_sweep')

# console_id = client.consoles.console().cid
# client.consoles.console(console_id).write('use auxiliary/scanner/discovery/arp_sweep')
# client.consoles.console(console_id).write('set RHOSTS 192.168.124.7')
# client.consoles.console(console_id).write('run')
#
# result = client.consoles.console(console_id).read()
# result = client.consoles.console(console_id).is_busy()

# print(result)

from xmlrpc.server import SimpleXMLRPCRequestHandler,DocXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2')


with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()


    @server.register_function(name='add')
    def adder_function(x, y):
        return x + y


    @server.register_function
    class MyFuncs:
        def mul(self, x, y):
            return x * y


    server.serve_forever()

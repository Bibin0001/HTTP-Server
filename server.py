import socket
from match_strings import match_header_content, match_header_expect, match_header_path_and_method
from parsing_handler import ParserHandler
from response_handler import ResponseHandler
from request_handler import RequestHandler
from http_parameters import SUPPORTED_METHODS

CHUNK_SIZE = 4096

class HTTPServer:
    def __init__(self, port):
        self.port = port
        self.host = "0.0.0.0"
        self.parser = None
        self.responder = None
        self.requester = None

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen()
        print(f'[*] Server started listening on 0.0.0.0:{self.port}')

        while True:
            client, address = server.accept()
            self.client_handler(client)

    def ninja_assemble(self, client_socket):
        self.parser = ParserHandler()
        self.responder = ResponseHandler(client_socket)
        self.requester = RequestHandler()
        print('Ninjas assemble !')

        

    def client_handler(self, client_socket):
        self.ninja_assemble(client_socket)
            
        request = client_socket.recv(CHUNK_SIZE)

        header, body = self.parser.get_header_and_body(request)
        parsed_request = self.parser.parse_request(request)

        method, path = parsed_request[0], parsed_request[1]

        if method not in SUPPORTED_METHODS:
            response = self.responder.create_response(501)
            self.responder.send_response(response)

        big_boi_data = False

        if method == 'POST':
            content_length = parsed_request[2]
            content_type = parsed_request[3]

            request_length = 0

            if parsed_request[-2]:
                response = self.responder.create_response(100)
                self.responder.send_response(response)
                whole_body = self.handle_big_request(content_length, body, client_socket)
                if not whole_body:
                    print('[-] Did not receive the full request :( ')
                    return 0 
                big_boi_data = True

                print("[*] Uploading a fat boi . . . ")

            elif parsed_request[-2] == 'Big boi data':
                self.responder.send_response(response)
                whole_body = self.handle_big_request(content_length, body, client_socket)
                if not whole_body:
                    print('[-] Did not receive the full request :( ')
                    return 0 

                big_boi_data = True

                print("[*] Uploading a fat boi . . . ")


        if big_boi_data: 
            request_data = [whole_body, parsed_request]
        else:
            request_data = [body, parsed_request]
        

        status = self.requester.handle_request(*request_data) # -> status_code, content-type, content-length, body
        print('THis is da status')
        print(status)

        generated_response = self.responder.create_response(*status)
        if generated_response:
            self.responder.send_response(generated_response)
        
        print(f"[*] Response sent: {generated_response}")


    def handle_big_request(self, content_length, body_part, client_socket):

        while content_length > len(body_part):
                remaining_bytes = content_length - len(body_part)
                chunk_size = min(262144, remaining_bytes) # Big chunks for big bois
                chunk = client_socket.recv(chunk_size)
                if not chunk:
                    break
                body_part += chunk
            
        if len(body_part) < content_length:
            print('Did not get the full reuqest')
            return False

        return body_part


'''
PORT = int(input("Select port to use: "))
server = HTTPServer(PORT)
server.start_server()
'''
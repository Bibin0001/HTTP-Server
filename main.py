import socket
from match_strings import match_header_content, match_header_expect, match_header_path_and_method
from parsing_handler import ParserHandler
from response_handler import ResponseHandler
from request_handler import RequestHandler
from http_parameters import SUPPORTED_METHODS
from server import HTTPServer
    

def main():

        server_port = int(input('Select a port to use .. :'))


        http_server = HTTPServer(server_port)
        http_server.start_server()


if __name__ == "__main__":
    main()



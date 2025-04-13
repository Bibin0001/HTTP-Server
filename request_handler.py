from parsing_handler import ParserHandler
from system_handler import SystemHandler
import re

class RequestHandler:
    def __init__(self):
        self.parser = ParserHandler()
        self.system = SystemHandler()

    def handle_request(self, *args):
        print('Got da request')

        http_method = args[1][0]
        print(f"[*] Handling HTTP Method: {http_method}")

        if http_method == 'POST':
            status = self.handle_POST(*args)
            return status

        if http_method == 'GET':
            status = self.handle_GET(*args)
            return status
        




    def handle_GET(self, *args):
        print('These are for get request')

        path = args[1][-1]
        print(path)
        filename = path.split('/')[-1]
        print(filename)
        file_extension = path.split(".")[-1]
        print(file_extension)

        file_to_get = self.system.get_file(path, filename, file_extension)
        return file_to_get

    def handle_POST(self, *args):
        print(args) 
        body = args[0]
        boundary = args[1][-1]

        print(boundary)
        filename, content = self.parser.extract_filename_and_file_content(body, boundary)

        print("Got em filez")
        print("[*] Uploading to server")

        uploaded = self.system.upload_file(filename, content)

        print(f"[*] Uploaded: {uploaded}")

        return uploaded # -> status_code, content-type, content-length, body


        # Need to return status code and content-type, content-length



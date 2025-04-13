import re
from http_parameters import SUPPORTED_METHODS

CHUNK_SIZE = 4096

class ParserHandler:

    def parse_request(self, request):
        header_part, body_part = self.get_header_and_body(request)
        decoded_header = self.decode_header(header_part)

        header_info = self.get_headers_information(decoded_header)

        if not header_info:
            return False

        method, path = header_info[0], header_info[1]        

        needed_info = header_info
        print("SEEING HEADERS")
        print(needed_info)

        if method == 'POST':
            content_length = header_info[2]
            content_type = header_info[3]
            expect = header_info[4]
            boundary = header_info[-1]

            if content_length > CHUNK_SIZE and not expect:

                # If i inoly give out as args i think it would be cleaner

                return [method, path, content_length, content_type,'Big boi data', boundary]

            return [method, path, content_length, content_type, expect, boundary]

        return [method, path]
            



    def get_header_and_body(self, request):
        header_part, body_part = request.split(b"\r\n\r\n", 1)
        return [header_part, body_part]


    def get_headers_information(self, decoded_header):
        method_and_path = self.match_header_path_and_method(decoded_header)

        if not method_and_path:
            return False

        method = method_and_path[0] 
        path = method_and_path[1]

        if method not in SUPPORTED_METHODS:
            return False

        if method == 'GET': # Finding the filename should be here
            return [method, path]        
        
        content_length_and_type = self.match_header_content(decoded_header)

        if not content_length_and_type:
            return False
        
        content_length = int(content_length_and_type[0])
        content_type = content_length_and_type[1]
        boundary = self.match_header_boundary(decoded_header)
        
        check_for_expect = self.match_header_expect(decoded_header)

        if check_for_expect:
            return [method, path, content_length, content_type, True, boundary]

        return [method, path, content_length, content_type, False, boundary]
        

    def decode_header(self, header):
        decoded_header = header.decode('utf-8')
        return decoded_header


    def match_header_path_and_method(self, header):
        match = re.match(r"^(\w+)\s+(\S+)", header)

        if match:
            method, path = match.groups()

            return [method, path]

        else:
            return False

    def match_header_content(self, header):
        content_length_match = re.search(r"Content-Length:\s*([^;\r\n]+)", header)
        content_type_match = re.search(r"Content-Type:\s*([^;\r\n]+)", header)

        if content_length_match and content_type_match:
            content_length = content_length_match.group(1)
            content_type = content_type_match.group(1)

            return [content_length, content_type]
        else:
            return False

    def match_header_boundary(self, header):
        content_boundary_match = re.search(r"--[a-zA-Z0-9]+", header)
        if content_boundary_match:
            boundary = content_boundary_match.group()
            return boundary
        

    def match_header_expect(self, header):
        match = re.search(r"Expect:\s*([^;\r\n]+)", header)
        if match:
            continue_code = match.group(1)
            return continue_code
        else:
            return False


    def extract_filename(self, body):
        match = re.search(r'Content-Disposition: form-data; name="file"; filename="([^"]+)"', body.decode('utf-8', errors='ignore'))
        if match:
            return match.group(1)  
        return None


    def extract_filename_and_file_content(self, body, boundary):
        boundary_line = '--' + boundary
        end_boundary_line = boundary_line.encode() + b'--'

        parts = body.split(boundary_line.encode())
        for part in parts:
            part = part.strip()

            if not part or part.startswith(b'--'):
                continue

            headers_raw, sep, content = part.partition(b'\r\n\r\n')
            if not sep:
                continue  

            filename_match = re.search(rb'filename="([^"]+)"', headers_raw)
            if not filename_match:
                continue  

            filename = filename_match.group(1).decode('utf-8', errors='ignore')

        return [filename, content]






'''
 Get file name
        filename_match = re.search(rb'filename="([^"]+)"', body)
        filename = filename_match.group(1).decode() if filename_match else 'unknown'
'''
from http_parameters import RESPONSES

class ResponseHandler:
    def __init__(self, socket):
        self.socket = socket


    def send_response(self, response):
        print(f"[*] Sending response ...")
        self.socket.sendall(response)

        

    def create_response(self, *args): # ->  Inside args: status code, text to create a response

        status_code = args[0]
        args_length= len(args)

        
        print('[*] Creating response')

        if  args_length == 1:
            response_text = RESPONSES[status_code]

            return response_text.encode()

        parameters_for_response = args[1 :-1]
        body = args[-1]

        response_template = RESPONSES[status_code]
        counter = 1
        response_headers =  response_template.format(*parameters_for_response)


        ready_response = response_headers.encode() + body 

        return ready_response

    
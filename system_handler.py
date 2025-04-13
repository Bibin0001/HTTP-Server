import os
from http_parameters import CONTENT_TYPES


class SystemHandler:


# Maybe there is a lfi 

    def check_if_file_exists(self, filename, path):
        #folder = './uploads'
        #print(os.listdir)

        print(f'This is the path {path}')
        print(f'This is the filename {filename}')
        if filename in os.listdir(path):
            print(f'{filename} already exists :3')
            return True
        
        print(f"{filename} doesn't exist :>")
        return False
            


    def get_file(self, file_path, file_name, file_extension):
        print(f"THIS IS THE FILEPATH: {file_path}")

        try:

            folder = './download' + file_path.replace(file_name, "")
            file_contents = self.read_file(folder, file_name)
        except:
            print('File not found')

        #if not file_contents:
            return [404]

        if file_extension not in CONTENT_TYPES.keys(): 
            file_content_type = 'default'
        else:
            file_content_type = CONTENT_TYPES[file_extension]

        file_length = len(file_contents)

        return [200, file_content_type, file_length, file_contents]
        
        



    def read_file(self, file_path, file_name):
        file_exists = self.check_if_file_exists(file_name, file_path)

        if file_exists == False:
            return False

        file_location = file_path + '/' + file_name
        with open(file_location, 'rb') as file:
            print('[+] Reading file :3')
            file_contents = file.read()

            return file_contents
        

        

    def write_file(self, file_path):
        with open(file_path, 'wb') as file:
            file.write(content)
            print('[+] Wrote file to server :3')
            return True
        
        print("[-] Could't write file to server :(")
        return False

        
    def upload_file(self, filename, content):
        print('File content:')
        print(type(content))

        print('[*] Cheking if file exists')
        path = './uploads'
        file = self.check_if_file_exists(filename, path)

        if file:
            fail = f"[-] File: {filename} already exists :("
            print(fail)
            return [409, 'text/plain', len(fail), fail]


        print("[*] Uploading ... ")
        file_written = self.write_file(fullpath)

        if file_written:
            success = f"[*] Uploaded {filename} to server"
            print(success)

            # Send data to create response
            return [201, 'text/plain', len(success), success]
            
        else:
            return [500]


import re

def match_header_path_and_method(header):
    match = re.match(r"^(\w+)\s+(\S+)", header)

    if match:
        method, path = match.groups()

        return [method, path]

    else:
        return False

def match_header_content(header):
    content_length_match = re.search(r"Content-Length:\s*([^;\r\n]+)", header)
    content_type_match = re.search(r"Content-Type:\s*([^;\r\n]+)", header)

    print(f"This is the header: {header}")


    if content_length_match and content_type_match:
        content_length = content_length_match.group(1)
        content_type = content_type_match.group(1)

        return [content_length, content_type]
    else:
        return False

    

def match_header_expect(header):
    match = re.search(r"Expect:\s*([^;\r\n]+)", header)
    if match:
        continue_code = match.group(1)
        return continue_code
    else:
        return False


def extract_filename(body):
    # Search for the Content-Disposition header inside the body part (don't decode the body)
    match = re.search(r'Content-Disposition: form-data; name="file"; filename="([^"]+)"', body.decode('utf-8', errors='ignore'))
    if match:
        return match.group(1)  # The filename part
    return None
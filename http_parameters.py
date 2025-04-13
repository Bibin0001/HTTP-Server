SUPPORTED_METHODS = ['GET', 'POST']

RESPONSES = {
    100: "HTTP/1.1 100 Continue\r\n\r\n",
    200: "HTTP/1.1 200 OK\r\nContent-Type: {0}\r\nContent-Length: {1}\r\n\r\n",
    201: "HTTP/1.1 201 Created\r\nLocation: /\r\nContent-Type: {0}\r\nContent-Length: {1}\r\n\r\n",
    400: "HTTP/1.1 400 Bad Request\r\nContent-Type: {0}\r\nContent-Length: {1}\r\n\r\n",
    403: "HTTP/1.1 403 Forbidden\r\nContent-Type: {0}\r\nContent-Length: {1}\r\n\r\n",
    404: "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n",
    409: "HTTP/1.1 409 Conflict\r\nContent-Type: {0}\r\nContent-Length: {1}\r\n\r\n",
    500: "HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: 82\r\n\r\n<html><body><h1>500 Internal Server Error</h1><p>Could not save the file.</p></body></html>",
    501: "HTTP/1.1 501 Not Implemented\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: 77\r\n\r\n<html><body><h1>501 Not Implemented</h1><p>This method is not supported.</p></body></html>",
}


CONTENT_TYPES = {
    "html": "text/html",
    "htm": "text/html",
    "css": "text/css",
    "js": "application/javascript",
    "json": "application/json",
    "txt": "text/plain",
    "csv": "text/csv",
    "xml": "application/xml",

    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "gif": "image/gif",
    "webp": "image/webp",
    "svg": "image/svg+xml",
    "ico": "image/x-icon",

    "mp4": "video/mp4",
    "webm": "video/webm",
    "ogg": "video/ogg",
    "mp3": "audio/mpeg",
    "wav": "audio/wav",

    "pdf": "application/pdf",
    "zip": "application/zip",
    "tar": "application/x-tar",
    "gz": "application/gzip",
    "rar": "application/vnd.rar",
    "7z": "application/x-7z-compressed",
    "exe": "application/octet-stream",
    "bin": "application/octet-stream",
    "wasm": "application/wasm",

    "doc": "application/msword",
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "xls": "application/vnd.ms-excel",
    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "ppt": "application/vnd.ms-powerpoint",
    "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",

    "default": "application/octet-stream"
}
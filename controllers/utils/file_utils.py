import os
import zlib

def get_files_of_type(path : str, extension : str):
    if not os.path.exists(path):
        raise Exception("Path not found")
    
    files = []
    for file in os.listdir(path):
        if file.endswith(extension):
            files.append(file)

    return files

def compress_file(file):
    data = b""
    with open(file, "rb") as f:
        data += f.read()

    compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    with open(file+".dat", "wb") as f:
        f.write(compressed_data)

    return file + ".dat"

def decompress_file_bytes(file):
    compressed_data = b""
    with open(file, "rb") as f:
        compressed_data = f.read()

    restored_data = zlib.decompress(compressed_data)
    return restored_data

def write_bytes_to_file(file, data):
    with open(file, "wb") as f:
        f.write(data)
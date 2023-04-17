import os
import zlib
from zipfile import ZipFile

def get_files_of_type(path : str, extension : str, with_path = False):
    if not os.path.exists(path):
        raise Exception("Path not found")

    before = path if with_path else ""
    
    if not before.endswith("/"):
        before += "/"

    files = []
    for file in os.listdir(path):
        if file.endswith(extension):
            files.append(before+file)

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

def zip_files(files: list[str], dest: str):
    with ZipFile(dest, "w") as zip:
        for file in files:
            zip.write(file)

def remove_file(file: list[str]):
    if os.path.isfile(file):
        os.remove(file)
    else:
        raise FileNotFoundError

def remove_files(files: list[str]):
    for file in files:
        remove_file(file)

def unzip_file(file_path: str):
    with ZipFile(file_path, "r") as zip:
        zip.extractall()

def compress_and_remove_files(file_paths: list[str]):
    for file in file_paths:
        compress_file(file)
        remove_file(file)

def decompress_and_remove_files(file_paths: list[str]):
    for file in file_paths:
        out = file.replace(".dat", "")
        write_bytes_to_file(out, decompress_file_bytes(file))
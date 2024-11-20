import os
import hashlib

def calculate_md5(file_path):
    """
    Calculates the MD5 checksum of a file.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_file_metadata(file_path):
    """
    Returns file metadata like size and type.
    """
    if not os.path.exists(file_path):
        return None

    return {
        "filename": os.path.basename(file_path),
        "size": os.path.getsize(file_path),
        "type": file_path.split('.')[-1]
    }

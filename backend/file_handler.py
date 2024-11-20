import os
from werkzeug.utils import secure_filename

# Directory to store uploaded files
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_file(file):
    """
    Saves an uploaded file to the UPLOAD_FOLDER.
    
    Args:
        file: File object from the request.

    Returns:
        dict: Metadata of the saved file including filename, path, and size.
    """
    if not file:
        raise ValueError("No file provided")
    
    # Secure the filename to prevent directory traversal attacks
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    # Save the file
    file.save(file_path)

    # Return file metadata
    return {
        "filename": filename,
        "path": file_path,
        "size": os.path.getsize(file_path)
    }

def get_file_path(filename):
    """
    Returns the full path of a file in the UPLOAD_FOLDER.

    Args:
        filename: Name of the file to locate.

    Returns:
        str: Full file path.
    """
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {filename} not found")
    return file_path

def delete_file(filename):
    """
    Deletes a file from the UPLOAD_FOLDER.

    Args:
        filename: Name of the file to delete.

    Returns:
        bool: True if file was deleted, False if it didn't exist.
    """
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False

def list_files():
    """
    Lists all files in the UPLOAD_FOLDER.

    Returns:
        list: Filenames of all files in the folder.
    """
    return [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]


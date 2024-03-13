import hashlib

def calculate_file_hash(file_path, algorithm='sha256'):
    """
    Calculate the hash value of the binary file located at the given path using the specified algorithm.

    Parameters:
    file_path (str): The path to the file.
    algorithm (str): The hashing algorithm to use (default is 'sha256').

    Returns:
    str: The hash value of the file.
    """
    # Validate algorithm
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported hashing algorithm '{algorithm}'")
    h = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    file_path = 'A:/Pobrane_Instalki/go1.21.3.windows-amd64.msi'
    hash_value = calculate_file_hash(file_path)
    print(f"The hash value of the file '{file_path}' is: {hash_value}")

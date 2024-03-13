import hashlib


def calculate_sha256(file_path):
    """
    Calculate the SHA256 hash value of the Ubuntu file located at the given path.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    str: The SHA256 hash value of the file.
    """
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    sha256_hash = h.hexdigest()
    return sha256_hash


if __name__ == "__main__":
    file_path = 'A:/ubuntu-22.04.4-desktop-amd64.iso'
    calculated_hash = calculate_sha256(file_path)
    print("Calculated hash for the file:", calculated_hash)

    # True hash for ubuntu-22.04.4-desktop-amd64
    true_hash = "071d5a534c1a2d61d64c6599c47c992c778e08b054daecc2540d57929e4ab1fd"

    if true_hash == calculated_hash:
        print("Hash is correct!")
    else:
        print("Hash is not correct!")

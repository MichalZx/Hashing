import hashlib

def calculate_sha256(file_path):
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    sha256_hash = h.hexdigest()
    return sha256_hash


file_path = 'A:/ubuntu-22.04.4-desktop-amd64.iso'
calculated_hash = calculate_sha256(file_path)
print("calculated hash for the file:", calculated_hash)
#ubuntu-22.04.4-desktop-amd64 hash:
true_hash="071d5a534c1a2d61d64c6599c47c992c778e08b054daecc2540d57929e4ab1fd"
if(true_hash == calculated_hash):
    print("hash is correct!")
else:
    print("hash is not correct!")
import hashlib
import time
import plotly.graph_objects as go

def calculate_hash(text, algorithm):
    """
    Calculate the hash value of the given text using the specified algorithm.

    Parameters:
    text (bytes): The text to hash.
    algorithm (str): The hashing algorithm to use.

    Returns:
    tuple: A tuple containing the hash value (str) and the time taken for hashing (float).
    """
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported hashing algorithm '{algorithm}'")
    start_time = time.time()
    h = hashlib.new(algorithm)
    h.update(text)
    if algorithm == 'shake_128':
        result = h.hexdigest(16)
    elif algorithm == 'shake_256':
        result = h.hexdigest(32)
    else:
        result = h.hexdigest()
    end_time = time.time()
    h_final_time = end_time - start_time
    return result, h_final_time

if __name__ == "__main__":
    file_path = './LoremIpsum.txt'

    with open(file_path, "rb") as file:
        text = file.read()

    hashList=['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'shake_128', 'shake_256', 'blake2b', 'blake2s']

    results_dict = {}
    for hash in hashList:
         result, htime = calculate_hash(text, hash)
         results_dict[result] = htime

    # Plotly
    hashes = list(hashList)
    times = list(results_dict.values())

    # Create a plotly figure
    fig = go.Figure(data=go.Bar(x=hashes, y=times))
    fig.update_layout(title='Time for each hashes', xaxis_title='Hash', yaxis_title='Time (seconds)')
    fig.show()

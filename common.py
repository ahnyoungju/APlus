# ===================================================
# Common Function and Library
# ===================================================
import json
import base64

# ===================================================
# Create a formatted string of the Python JSON object
# ===================================================
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)

# ===================================================
# Encrypt File
# ===================================================
def encodeFile(inputF):

    with open(inputF, "rb") as f:
        data = f.read()
    f.close()

    encoded = base64.b64encode(bytes(data))

    with open(inputF, 'wb') as f:
        f.write(encoded)

# ===================================================
# Decrypt File
# ===================================================
def decodeFile(inputF):
    with open(inputF, "rb") as f:
        data = f.read()

    decoded = base64.b64decode(bytes(data))

    with open(inputF, 'wb') as f:
        f.write(decoded)

# ===================================================
# Decrypt Data
# ===================================================
def decode(data):
    decode = base64.b64decode(data)
    return decode
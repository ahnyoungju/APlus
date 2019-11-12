# ===================================================
# Common Function and Library
# ===================================================
import json
import base64

# ===================================================
# jprint
#
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
    print(data)
    print(encoded)

    with open(inputF, 'wb') as f:
        f.write(encoded)
    f.close()

# ===================================================
# Decrypt File
# ===================================================
def decodeFile(inputF):
    with open(inputF, "rb") as f:
        data = f.read()
    f.close()

    decoded = base64.b64decode(bytes(data))
    print(data)
    print(decoded)

    with open(inputF, 'wb') as f:
        f.write(decoded)
    f.close()
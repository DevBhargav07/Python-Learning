#uuid testing 
import re
import uuid
import string
import secrets

alphabet = string.ascii_letters + string.digits

def get_random_key(length=7):
	return "".join(secrets.choice(alphabet) for _ in range(length))

mac_random = "abcdefABCDEF0123456789"
def generate_random_mac():
    string_mac = "".join(secrets.choice(mac_random) for _ in range(12))
    string_mac =  "".join([string_mac[i:i+2]+":" for i in range(0, len(string_mac), 2)])
    return string_mac[:-1]

def is_valid_mac(mac):
    colon_count = mac.count(":")
    dot_count = mac.count(".")
    hypen_count = mac.count("-")

    seperator_count = sum([
        colon_count > 0,
        hypen_count > 0,
        dot_count > 0
    ])
    if seperator_count > 1:
        return False
    
    # valid mac address patterns
    patterns = {
        "colon": r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", # AA:BB:CC:DD:EE:FF
        "hyphen": r"^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}$", # AA-BB-CC-DD-EE-FF
        "dot": r"^([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}$", # AA.BB.CC.DD.EE.FF
        "bare": r"^[0-9A-Fa-f]{12}$" # AABBCCDDEEFF
    }
    return any(re.match(pattern, mac) for pattern in patterns.values())

secret_key = str(get_random_key(length=9))
mac_address = generate_random_mac()
print(mac_address)
# mac_address = "fA:BB:CC:DD:EE:FZ"
valid = is_valid_mac(mac_address)
print(valid)
if not valid:
    print("Fake mac address received")
else:
    generated_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, f'{secret_key}-{mac_address}')

    print(generated_uuid)

from cryptography.fernet import Fernet

"""
TODO:
- Generate a key once and reuse it for both pseudonymization and restoration. In a real system, this key would be securely stored.
"""
key = Fernet.generate_key()
fernet = Fernet(key)


def pseudonymize_names(names):
    """
    TODO: Encrypt each name with Fernet symmetric encryption.
    - return list of encrypted names
    """
    encrypted = []
    for name in names:
        token = fernet.encrypt(name.encode())
        encrypted.append(token.decode())
    return encrypted



def restore_names(encrypted):
    """
    TODO: Decrypt previously pseudonymized names.
    - return list of decrypted names
    """
    restored = []
    for token in encrypted:
        name = fernet.decrypt(token.encode()) 
        restored.append(name.decode())
    return restored

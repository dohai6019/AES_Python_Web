from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def pad(data):
    padding_length = AES.block_size - len(data) % AES.block_size
    return data + bytes([padding_length]) * padding_length


def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]


def encrypt_aes(plaintext, key):
    plaintext_bytes = plaintext.encode("utf-8")

    # Thêm padding
    padded_data = pad(plaintext_bytes)

    # Tạo IV ngẫu nhiên
    iv = get_random_bytes(AES.block_size)

    # Tạo AES ở chế độ CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Mã hóa
    ciphertext = cipher.encrypt(padded_data)

    # Ghép IV với ciphertext
    encrypted_data = iv + ciphertext

    # Chuyển sang Base64
    return base64.b64encode(encrypted_data).decode("utf-8")


def decrypt_aes(encrypted_text, key):
    # Giải mã Base64
    encrypted_data = base64.b64decode(encrypted_text)

    # Lấy IV
    iv = encrypted_data[:AES.block_size]

    # Lấy ciphertext
    ciphertext = encrypted_data[AES.block_size:]

    # Tạo AES
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Giải mã
    padded_data = cipher.decrypt(ciphertext)

    # Bỏ padding
    plaintext_bytes = unpad(padded_data)

    return plaintext_bytes.decode("utf-8")


def main():

    # Khóa AES-256 = 32 byte
    key = b"0123456789ABCDEF0123456789ABCDEF"

    print("=" * 50)
    print("       CHUONG TRINH MA HOA AES-256")
    print("=" * 50)

    plaintext = input("Nhap noi dung can ma hoa: ")

    # Mã hóa
    encrypted = encrypt_aes(plaintext, key)

    print("\n--- KET QUA MA HOA ---")
    print("Du lieu goc:")
    print(plaintext)

    print("\nDu lieu da ma hoa:")
    print(encrypted)

    # Giải mã
    decrypted = decrypt_aes(encrypted, key)

    print("\n--- KET QUA GIAI MA ---")
    print("Du lieu sau khi giai ma:")
    print(decrypted)

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
from hashlib import sha256

password = '123456789'
hashed_password = sha256(password.encode(encoding="utf-8")).hexdigest()

print(hashed_password)

import hashlib 

filename = "Image.jpg"
with open(filename, "rb") as f:
	file_data = f.read()
	image_hash = hashlib.sha256(file_data).hexdigest()
	print("Hash Code Of Image : ", image_hash)
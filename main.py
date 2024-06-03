import base64

# Your base64 encoded certificate string
base64_cert = """INSERT YOUR BASE64 ENCODED CERT HERE"""

base64_cert = base64_cert.replace("\n", "").replace(" ", "")

decoded_cert = base64.b64decode(base64_cert)

pem_cert = "".join(decoded_cert.decode('utf-8'))

with open("certificate.pem", "w") as pem_file:
    pem_file.write(pem_cert)

print("Certificate saved to certificate.pem")

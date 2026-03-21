import socket, base64, re

HOST = "csd.sentinel-cyber.sg"
PORT = 42915

USERS_DB = {
'larry' : 0x496c6b43,
'bridget' : 0xf60977a6,
'billy' : 0x7e337272,
'peter' : 0xe8fbbcbe,
'donald' : 0x14107096,
'hilda' : 0xae1782a5,
'javier' : 0xf623bd34,
'juan' : 0x40ea256f,
'john' : 0xd8177179,
'carolyn' : 0x49559a18,
'jonathan' : 0x58478709,
'martin' : 0xea8e66ad,
'donna' : 0xfdf44767,
'helen' : 0xa4a9c387,
'michael' : 0x9b6baafd,
'velma' : 0x1758ade5,
'linda' : 0xee04ecb3,
'belinda' : 0x689c228d,
'tammy' : 0xeced5f47,
'florida' : 0x327f4716,
'ernest': 0xf93ac6de,
'debra': 0x3d20d707,
'freddie': 0x0c8e88bf,
'martha': 0x3d34adae,
'carol': 0xa3e664d1,
'patricia': 0xf4c66b2b,
'mattie': 0x88e9710a,
'samuel': 0xfe8b33f5,
'melissa': 0xbf9f24c4,
'charles': 0x0e28a0a2,
'jill': 0x5dd3ee0e,
'william': 0xa56ffef9,
'edith': 0x87b851cc,
'dawn': 0x41e2d253,
'scott': 0xcae427c8,
'raymond': 0x2f492ec1,
'robert': 0x037f1270,
'rudy': 0xe6b1d19b,
'meg': 0x852e7a7d,
'frederick': 0x35de9ab1,
'tyler': 0x01580988,
'david': 0x63814141,
'bill': 0x1330d34f,
'todd': 0x1378b9e0,
'thomas': 0xd634a520,
'graciela': 0x9d2fe22f,
'shelly': 0x8adc1f88,
'valerie': 0xf470de7d,
'kenneth': 0x504e3a64,
'jessica': 0x9be8620a,
}

def recv_line(sock):
    buf = b""
    while not buf.endswith(b"\n"):
        chunk = sock.recv(1)
        if not chunk:
            break
        buf += chunk
    return buf.decode(errors="ignore").rstrip("\r\n")

def recv_all(sock):
    chunks = []
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                break
            chunks.append(data)
    except:
        pass
    return b"".join(chunks).decode(errors="ignore")

def compute_response(username, challenge):
    password = USERS_DB[username]
    return (challenge ^ password) + sum(ord(c) for c in username)

flag_found = None

# for username in USERS_DB:
#     try:
s = socket.socket()
s.settimeout(3)
s.connect((HOST, PORT))
s.sendall(b"START\n")
recv_line(s)  # banner
recv_line(s)  # LOGIN

s.sendall(f"USERNAME|\n".encode())
line = recv_line(s)
# if not line.startswith("CHALLENGE|"):
#     continue
challenge = int(line.split("|")[1])
response = compute_response(username, challenge)
s.sendall(f"RESPONSE|{response}\n".encode())

songs = recv_all(s).splitlines()
s.close()

for song in songs:
    try:
        decoded = base64.b64decode(song).decode()
        print(decoded)
        match = re.search(r'FLAG-.*', decoded)
        if match:
            flag_found = match.group()
            print(f"FLAG FOUND for user {username}: {flag_found}")
            break
    except:
        pass

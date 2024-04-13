import socket


class Peer:
    def __init__(self):
        self.protocol = b"BitTorrent protocol" # 19 bytes
        self.reserved = b"\x00" * 8  # 8 bytes reserved
        self.protocol_length = len(self.protocol).to_bytes(1, byteorder="big") # 1 byte
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket

    def handshake(self, info_hash: bytes, peer_id: bytes, peer_ip, peer_port: int):
        if len(info_hash) != 20:
            raise ValueError("info_hash must be 20 bytes long")
        if len(peer_id) != 20:
            raise ValueError("peer_id must be 20 bytes long")
        
        self.socket.connect((peer_ip, peer_port))
        handshake_msg = self.protocol_length + self.protocol + self.reserved + info_hash + peer_id
        self.socket.sendall(handshake_msg)
        response = self.socket.recv(68)
        connected_peer_id = response[48:]
        print(connected_peer_id.hex())
        self.socket.close()

 
    
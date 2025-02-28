import hashlib
from bencode import Bencode
class MetaInfo:
    def __init__(self, data):
        self.announce = data['announce']
        self.info = data['info']
        self.length = self.info['length'] # single file case
        self.files = None # multi files case
        self.piece_length = self.info['piece length']
        self.pieces = self.info['pieces']
        self.info_hash = hashlib.sha1(Bencode.encode(self.info)).digest()
        self.info_hash_hex = self.info_hash.hex()
        
    def get_piece_hashes(self):
        return [self.pieces[i:i+20].hex() for i in range(0, len(self.pieces), 20)]
        
    
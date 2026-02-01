class Codec:
    def __init__(self):
        self.dict = {}

    def encode(self, strs):
        self.dict[str(strs)] = strs
        return str(strs)

    def decode(self, s):
        return self.dict[s]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
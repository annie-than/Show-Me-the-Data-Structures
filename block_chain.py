
import hashlib


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f""" Timestamp: {self.timestamp} \n Data: {self.data} \n SHA256 Hash: {self.hash} \n Prev_Hash: {self.previous_hash} \n"""


class Node:
    def __init__(self, block):
        self.block = block
        self.next = None


class BlockChain:
    def __init__(self):
        self.head = None

    def add_block(self, timestamp, data):
        if self.head is None:
            self.head = Node(Block(timestamp, data, None))
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(Block(timestamp, data, node.block.hash))
        return

    def print_chain(self):
        node = self.head
        while node:
            print(node.block)
            node = node.next


block_chain = BlockChain()
block_chain.add_block("13:12 4/2/2019", "Some information")
block_chain.add_block("13:12 4/2/2019", "Some Information: ABC")
block_chain.add_block("13:12 4/2/2019", "Some Information: BCD")
block_chain.print_chain()








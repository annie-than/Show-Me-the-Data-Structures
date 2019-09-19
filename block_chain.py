
import hashlib
import datetime


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

    def add_block(self, timestamp, data=None):
        if data is None:
            print("No input data for the block")
            return

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
        if node is None:
            print("Block chain empty!")
        else:
            while node:
                print(node.block)
                node = node.next


block_chain = BlockChain()
tc = int(input("Enter the test case number: "))
if tc == 1:
    block_chain.add_block(datetime.datetime.now(), "Some information")
    block_chain.add_block(datetime.datetime.now(), "Some Information: ABC")
    block_chain.add_block(datetime.datetime.now(), "Some Information: BCD")
    block_chain.print_chain()
elif tc == 2:
    block_chain.add_block(datetime.datetime.now())  # Should warning "No input data for the block"
elif tc == 3:
    block_chain.print_chain()








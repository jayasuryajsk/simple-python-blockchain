
import hashlib as hasher
import time
import datetime as date


class Block:
  def __init__(self, index, previousHash, timestamp, data):
    self.index = index
    self.timestamp = timestamp
    self.previousHash = previousHash
    self.data = data
    self.currentHash = self.hashBlock()

  def hashBlock(self):
    sha = hasher.sha256()
    sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previousHash))
    return sha.hexdigest()


def genesisBlock():
	return Block(0,date.datetime.now(),"Genesis Block","0")

def nextBlock(previousBlock):
	newIndex = previousBlock.index + 1
	newTimestamp = date.datetime.now()
	newData = "This block is new " + str(newIndex)
	newHash = previousBlock.currentHash
	return Block(newIndex, newTimestamp, newData, newHash)

blockchain = [genesisBlock()]
previousBlock = blockchain[0]

number_of_blocks = 20

for i in range(0, number_of_blocks):
	block_to_add = nextBlock(previousBlock)
	blockchain.append(block_to_add)
	previousBlock = block_to_add
	print("block #{}h as been added to chain".format(block_to_add.index))
	print('hash: {}\n'.format(block_to_add.currentHash))
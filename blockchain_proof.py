import hashlib
import json
from time import time
import copy

DIFFICULTY = 4  # Quantidade de zeros (em hex) iniciais no hash válido.


class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock()

    def createGenesisBlock(self):
        self.createBlock(previousHash='0' * 64, nonce=0)
        self.mineProofOfWork(self.prevBlock)

    def createBlock(self, nonce=0, previousHash=None):
        if (previousHash == None):
            previousBlock = self.chain[-1]
            previousBlockCopy = copy.copy(previousBlock)
            previousBlockCopy.pop("transactions", None)

        block = {
            'index': len(self.chain) + 1,
            'timestamp': int(time()),
            'transactions': self.memPool,
            'merkleRoot': '0' * 64,
            'nonce': nonce,
            'previousHash': previousHash or self.generateHash(previousBlockCopy),
        }

        self.memPool = []
        self.chain.append(block)
        return block

    def mineProofOfWork(self, prevBlock):
        prevBlock['nonce'] = 0
        while True:
            if(self.isValidProof(prevBlock, prevBlock['nonce'])):
                return True
            prevBlock['nonce'] += 1



    @staticmethod
    def isValidProof(block, nonce):
        blocoAtual = Blockchain.getBlockID(block)
        if blocoAtual.startswith('0' * DIFFICULTY):
            return True
        return False

    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    @staticmethod
    def getBlockID(block):
        # TODO Implemente seu código aqui.
        newBlock = block.copy()
        newBlock.pop('transactions')
        return Blockchain.generateHash(newBlock)

    def printChain(self):
        # Mantenha seu método de impressão do blockchain feito na prática passada.
        pass

    @property
    def prevBlock(self):
        return self.chain[-1]


# Teste
blockchain = Blockchain()
for x in range(0, 4):
    blockchain.createBlock()
    blockchain.mineProofOfWork(blockchain.prevBlock)

for x in blockchain.chain:
    print('[Bloco #{} : {}] Nonce: {} | É válido? {}'.format(x['index'], Blockchain.getBlockID(x), x['nonce'],
                                                             Blockchain.isValidProof(x, x['nonce'])))
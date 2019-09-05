import hashlib
import json
from time import time
class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock()

    def createGenesisBlock(self):
        # Implemente aqui o método para gerar o bloco Genesis, invocado no construtor da classe,
        # chamando o método createBlock() previamente implementado.
        self.createBlock()
    def createBlock(self, nonce=0, previousHash=None):
        # Implemente aqui o método para retornar um bloco (formato de dicionário)
        # Lembre que o hash do bloco anterior é o hash na verdade do CABEÇALHO do bloco anterior.

        bloco = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            'nonce': 0,
            'merkleRoot': '0000000000000000000000000000000000000000000000000000000000000000',
            'previousHash': 0,
            'hashAtual': 0,
            'transactions': []
        }
        self.activeBlock = self.chain[len(self.chain)].copy()
        self.activeBlock.pop('transactions')
        bloco['hashAtual'] = self.generateHash(self.activeBlock)
        if len(self.chain) == 0:
            bloco['previousHash'] = '0000000000000000000000000000000000000000000000000000000000000000'
        else:
            self.prevBlockCopy = self.chain[len(self.chain) - 1].copy()
            self.prevBlockCopy.pop('transactions')
            bloco['previousHash'] = self.generateHash(self.prevBlockCopy)
        self.chain.append(bloco)
        return bloco

    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    def printChain(self):
        # Implemente aqui um método para imprimir de maneira verbosa e intuitiva o blockchain atual.
        for x in self.chain:
            print(' __________________________________________________________________ ')
            print('| {} |'.format(x['previousHash']))
            print('| Índice:\t\tTimestamp:\t\tNonce:\t\t   |')
            print('| {}\t\t\t{}\t{}\t\t   |'.format(x['index'], x['timestamp'], x['nonce']))
            print('| Merkle Root:\t\t\t\t\t\t\t   |')
            print('| {} |'.format(x['merkleRoot']))
            print('| Transações:\t\t\t\t\t\t\t   |')
            print('| 0 \t\t\t\t\t\t\t\t   |')
            print('| Hash do último bloco:\t\t\t\t\t\t   |')
            print('| {} |'.format(x['previousHash']))
            print(' ------------------------------------------------------------------ ')

# Teste
blockchain = Blockchain()
for x in range(0, 3): blockchain.createBlock()
blockchain.printChain()
import unittest
from blockchain.blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_genesis_block(self):
        genesis_block = self.blockchain.chain[0]
        self.assertEqual(genesis_block.index, 0)
        self.assertEqual(genesis_block.previous_hash, "0")
        self.assertEqual(genesis_block.data, "Genesis Block")

    def test_add_block(self):
        self.blockchain.add_block("Test Data")
        self.assertEqual(len(self.blockchain.chain), 2)
        self.assertEqual(self.blockchain.chain[1].data, "Test Data")

    def test_is_chain_valid(self):
        self.blockchain.add_block("Test Data")
        self.assertTrue(self.blockchain.is_chain_valid())

if __name__ == '__main__':
    unittest.main()
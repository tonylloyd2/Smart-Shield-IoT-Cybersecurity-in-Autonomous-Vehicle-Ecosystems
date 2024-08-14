import os
from block.blockchain import Blockchain


def initialize_blockchain():
    blockchain = Blockchain()
    blockchain_log_path = '../data/blockchain_logs/blockchain_data.json'
    blockchain.load_chain(blockchain_log_path)
    return blockchain, blockchain_log_path

def add_log_to_blockchain(blockchain, log_data, blockchain_log_path):
    for log in log_data:
        blockchain.add_block(log)

    if blockchain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid!")

    os.makedirs(os.path.dirname(blockchain_log_path), exist_ok=True)
    blockchain.save_chain(blockchain_log_path)
    print(f"Blockchain logs saved to {blockchain_log_path}")

if __name__ == "__main__":
    blockchain, blockchain_log_path = initialize_blockchain()
    log_data = [
        "Sensor anomaly detected at sensor 1",
        "Normal operation resumed",
        "DDoS attack detected",
        "MITM attack detected",
        "System rebooted"
    ]
    add_log_to_blockchain(blockchain, log_data, blockchain_log_path)
import hashlib

class NeuralCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
        
t1 = "Anna sends 2 NC to Mike"
t2 = "Bob sends 4.1 NC to Mike"
t3 = "Mike sends 4.1 NC to Bob"
t4 = "Mike sends 3.2 NC to Charlie"
t5 = "Daneil sends 2 NC to Anna"
t6 = "Anna sends 2 NC to Mike"

initial_block = NeuralCoinBlock("Initial String",  [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

#Anna sends 2 NC to Mike-Bob sends 4.1 NC to Mike-Initial String
#ac7c14de74c73ddea0bd7d122af9874da86a5900c006a79aaf7dbf0cf9cd38d2

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_data, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash)
# Questão 02 - Hash Table

class HashTable:
    def __init__(self, size = 100):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        # Convertendo a chave em índice
        hash_value = 0
        for char in key:
            hash_value = (hash_value + ord(char)) % self.size
        return hash_value

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        raise KeyError('Chave {} não encontrada.'.format(key))

# Exemplo
hash_table = HashTable()

hash_table.insert('nome', 'Ana')
hash_table.insert('idade', 29)
hash_table.insert('cidade', 'Rio')

print(hash_table.get('nome'))  
print(hash_table.get('idade'))  
print(hash_table.get('cidade'))  

# Testando o erro
try:
    print(hash_table.get('email'))
except KeyError as e:
    print(e)
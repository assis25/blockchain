import hashlib
import json
class Blockchain(object):
    @staticmethod
    def generateHash(data):
        # Implemente aqui seu método para retornar a string referente ao hash SHA256 do argumento passado.
        # Confira a documentação do hashlib: https://docs.python.org/3/library/hashlib.html
        # Note que o argumento passado pode ser um objeto, portanto serialize o argumento antes.
        # Dica: Use o json.dumps() do módulo json.
        dados = hashlib.sha256(json.dumps(data, sort_keys=True).encode())
        hex_dig = dados.hexdigest()
        return hex_dig



# Testando sua implementação: espera-se um retorno True.

var1 = {
            'nome': "Jon Snow",
            'idade': 18,
        }
expected_hash1 = "4145c81419ee987c94f741936c3277e9b281e2ffc9faa3edb5693128e1ee65c1"
var1_hash = Blockchain.generateHash(var1)
print('Dados: {}'.format(var1))
print('Hash   gerado: {}'.format(var1_hash))
print('Hash esperado: {}'.format(expected_hash1))
print('Iguais? {}\n'.format(expected_hash1==var1_hash))
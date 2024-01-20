from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_receber_01_01_2000_deve_retornar_24(self):
        entrada = '01/01/2000'
        esperado = 24
        
        funcionario_teste = Funcionario('Teste', entrada, 1000)
        
        resultado = funcionario_teste.idade()
        
        assert resultado == esperado
    
    def test_quando_sobrenome_recebe_Mariana_Sena_deve_retornar_Sena(self):
        entrada = 'Mariana Sena'
        esperado = 'Sena'
        
        funcionario_teste = Funcionario(entrada, '01/01/2000', 1000)
        
        resultado = funcionario_teste.sobrenome()
        
        assert resultado == esperado
        
    def test_quando_recebe_10000_e_eh_diretor_deve_retornar_9000(self):
        entrada_salario = 10000
        esperado = 9000
        entrada_nome ='Pedro Bragança'
        
        funcionario_teste = Funcionario(entrada_nome, '01/01/2000', entrada_salario)
        
        resultado = funcionario_teste.decrescimo_salario()
        
        assert esperado == resultado
        
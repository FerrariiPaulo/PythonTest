from codigo.bytebank import Funcionario
import pytest
from pytest import mark

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
        
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100
        
        funcionario_teste = Funcionario('Pedro', '01/01/1990', entrada)
        
        resultado = funcionario_teste.calcular_bonus()
        
        assert esperado == resultado
    
    @mark.calcular_bonus    
    def test_quando_calcular_bonus_recebe_20000_deve_retornar(self):
        with pytest.raises(Exception):
            entrada = 20000
                      
            funcionario_teste = Funcionario('Pedro', '01/01/1990', entrada)       
        
            resultado = funcionario_teste.calcular_bonus()
        
            assert resultado
            
        
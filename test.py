import time

def print_com_atraso(atraso_segundos):
    time.sleep(atraso_segundos)

print("Iniciando sistema da Universidade Celestial de Canudos")
print_com_atraso(2)

while True:
    resposta = input("A) Matricular nova pessoa:\nB) Ver dados de funcionario ou aluno:\nC) Voltar\nD) Fechar o programa\nResposta: ").upper()

    if resposta == "A":
        print("Universidade Celestial de Canudos\n      MATRICULA")
        print_com_atraso(1)
        matricular = input("O que deseja matricular:\nA) Matricular Aluno\nB) Matricular Funcionario\nC) Voltar\nD) Fechar o programa\nResposta: ").upper()

        if matricular == "A":
            print("Iniciando matricula do aluno")
            print_com_atraso(0.5)
        elif matricular == "B":
            print("Aqui esta a lista com todos os Cargos:")
            # lista com Cargos dos funcionarios
            print("Enumere o cargo que deseja cadastrar:")
            # chama a classe e inicia o cadastro
        elif matricular == "C":
            continue  # Volta à pergunta anterior
        elif matricular == "D":
            break  # Fecha o programa

    elif resposta == "B":
        visuDados = input("Voce deseja ver dados dos:\nA) Alunos\nB) Funcionarios\nC) Voltar\nD) Fechar o programa\nResposta: ").upper()

        if visuDados == "A":
            print("Aqui esta a lista com todos os Alunos:")
            # lista com nomes de todos alunos
            print("Enumere o aluno que deseja ver:")
        elif visuDados == "B":
            print("Aqui esta a lista com todos os Cargos:")
            # lista com Cargos dos funcionarios
            print("Enumere o cargo que deseja ver:")
            # lista com nomes de todos funcionarios do cargo escolhido
        elif visuDados == "C":
            continue  # Volta à pergunta anterior
        elif visuDados == "D":
            break  # Fecha o programa

print("Programa encerrado.")

from area_circulo import area_circulo
from area_triangulo import area_triangulo
from area_trapezio import area_trapezio
from area_losango import area_losango

def menu():
    print("Escolha uma opção:")
    print("1 - Área de um círculo")
    print("2 - Área de um triângulo")
    print("3 - Área de um trapézio")
    print("4 - Área de um losango")
    print("5 - Sair")

def ler_opcao():
    opcao = input("Digite o número da opção desejada: ")
    return opcao

def calculo():
    while True:
        menu()
        opcao = ler_opcao()

        if opcao == '1':
            raio = float(input("Digite o raio do círculo: "))
            print(f"Área do círculo: {area_circulo(raio)}")
            
        elif opcao == '2':
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            print(f"Área do triângulo: {area_triangulo(base, altura)}")
            
        elif opcao == '3':
            base_maior = float(input("Digite a base maior do trapézio: "))
            base_menor = float(input("Digite a base menor do trapézio: "))
            altura = float(input("Digite a altura do trapézio: "))
            print(f"Área do trapézio: {area_trapezio(base_maior, base_menor, altura)}")
            
        elif opcao == '4':
            diagonal_maior = float(input("Digite a diagonal maior do losango: "))
            diagonal_menor = float(input("Digite a diagonal menor do losango: "))
            print(f"Área do losango: {area_losango(diagonal_maior, diagonal_menor)}")
            
        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    calculo()

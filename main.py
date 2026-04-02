import json
import os

def menu():
    print("\n----- Loja Pokémon -----")
    print("1. Adicionar Pokémon")
    print("2. Listar Pokémon")
    print("3. Atualizar Pokémon")
    print("4. Excluir Pokémon")
    print("0. Sair")


def escolher_grupo():
    print("\nCategoria do Pokémon:")
    print("1. Comum")
    print("2. Raro")
    print("3. Lendário")

    opcao = input("Escolha: ")

    if opcao == "1":
        return "comuns"
    elif opcao == "2":
        return "raros"
    elif opcao == "3":
        return "lendarios"
    else:
        print("Opção inválida.")
        return escolher_grupo()

def ler_dados():
    if not os.path.exists("pokemons.json"):
        return {
            "comuns": [],
            "raros": [],
            "lendarios": []
        }

    with open("pokemons.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_dados(dados):
    with open("pokemons.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

def adicionar():
    grupo = escolher_grupo()

    nome = input("Nome do Pokémon: ")
    hp = int(input("HP: "))

    dados = ler_dados()

    dados[grupo].append({
        "nome": nome,
        "hp": hp
    })

    salvar_dados(dados)
    print("Pokémon adicionado com sucesso!")

def listar():
    dados = ler_dados()

    for grupo in dados:
        print(f"\n--- {grupo.upper()} ---")

        if not dados[grupo]:
            print("Nenhum Pokémon.")
            continue

        for i, p in enumerate(dados[grupo], start=1):
            print(f"{i}. {p['nome']} | HP: {p['hp']}")

def atualizar():
    grupo = escolher_grupo()
    dados = ler_dados()

    if not dados[grupo]:
        print("Nenhum Pokémon nesse grupo.")
        return

    for i, p in enumerate(dados[grupo], start=1):
        print(f"{i}. {p['nome']}")

    index = int(input("Número do Pokémon: ")) - 1

    if 0 <= index < len(dados[grupo]):
        nome = input("Novo nome: ")
        hp = int(input("Novo HP: "))

        dados[grupo][index] = {
            "nome": nome,
            "hp": hp
        }

        salvar_dados(dados)
        print("Atualizado com sucesso!")
    else:
        print("Índice inválido.")

def excluir():
    grupo = escolher_grupo()
    dados = ler_dados()

    if not dados[grupo]:
        print("Nenhum Pokémon nesse grupo.")
        return

    for i, p in enumerate(dados[grupo], start=1):
        print(f"{i}. {p['nome']}")

    index = int(input("Número do Pokémon: ")) - 1

    if 0 <= index < len(dados[grupo]):
        dados[grupo].pop(index)
        salvar_dados(dados)
        print("Excluído com sucesso!")
    else:
        print("Índice inválido.")

def main():
    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            excluir()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

main()
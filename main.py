import json
import os

# Exibe o menu de opções principal no console
def menu():
    print("\n----- Loja Pokémon -----")
    print("1. Adicionar Pokémon")
    print("2. Listar Pokémon")
    print("3. Atualizar Pokémon")
    print("4. Excluir Pokémon")
    print("0. Sair")

# Gerencia a seleção da categoria para organizar os dados no JSON
def escolher_grupo():
    print("\nCategoria do Pokémon:")
    print("1. Comum")
    print("2. Raro")
    print("3. Lendário")

    # Captura a escolha do usuário
    opcao = input("Escolha: ")

    # Retorna a chave correspondente ao dicionário do banco de dados
    if opcao == "1":
        return "comuns"
    elif opcao == "2":
        return "raros"
    elif opcao == "3":
        return "lendarios"
    else:
        # Caso a opção seja inválida, chama a função novamente (recursão)
        print("Opção inválida.")
        return escolher_grupo()

# Carrega as informações do arquivo JSON ou cria uma estrutura inicial se não existir
def ler_dados():
    if not os.path.exists("pokemons.json"):
        return {
            "comuns": [],
            "raros": [],
            "lendarios": []
        }

    with open("pokemons.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

# Grava as alterações realizadas no dicionário de volta para o arquivo físico
def salvar_dados(dados):
    with open("pokemons.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

# Recebe novos dados e insere na lista da categoria escolhida
def adicionar():
    grupo = escolher_grupo()

    nome = input("Nome do Pokémon: ")
    hp = int(input("HP: "))

    dados = ler_dados()

    # Adiciona o novo dicionário ao final da lista selecionada
    dados[grupo].append({
        "nome": nome,
        "hp": hp
    })

    salvar_dados(dados)
    print("Pokémon adicionado com sucesso!")

# Percorre todas as categorias e exibe os Pokémons cadastrados
def listar():
    dados = ler_dados()

    for grupo in dados:
        print(f"\n--- {grupo.upper()} ---")

        if not dados[grupo]:
            print("Nenhum Pokémon.")
            continue

        # Exibe cada item com seu respectivo índice (começando em 1)
        for i, p in enumerate(dados[grupo], start=1):
            print(f"{i}. {p['nome']} | HP: {p['hp']}")

# Localiza um Pokémon específico por grupo e índice para editar seus dados
def atualizar():
    grupo = escolher_grupo()
    dados = ler_dados()

    if not dados[grupo]:
        print("Nenhum Pokémon nesse grupo.")
        return

    # Lista os Pokémons para o usuário saber qual número escolher
    for i, p in enumerate(dados[grupo], start=1):
        print(f"{i}. {p['nome']}")

    index = int(input("Número do Pokémon: ")) - 1

    # Valida se o índice existe na lista antes de tentar editar
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

# Remove um Pokémon da lista com base na categoria e posição
def excluir():
    grupo = escolher_grupo()
    dados = ler_dados()

    if not dados[grupo]:
        print("Nenhum Pokémon nesse grupo.")
        return

    for i, p in enumerate(dados[grupo], start=1):
        print(f"{i}. {p['nome']}")

    index = int(input("Número do Pokémon: ")) - 1

    # Remove o item da lista e salva o estado atual do arquivo
    if 0 <= index < len(dados[grupo]):
        dados[grupo].pop(index)
        salvar_dados(dados)
        print("Excluído com sucesso!")
    else:
        print("Índice inválido.")

# Ponto de entrada do programa que mantém o loop de execução
def main():
    while True:
        menu()
        opcao = input("Escolha: ")

        # Direciona o fluxo para a função correspondente
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

# Inicia a execução do sistema
main()

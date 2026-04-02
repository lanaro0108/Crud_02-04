# Crud_02-04
# 🎮 Loja Pokémon

Um sistema de gerenciamento de inventário Pokémon desenvolvido em **Python**. O projeto permite realizar operações de CRUD (Create, Read, Update, Delete) diretamente no terminal, com persistência de dados em formato **JSON**.

## 📌 Funcionalidades

O script oferece uma interface de menu interativa para:
- **Adicionar Pokémon**: Registra o nome e o HP, separando-os por categorias (Comuns, Raros e Lendários).
- **Listar Pokémon**: Exibe todos os registros salvos de forma organizada por grupo.
- **Atualizar Pokémon**: Permite modificar os atributos de um Pokémon já existente.
- **Excluir Pokémon**: Remove um registro específico do banco de dados.
- **Persistência de Dados**: Grava e lê as informações automaticamente no arquivo `pokemons.json`.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **JSON**: Para armazenamento e intercâmbio de dados.
- **OS**: Para manipulação e verificação de arquivos do sistema.

## 📂 Estrutura de Dados

Os dados são armazenados seguindo esta estrutura hierárquica no arquivo `pokemons.json`:

```json
{
  "comuns": [],
  "raros": [],
  "lendarios": []
}

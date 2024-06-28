opcao = 0
produtos = []
precos = []
quantidadeEstoque = []

# Loop de Opções
while opcao < 4:
  # Menu
  print("\n1. Adicionar Produto")
  print("2. Atualizar Produto")
  print("3. Visualizar Estoque")
  print("4. Sair do Sistema")
  # Entrada de Opção
  opcao = int(input("Digite a opção desejada: "))
  if opcao == 1:
    # Entrada do nome do produto + adicionado na lista de produtos
    nomeDoProduto = str(input("Digite o nome do produto: "))
    produtos.append(nomeDoProduto)
    print(f"Produto {nomeDoProduto} adicionado com sucesso!!")

    # Entrada do preço do produto + adicionado na lista de preços
    precoProduto = float(input("Digite o preço do produto: "))
    precos.append(precoProduto)
    print(f"Preço {precoProduto} adicionado com sucesso!!")

    # Entrada da quantidade do produto + adicionado na lista de quantidade de estoque
    quantidadeProduto = int(input("Digite a quantidade do produto: "))
    quantidadeEstoque.append(quantidadeProduto)
    print(f"{quantidadeProduto} {nomeDoProduto} adicionados com sucesso!!")
    
  elif opcao == 2:
    # Se alguma lista estiver vazia, não é possível atualizar e mostra mensagem de erro
    if not produtos or not precos or not quantidadeEstoque: 
      print("\nErro\n")
      
    else:
      # Display da lista de produtos e entrada do nome do produto que será atualizado
      print("A lista de produtos disponíveis: \n" + str(produtos))
      produtoSelecionado = str(input("Digite o nome do produto que deseja alterar: "))
      # Verifica se o produto selecionado está na lista de produtos para a modificação
      for i in range(len(produtos)):
        if produtos[i] == produtoSelecionado:
            novoPreco = float(input("Digite o novo preço: "))
            novaQuantidade = int(input("Digite a nova quantidade: "))

            precos[i] = novoPreco
            quantidadeEstoque[i] = novaQuantidade

  elif opcao == 3:
    for i in range(len(produtos)):
      # Se alguma lista estiver vazia, não é possível atualizar e mostra mensagem de erro
      if not produtos or not precos or not quantidadeEstoque:
        print("\nErro\n")
      # Se não houver erros, mostra a lista de produtos e seus respectivos preços
      else:
        print(f"\nProduto: {produtos[i]}")
        print(f"Preço: {precos[i]}")
        print(f"Quantidade em estoque: {quantidadeEstoque[i]}")
quantidade = 0
a = []
while True:
    
    option = int(input("Selecione a opção: 1: CADASTRAR, 2: LISTAR, 3 PROCURAR, 4 EXCLUIR, 5 QUANTIDADE, 0 SAIR: "))
    match option:
        case 1:
       
            print("---CADASTRO DE LIVROS---")
            name = input("NOME: ")
            year = int(input("ano de publicação: "))
            author = input("nome do author: ")
            publisher = input("nome da editora: ")
            book = {
                "name" : name,
                "year" : year,
                "author": author,
                "publisher": publisher,   
            }
            a.append(book)
        case 2:
            print("---LISTAR LIVROS---")
            for book in a:
                print(book["name"])
                print(book["year"])
                print(book["author"])
                print(book["publisher"])
        case 3: 
            print("---PROCURAR LIVROS---")
            np = input("Digite o nome do livro para procurar: ")
            for book in a:
                if book["name"] == np:
                    print(book)
        case 4:
            print("---EXCLUIR LIVROS---")
            np = input("Digite o nome do livro para excluir: ")
            for book in a:
                if book["name"] == np:
                    del(book)
                    print("Livro excluído.")
        case 5:
            for book in a:
                quantidade += 1
            print("existem ", quantidade ,"livros")
            quantidade = 0
        case 0:
            break
        case _:
            print("erro, opção invalida ")
                
                
                    
            
            
            
            
        

        
    
     









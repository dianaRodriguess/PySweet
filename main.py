import os

#####################################
##### Projeto Escola - Versão 1 #####
#####################################

resp = ''
while resp != '0':
  os.system('clear')
  print("############################################")
  print("######       Projeto PySweet       ######")
  print("############################################")
  print("#####      1 - Módulo Cadastrar        #####")
  print("#####      2 - Módulo Pesquisar        #####")
  print("#####      3 - Módulo Atualizar        #####")
  print("#####      4 - Módulo Deletar          #####")
  print("#####      5 - Módulo Relatório        #####")
  print("#####      6 - Módulo Informações      #####")
  print("#####      0 - Sair                    #####")
  resp = input("##### Escolha sua opção: ")

  if resp == '1':
      print()
      print("############################################")
      print("#####     Você está no Módulo Cadastrar     ####")
      print("############################################")
      print()
      input("Tecle <ENTER> para continuar...")
  elif resp == '2':
      print()
      print("############################################")
      print("#####   Você está no Módulo Atualizar   ####")
      print("############################################")
      print()
      input("Tecle <ENTER> para continuar...")
  elif resp == '3':
      print()
      print("############################################")
      print("#####     Você está no Módulo Deletar     ####")
      print("############################################")
      print()
      input("Tecle <ENTER> para continuar...")
  elif resp == '4':
      print()
      print("############################################")
      print("#####   Você está no Módulo Relatório   ####")
      print("############################################")
      print()
      input("Tecle <ENTER> para continuar...")
  elif resp == '5':
      print()
      print("############################################")
      print("#####  Você está no Módulo Informações  ####")
      print("############################################")
      print()
      print("##### Projeto de Gestão de uma Escola   ####")
      print("##### Equipe de desenvolvimento:        ####")
      print("##### Flavius Gorgônio @flgorgonio      ####")
      print("##### Vitória Geovanna @vitoriageovanna ####")
      print("##### Licença Pública Geral GNU         ####")
      print("##### www.gnu.org/licenses/gpl.html     ####")
      print()
      input("Tecle <ENTER> para continuar...")


print("Você encerrou o programa!")
print("Até logo!")

class ConverterPesEmMetros:
    def pesParaMetros(self, pes):
        return pes * 0.3048

    def metrosParaPes(self, metros):
        return metros * 3.281

class ConverterJardasEmMetros:
    def jardasEmMetros(self, jardas):
        return jardas * 0.9144

    def jardasEmPes(self, jardas):
        metros = self.jardasEmMetros(jardas)
        return metros * 3.281

converterPesMetros = ConverterPesEmMetros()
converterJardasMetros = ConverterJardasEmMetros()

print("Escolha uma das opções: \n"
      "1 - Pés para metros\n"
      "2 - Metros para pés\n"
      "3 - Jardas para metros\n"
      "4 - Jardas para pês")

opcao = int(input("Digite uma opção correspondente: "))

if opcao == 1:
    pes = float(input("Digite a quantidade de pês: "))
    metros = converterPesMetros.pesParaMetros(pes)
    print(f"{pes} pés é igual a {metros:.4f} metros.")
elif opcao == 2:
    metros = float(input("Digite a quantidade de metros: "))
    pes = converterPesMetros.metrosParaPes(metros)
    print(f"{metros} pés é igual a {pes:.4f} metros.")
elif opcao == 3:
    jardas = float(input("Digite a quantidade de jardas: "))
    metros = converterJardasMetros.jardasEmMetros(jardas)
    print(f"{jardas} pés é igual a {metros:.4f} metros.")
elif opcao == 4:
    jardas = float(input("Digite a quantidade de jardas: "))
    pes = converterJardasMetros.jardasEmPes(jardas)
    print(f"{jardas} pés é igual a {pes:.4f} metros.")
else:
    print("Opção inválida.")

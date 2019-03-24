"""
43- Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

-o total a pagar com desconto de 10%;
-o valor de cada parcela, no parcelamento de 3x sem juros;
-a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
-a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""
try:

    val_prod = float(input("Digite o valor total da compra: R$"))

    print(f"""
    O valor total a pagar com desconto de 10% é R${val_prod-(val_prod*10/100)}
    O valor da parcela em 3x s/ juros é R${val_prod/3}
    Comissão venda a vista R${(val_prod-(val_prod*10/100))*5/100}
    Comissão venda parcelada R${val_prod*5/100}
    """)

except ValueError:

    print(f'Somente números são aceitos. Feche o programa e tente novamente.')

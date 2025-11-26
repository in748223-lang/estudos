import pandas as PD

dados_df = PD.read_excel("produtos_ficticios.xlsx")

#print (dados_df.to_string ()) 
#print (dados_df.columns)
#print(dados_df.shape)


#produto = dados_df[['Categoria','Código do produto']]
#print(produto)

#roupa = dados_df.loc[dados_df['Categoria'] == 'Roupas', ['Categoria','Código do produto', 'Preço']]
#print(roupa)

#cor= dados_df.loc[dados_df['Cor']== 'Preto']
#print(cor)

 #produto_cor_df= dados_df.loc[(dados_df['Categoria'] == 'Roupas') & (dados_df['Cor'] == 'Preto'),
 #['Categoria','Código do produto','Preço','Cor']]
#print (produto_cor_df)

print(dados_df.loc[5, 'Código do produto'])




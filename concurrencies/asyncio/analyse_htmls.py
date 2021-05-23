#%%
### Aki a gente faz ETL, extrai dados e gera o HTML

# from get_html_of_sites import get_all_htmls

# html = get_all_htmls()
# with open('final_text.txt', 'w') as x:
#     x.write('\n\n\n\n'.join(html))
#%%
import re 
import pyperclip
#%%
with open('final_text.txt', 'r') as x:
    html = x.read()

# %% with price:
p = re.compile("<div class=\"informacoesListagemPrincipais\">.*\n.*\n.*<p>(.*)</p>.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*>(.*)<")

products_price = set(re.findall(p,html))
len(products_price)



# %% without price:
p = re.compile("<div class=\"informacoesListagemPrincipais\">.*\n.*\n.*<p>(.*)</p>")

products = list(set(re.findall(p,html)))
products
#%%


import pandas as pd 

df1 = pd.DataFrame(products, columns = ['name'])

df2 = pd.DataFrame(products_price, columns = ['name','price'])

df = pd.merge(left = df1, right = df2, on = 'name', how = 'outer')
df
#%%
df.name.nunique()

yo = df.to_html()
#%%
with open('lala.html', 'w') as x:
    x.write(yo)
#%%
#
# <div class="informacoesListagemPrincipais">
#                                                                     <div class="itemListagemNomeProduto">
#                                             <p>illustra GFX PCR DNA and Gel Band Purification Kit, 250 Purifications - Cytiva - 28903471</p># %%

# %%

######
# Objective of this project:
# Join tables 
# using function from the module treat tables

#%%
import modules.treat_tables as tt

if __name__ == '__main__':
    # first part: join all clients tables
    clients = tt.join_tables(
        'dados_clientes')
    
    # final part: save to csv
    clients.to_csv(
        r'output/merged_tables.csv')


# %%
clients
# %%

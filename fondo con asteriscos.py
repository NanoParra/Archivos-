import random

astericos="*"
entre_comillas="()"
tilde="'' '"
unir=f"{astericos}{tilde}"

for i in range(80):
    for j in range(20):
        print (random.choice(unir),end=" ",)
print("")
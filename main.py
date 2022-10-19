import time, random as r, string as st

bsVindas="Bem vindo. Eu sou o Po-gag e vou te ajudar a ter uma nova senha segura!\n"
for x in list(bsVindas):
    print(x, end="", flush=True)
    time.sleep(0.1)

senha=""
for x in range(13):
    senha=senha+r.choice(st.ascii_letters+st.digits+st.punctuation)
print(f"Sua nova senha é: {senha}")

import time, random as r, string as st

senha=""
for x in range(13): senha=senha+r.choice(st.ascii_letters+st.digits+st.punctuation)
print(f"Sua nova senha é: {senha}")

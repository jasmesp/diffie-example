p = 23
g = 5

bob_private = 3 #a
alice_private = 6 #b

# alice_public = (g ** alice_private) % p #A
alice_public = pow(g, alice_private, p) #refactor for betterness
# bob_public = (g ** bob_private) % p #B
bob_public = pow(g, bob_private, p) #refactor for betterness

# alice_shared = (bob_public ** alice_private) % p #s
alice_shared = pow(bob_public, alice_private, p) #refactor for betterness
bob_shared = pow(alice_public, bob_private, p) #s

assert alice_shared == bob_shared

print(alice_shared, bob_shared)


def eves_nightmare():
    for i in range(p-1):
        if pow(g, i, p) == alice_public:
            print("ur done for, this is why we need a huge p!")
            return i
    return None

print("Eve wins!",eves_nightmare())

        
        
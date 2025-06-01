p = 23
g = 5

bob_private = 3 #a
alice_private = 6 #b

alice_public = (g ** alice_private) % p #A
bob_public = (g ** bob_private) % p #B

alice_shared = (bob_public ** alice_private) % p #s
bob_shared = (alice_public ** bob_private) % p #s

assert alice_shared == bob_shared

print(alice_shared, bob_shared)

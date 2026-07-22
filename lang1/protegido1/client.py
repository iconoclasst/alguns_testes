from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/tradutor")
idio = input('Insira o idioma: ')
text = input('Insira o texto: ')
resp = remote_chain.invoke({'idioma': idio, 'texto': text})

print(resp)

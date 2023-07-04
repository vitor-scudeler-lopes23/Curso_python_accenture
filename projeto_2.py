usuarios = {
    "Carolinda" : "Carol@123",
    "RodolfoJunior" : "Junior$345",
    "JoseFabiano" : "JoseFabi@890"
}

nome_usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if nome_usuario in usuarios and senha == usuarios[nome_usuario]:
    print("Login bem-sucedido!")
else:
    print("Falha no login. Verifique o nome de usuário e a senha.")
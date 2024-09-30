print("Bem-vindo ao Quiz!")
print("--------------------")

perguntas = [
    {
        "pergunta": "Por quem a gravidade foi descoberta?",
        "respostas": ["Isaac Newton", "Albert Einstein", "Galileu Galilei", "Leonardo da Vinci"],
        "correta": "Isaac Newton"
    },
    {
        "pergunta": "Qual o orgão que os seres humanos respiram?",
        "respostas": ["Coração", "Pulmão", "Fígado", "Rim"],
        "correta": "Pulmão"
    },
    {
        "pergunta": "Qual foi o país que Portugal descobriu?",
        "respostas": ["Alemanha", "Espanha", "Brasil", "Índia"],
        "correta": "Brasil"



    }
]

pontos = 0

for pergunta in perguntas:
    print(pergunta["pergunta"])
    for i, resposta in enumerate(pergunta["respostas"]):
        print(f"{i+1}. {resposta}")
    resposta_usuario = input("Escolha uma opção: ")
    if pergunta["respostas"][int(resposta_usuario) - 1] == pergunta["correta"]:
        print("Parabéns, você acertou!")
        pontos += 1
    else:
        print(f"Erro, a resposta correta é {pergunta['correta']}")

print(f"Você fez {pontos} pontos!")
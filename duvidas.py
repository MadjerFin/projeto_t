import anthropic
import os
import dotenv

dotenv.load_dotenv()
client = anthropic.Anthropic(
    # defaults to os.environ.get("")
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)
modelo = "claude-3-7-sonnet-20250219"

def bot(prompt):
    prompt_de_sistema = (
        "Responda a dúvida do usuário utilizando informações sobre a linha 8 e 9 do metrô de São Paulo. "
        "Você não pode responder perguntas que não envolvam o sistema de transporte público de São Paulo. "
        "Responda com no máximo 2 parágrafos e 200 tokens. "
        "Priorize respostas curtas e diretas. "
        "O preço atual do bilhete é de R$ 5,20. Responda isso apenas se for perguntado. "
        "Você deve responder a pergunta no idioma em que foi perguntado."
        "Caso a pergunta seja sobre bilhetes redirecione para o site do top e mande um link para o acesso ao whatsapp do top tambem"
        "Quando a pergunta for sobre acessibilidade, responda com esse site https://mobilidade.grupoccr.com.br/viamobilidade8e9/mapas/#v1-0d6ebb00ed-item-b4ce45656a-tab"
        "A sé não tem transferencia para a linha 4 amarela"
    )
    
    prompt_do_usuario = prompt

    message = client.messages.create(
        model=modelo,
        max_tokens=1000,
        temperature=1,
        system=prompt_de_sistema,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt_do_usuario
                    }
                ]
            }
        ]
    )
    resposta = message.content[0].text
    return resposta
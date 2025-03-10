import anthropic
import os
import dotenv

dotenv.load_dotenv()
client = anthropic.Anthropic(
    # defaults to os.environ.get("")
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)
modelo = "claude-3-5-sonnet-20240620"
propmt_de_sistema = "Responda a dúvida do abaixo utilizando informações sobre a linha 8 e 9 do metrô de São Paulo"
propmt_do_usuario = input("Olá, meu nome é TRIP, em que posso te ajudar?")

message = client.messages.create(
    model= modelo,
    max_tokens=1000,
    temperature=1,
    system= propmt_de_sistema,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": propmt_do_usuario
                }
            ]
        }
    ]
)
resposta = message.content[0].text
print(resposta)
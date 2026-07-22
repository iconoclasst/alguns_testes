# ------------------------------------------------------------------------
# Importação de variáveis de ambiente, importação de modelo, parser de saída, criação de mensagens
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage 
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Mensagens no formato padrão (inutilizadas na chain)
messages = [
    SystemMessage("Traduza literalmente o texto a seguir para inglês"),
    HumanMessage("Teste 1")
]
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Criação de modelo e parser para texto da saída
model = GoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0)
parser = StrOutputParser()
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Apenas ilustração de como seria a execução passo a passo. Primeiro passa as mensagens (SystemMessage e HumanMessage)
# para o invoke do modelo, depois extrai o texto com o parser.invoke que recebe a resposta
# resp = model.invoke(messages) ###
# text = parser.invoke(resp) ###
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Criação de template de mensagem. Serve para entradas pré-definidas com alteração de variáveis.
# Nesse caso, as variáveis são "idioma" e "texto". Os termos "system" e "user" seriam a
# SystemMessage e HumanMessage.
msg_template = ChatPromptTemplate.from_messages([
    ("system", "Traduza literalmente o texto a seguir para {idioma}"),
    ("user" "{texto}"),
])
#------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Definição das variáveis em forma de dicionário. O dicionário é passado como input 
# na chain para o msg_template. 
variables = {
    "idioma": "francês",
    "texto": "teste 2"
}
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Definição da chain. Inicia com o msg_template e termina com o texto extraido pelo parser.
chain = msg_template | model | parser
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Resultado com chain.invoke
print(chain.invoke(variables))
# ------------------------------------------------------------------------

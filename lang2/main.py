import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# -------------------------------------------------------------------------------------
# Carregamento de variávies de ambiente
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Criação e definição do funcionamento do modelo

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0)
parser = StrOutputParser()

msg_template = ChatPromptTemplate([
    ('system',
    '''
    Você é um assistente que vai simplesmente analisar arquivos.
    Você não pode inventar informações e nem pode fazer operações de risco.
    Você só pode usar as ferramentas disponíveis.
    Você fará uma ação de acordo com o input do user.
    '''
    ),

    ('user', 
    '''
    <input>
    {input}
    </input>
    '''
    )
])
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Primeira tool
from langchain.tools import tool

@tool
def ler_arquivo(caminho:str) -> str:
    '''Lê o conteúdo de um arquivo'''
    with open(caminho, 'r') as f:
        return f.read()
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# vinculo de ferramentas
model_with_tool = model.bind_tools([ler_arquivo])
# -------------------------------------------------------------------------------------

#Tratamento de decisão do modelo
entrada = input("Insira a entrada: ")
prompt = msg_template.invoke({'input': entrada})
response = model_with_tool.invoke(prompt.messages)
call = response.tool_calls[0]

id = call['id']
caminho = call['args']['caminho']
caminho = os.path.expanduser(caminho)

resultado = ler_arquivo.invoke({'caminho':caminho})
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Invocação da ferramenta
from langchain_core.messages import ToolMessage

tool_message = ToolMessage(
    content=resultado,
    tool_call_id = id
)
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Invocação final do modelo
final = model.invoke([
    *prompt.messages,
    response, 
    tool_message
])

print(final.content)
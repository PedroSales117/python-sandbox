from transformers import pipeline

# Inicializar a pipeline de question answering
qa_pipeline = pipeline("question-answering")

# Definir o contexto e a pergunta
contexto = """Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991."""

pergunta = "Quem lançou Python?"

# Executar a pipeline de question answering
resposta = qa_pipeline(question=pergunta, context=contexto)

# Exibir a resposta
print(resposta)

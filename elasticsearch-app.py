from elasticsearch import Elasticsearch

class SimpleRetriever:
    def __init__(self, index_name, host, port, scheme='http'):
        self.es = Elasticsearch(
            [{'host': host, 'port': port, 'scheme': scheme}]
        )
        self.index_name = index_name

    def index_documents(self, documents):
        for doc_id, document in enumerate(documents):
            self.es.index(index=self.index_name, id=doc_id, body=document)

    def search(self, query, top_k=5):
        response = self.es.search(index=self.index_name, body={
            'query': {
                'match': {
                    'content': query
                }
            },
            'size': top_k
        })
        
        return [(hit['_source'], hit['_score']) for hit in response['hits']['hits']]

# Exemplo de uso
if __name__ == "__main__":
    # Ajuste os valores de host, port e scheme conforme necessário
    retriever = SimpleRetriever(index_name="my_documents_index", host='localhost', port=9200, scheme='http')
    documents = [
        {"content": "Documento sobre IA."},
        {"content": "Documento sobre aprendizado de máquina."},
        {"content": "Documento sobre saúde."},
    ]
    retriever.index_documents(documents)
    query = "aprendizado de máquina"
    results = retriever.search(query)
    print(results)

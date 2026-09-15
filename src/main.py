from sentence_transformers import SentenceTransformer


from document_reader import read_document
from chunker import chunk_text
from retriever import retrieve_best_chunk

def main():
    document = read_document("data/sample.txt")
    chunks = chunk_text(document)

    model = SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    query = "Sistem hangi belge türlerini destekleyecek?"

    best_chunk, best_score = retrieve_best_chunk(
        query,
        chunk,
        model
    )

    print("AI Knowledge RAG başlatıldı")
    print(f"Soru: {query}")
    print(f"Benzerlik skoru: {best_score}")
    print("\nEn uygun chunk:")
    print(best_chunk)

if __name__ == "__main__":
    main()

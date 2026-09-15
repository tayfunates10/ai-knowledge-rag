from document_reader import read_document
from chunker import chunk_text

def main():
    document = read_document("data/sample.txt")
    chunks = chunk_text(document)

    print("AI Knowledge RAG başlatıldı")
    print(f"Toplam chunk sayısı: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n--- Chunk {index} ---")
        print(chunk)

if __name__ == "__main__":
    main()

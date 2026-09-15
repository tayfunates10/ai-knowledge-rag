def chunk_text(text: str, chunk_size: int = 100) -> list[str]:
    words = text.split()

    chunks = []
    current_chunk = []

    for word in words:
        candidate = " ".join(current_chunk + [word])

        if len(candidate) <= chunk_size:
            current_chunk.append(word)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]

        if current_chunk:
         current_chunk.append(" ".join(current_cunk))
    
    return chunks

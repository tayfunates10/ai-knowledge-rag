def chunk_text(text: str, chunk_size: int = 100, overlap_words: int = 3) -> list[str]:
    words = text.split()

    chunks = []
    current_chunk = []

    for word in words:
        candidate = " ".join(current_chunk + [word])

        if len(candidate) <= chunk_size:
            current_chunk.append(word)
        else:
            chunks.append(" ".join(current_chunk))

            overlap = current_chunk[-overlap_words:]
            current_chunk = overlap + [word]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

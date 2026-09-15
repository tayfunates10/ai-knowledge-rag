from vector_math import cosine_similarity


def retrieve_best_chunk(query: str, chunks: list[str], model) -> tuple[str,float]:
    query_embedding = model.encode(query).tolist()

    best_chunk = ""
    best_score = (-1, 0)

    for chunk in chunks:
        chunk_embedding = model.encode(chunk).tolist()

        score = cosine_similarity(
            query_embedding,
            chunk_embedding
        )

        if score > best_score:
            best_score = score
            best_chunk = chunk

    return best_chunk, best_score

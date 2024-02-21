def vo_embed(documents):
    # This snippet is given in the VoyageAI API docs.
    batch_size = 128
    documents_embeddings = [
        vo.embed(
            documents[i:i + batch_size], model="voyage-2", input_type="document",
        ).embeddings
        for i in range(0, len(documents), batch_size)
    ]
    documents_embeddings_final = [[]]
    for doc in documents_embeddings:
        documents_embeddings_final.extend(doc)
    del[documents_embeddings_final[0]]
    return documents_embeddings_final
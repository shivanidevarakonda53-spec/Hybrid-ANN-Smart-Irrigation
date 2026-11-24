
import faiss
import pickle
from sentence_transformers import SentenceTransformer

print("Loading knowledge database...")

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

index = faiss.read_index("knowledge.index")

with open("knowledge.pkl", "rb") as file:
    chunks = pickle.load(file)

def search_knowledge(question):

    question_embedding = model.encode(
        [question],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    scores, results = index.search(question_embedding, 3)

    print("\nRelevant agricultural information:\n")

    for position, score in zip(results[0], scores[0]):

        if position == -1:
            continue

        print("Source:", chunks[position]["filename"])
        print("Relevance:", round(float(score), 3))
        print("Information:", chunks[position]["text"])
        print("-" * 50)


question = input("Ask an agricultural question: ")

search_knowledge(question)

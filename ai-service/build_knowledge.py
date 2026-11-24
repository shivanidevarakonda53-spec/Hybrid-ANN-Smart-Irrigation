
import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Folder containing agricultural documents
DOCUMENT_FOLDER = "documents"

# Load multilingual embedding model
print("Loading embedding model...")

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

documents = []

# Read all text files
for filename in os.listdir(DOCUMENT_FOLDER):

    if filename.endswith(".txt"):

        file_path = os.path.join(DOCUMENT_FOLDER, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        documents.append({
            "filename": filename,
            "content": content
        })

print("Documents loaded:", len(documents))

# Divide documents into smaller chunks
chunks = []

for document in documents:

    paragraphs = document["content"].split("\n\n")

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if len(paragraph) > 30:

            chunks.append({
                "filename": document["filename"],
                "text": paragraph
            })

print("Total chunks:", len(chunks))

# Generate embeddings
texts = [chunk["text"] for chunk in chunks]

embeddings = model.encode(
    texts,
    convert_to_numpy=True,
    normalize_embeddings=True
)

# Create FAISS vector database
dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(embeddings)

# Save vector database
faiss.write_index(index, "knowledge.index")

# Save document information
with open("knowledge.pkl", "wb") as file:
    pickle.dump(chunks, file)

print("\nKnowledge database created successfully!")
print("Saved: knowledge.index")
print("Saved: knowledge.pkl")


import torch
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

print("Loading RAG system...")

# Load embedding model
embedding_model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# Load FAISS database
index = faiss.read_index("knowledge.index")

with open("knowledge.pkl", "rb") as file:
    chunks = pickle.load(file)

# Load language model
model_name = "Qwen/Qwen2.5-1.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)

llm = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    low_cpu_mem_usage=True
)

print("RAG chatbot is ready!")


def get_context(question):

    question_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    scores, results = index.search(question_embedding, 3)

    context = []

    for position in results[0]:

        if position != -1:
            context.append(chunks[position]["text"])

    return "\n\n".join(context)


def ask_chatbot(question):

    context = get_context(question)

    messages = [
        {
            "role": "system",
            "content": (
                "You are an agricultural assistant. "
                "Answer using the supplied agricultural information. "
                "If the information is insufficient, say so. "
                "Do not invent irrigation quantities. "
                "Use simple language."
            )
        },
        {
            "role": "user",
            "content": (
                f"Question: {question}\n\n"
                f"Agricultural information:\n{context}\n\n"
                "Give a clear answer."
            )
        }
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():

        outputs = llm.generate(
            **inputs,
            max_new_tokens=150,
            do_sample=False
        )

    answer = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=True
    )

    return answer


if __name__ == "__main__":

    while True:

        question = input("\nAsk your farming question (type exit to stop): ")

        if question.lower() == "exit":
            break

        answer = ask_chatbot(question)

        print("\nAI Answer:")
        print(answer)
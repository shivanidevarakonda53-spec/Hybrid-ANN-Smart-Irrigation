
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Qwen/Qwen2.5-1.5B-Instruct"

print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    low_cpu_mem_usage=True
)

def ask_ai(question):
    messages = [
    {
        "role": "system",
        "content": (
            "You are an agricultural assistant. "
            "Answer accurately in the same language as the user's question. "
            "Use simple, natural language. "
            "For Telugu questions, use only correct Telugu. "
            "For Hindi questions, use only correct Hindi. "
            "Do not mix languages. "
            "Give short and clear answers."
        )
    },
    {
        "role": "user",
        "content": question
    }
]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False
    )

    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=False,
            repetition_penalty=1.15
        )

    answer = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=True
    )

    return answer


questions = [
    "Explain smart irrigation in simple English.",
    "స్మార్ట్ ఇరిగేషన్ అంటే ఏమిటి? తెలుగులో వివరించండి.",
    "स्मार्ट सिंचाई क्या है? हिंदी में समझाइए।"
]

for question in questions:
    print("\nQuestion:", question)
    print("AI Answer:", ask_ai(question))
    print("-" * 50)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from google import genai
# from langchain_community.vectorstores import FAISS
# from langchain_huggingface import HuggingFaceEmbeddings
# import os

# # Load vector database from file
# def load_vector_db(db_path="faiss_index"):
#     embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#     vector_db = FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
#     return vector_db

# # Retrieve relevant data from vector database
# def retrieve_relevant_data(vector_db, query):
#     retriever = vector_db.as_retriever()
#     relevant_docs = retriever.get_relevant_documents(query)
#     # Extracting the page content
#     page_contents = [doc.page_content for doc in relevant_docs]
#     return "\n".join(page_contents)

def generator(query):
    ### uncomment below code to use RAG

    # db_path = "faiss_index"  # Path to stored FAISS index
    # vector_db = load_vector_db(db_path)

    # retrieved_data = retrieve_relevant_data(vector_db, query)

    with open("./static/knowledge.txt", "r", encoding="utf-8") as file:
        knowledge = file.read()

    client = genai.Client(api_key="AIzaSyC09vgOIf0feqQ2omtUaraUbzYZu9vUtHI")
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=f"Follow below instruction for text generation: \n1. You are Jarvis, an assistant. \n2. Greet only if question is Greeting and Greeting should be in few words only. \n3. Do not show that a document or text has been shared while responding. \n4. Use following Given knowledge if it contains answer of query else answer that you have no information for that. \n5. Answer in maximum 50 words only.\n\n Question: {query}. \n\n Given knowledge: You are Jarvis, an assistant. {knowledge}"

    )
    return response.text

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            response_message = generator(user_message)
            return JsonResponse({"response": response_message})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
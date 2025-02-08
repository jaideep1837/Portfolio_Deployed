from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from google import genai

def generator(query):
    client = genai.Client(api_key="AIzaSyC09vgOIf0feqQ2omtUaraUbzYZu9vUtHI")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"Question: {query}. You are bagul, an assistant. answer in few words only."
    )
    print(f"Bot: {response.text}")
    return response.text

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            print(f"You: {user_message}.")
            response_message = generator(user_message)
            return JsonResponse({"response": response_message})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
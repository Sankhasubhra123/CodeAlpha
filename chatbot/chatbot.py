import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import sys

# Ensure the necessary NLTK data is downloaded (runs silently)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

# --- 1. Define the Knowledge Base ---
# You can add more questions and answers here
faq_data = {
    "hello": "Hello! How can I help you with your CodeAlpha internship?",
    "hi": "Hi there! Feel free to ask me about the internship tasks.",
    "what is codealpha?": "CodeAlpha is a platform offering internships and tech education in various domains like AI, Web Dev, and App Dev.",
    "how do i submit my tasks?": "You need to upload your code to a GitHub repository named 'CodeAlpha_ProjectName' and submit the link via the Google Form.",
    "is the internship free?": "Yes, the internship is completely free of cost.",
    "what are the tasks?": "The tasks usually include a Language Translator, Chatbot, Tic-Tac-Toe AI, and Face Detection.",
    "when do i get the certificate?": "Certificates are usually issued after the internship period ends and your submission is verified.",
    "bye": "Goodbye! Best of luck with your coding."
}

# Separate questions and answers for processing
questions_list = list(faq_data.keys())

def get_response(user_input):
    # Clean the input
    user_input = user_input.lower().strip()
    
    # Direct match check (for simple greetings like 'bye')
    if user_input in faq_data:
        return faq_data[user_input]

    # --- 2. Vectorization (Convert text to numbers) ---
    # We add the user's input to the list of known questions to compare them
    all_texts = questions_list + [user_input]
    
    # TfidfVectorizer converts the text into mathematical vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # --- 3. Calculate Similarity ---
    # The last vector is the User Input, the others are the FAQ questions
    user_vector = tfidf_matrix[-1]
    question_vectors = tfidf_matrix[:-1]
    
    # Calculate cosine similarity
    similarity_scores = cosine_similarity(user_vector, question_vectors)
    
    # Find the index of the highest score
    best_match_index = np.argmax(similarity_scores)
    best_score = similarity_scores[0, best_match_index]
    
    # --- 4. Return Answer or Fallback ---
    # If the similarity is too low (below 0.2), we assume we don't know the answer
    if best_score > 0.2:
        matched_question = questions_list[best_match_index]
        return faq_data[matched_question]
    else:
        return "I'm sorry, I don't understand that question. Could you please rephrase?"

# --- Main Chat Loop ---
def start_chat():
    print("\n" + "="*40)
    print("   CodeAlpha FAQ Chatbot")
    print("   (Type 'bye' to exit)")
    print("="*40 + "\n")
    
    while True:
        try:
            user_text = input("You: ")
            if not user_text:
                continue
                
            response = get_response(user_text)
            print(f"Bot: {response}\n")
            
            if user_text.lower() == 'bye':
                break
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_chat()
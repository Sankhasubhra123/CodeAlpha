import tkinter as tk
from tkinter import ttk, messagebox
# We use deep_translator now, which works with Python 3.13
from deep_translator import GoogleTranslator

# Map common language names to codes manually since we changed libraries
LANGUAGES = {
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Portuguese': 'pt',
    'Hindi': 'hi',
    'Chinese (Simplified)': 'zh-CN',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Russian': 'ru',
    'Arabic': 'ar',
    'Bengali': 'bn'
}

def translate_text():
    source_text = text_input.get("1.0", "end-1c")
    target_lang_name = lang_combo.get()
    
    if not source_text.strip():
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    # Get the language code (e.g., 'es' for Spanish)
    target_code = LANGUAGES.get(target_lang_name)
    
    if not target_code:
        messagebox.showerror("Error", "Invalid language selected.")
        return

    try:
        # Perform translation
        translator = GoogleTranslator(source='auto', target=target_code)
        translated_text = translator.translate(source_text)
        
        text_output.delete("1.0", "end")
        text_output.insert("1.0", translated_text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"Check internet connection.\nError: {e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("CodeAlpha Task 1: Translator")
root.geometry("500x450")

# Title Label
tk.Label(root, text="Language Translator", font=("Arial", 16, "bold")).pack(pady=10)

# Input
tk.Label(root, text="Enter Text:").pack(pady=5)
text_input = tk.Text(root, height=5, width=50)
text_input.pack()

# Dropdown
tk.Label(root, text="Select Target Language:").pack(pady=5)
lang_combo = ttk.Combobox(root, values=sorted(list(LANGUAGES.keys())))
lang_combo.set("Spanish") 
lang_combo.pack()

# Button
tk.Button(root, text="Translate", command=translate_text, bg="lightblue", font=("Arial", 10, "bold")).pack(pady=15)

# Output
tk.Label(root, text="Translated Result:").pack(pady=5)
text_output = tk.Text(root, height=5, width=50)
text_output.pack()

root.mainloop()
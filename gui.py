import tkinter as tk
from chatbot import ask_gpt

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_log.insert(tk.END, f"You: {user_input}\n", 'user')
    entry.delete(0, tk.END)
    response = ask_gpt(user_input)
    chat_log.insert(tk.END, f"Bot: {response}\n\n", 'bot')

root = tk.Tk()
root.title("SmartStudy Bot")
root.geometry("500x600")
root.resizable(False, False)

chat_log = tk.Text(root, bg="#f5f5f5", font=("Arial", 12))
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_log.tag_config('user', foreground='blue')
chat_log.tag_config('bot', foreground='green')

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=(0, 10), fill=tk.X)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message, bg="#4CAF50", fg="white", font=("Arial", 12))
send_button.pack(pady=(0, 10))

# THIS LINE IS IMPORTANT: It starts the GUI loop
root.mainloop()

# GUI initialized

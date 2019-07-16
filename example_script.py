
import zwende

shown_text = "This is what you see."
hidden_text = "My super secret message."

print("Encoding the message.")
encoded_message = zwende.enzero(hidden_text, shown_text)
print("...")
print(f"Encoded Message: {encoded_message}")
print("Decoding the message.")
decoded_message = zwende.dezero(encoded_message)
print("...")
print(f"Decoded Message: {decoded_message}")

import pywhatkit

def send_whatsapp_message_and_contacts(phone_number, message):
    pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True)
    pywhatkit.sendwhats_image(phone_number, "contacts.png", caption="Here are my contacts.", wait_time=10, tab_close=True)

# Usage example
phone_number = "+91 9575354661"  # Replace with the victim's phone number
message = "Hello, can I have access to your WhatsApp chat history and contacts?"
send_whatsapp_message_and_contacts(phone_number, message)
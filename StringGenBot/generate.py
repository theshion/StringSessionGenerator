from pyrogram import Client
from telethon.sync import TelegramClient
from telethon.errors import PhoneCodeInvalid, PhoneNumberInvalid, TimeoutError
import time
import random
import string

# Function to generate random session name
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to generate session with given details
def generate_session(api_id_msg, api_hash_msg, phone_number_msg, otp_msg):
    try:
        # Extracting API ID and Hash
        api_id = int(api_id_msg.text)
        api_hash = api_hash_msg.text
        
        # Logging in with Pyrogram Client
        with Client(generate_random_string(), api_id, api_hash) as pyrogram_client:
            pyrogram_client.send_message(phone_number_msg.text, "OTP")
            time.sleep(5)
        
        # Wait and capture OTP
        otp = otp_msg.text
        
        # Handling the session with Telethon Client
        with TelegramClient(generate_random_string(), api_id, api_hash) as telethon_client:
            telethon_client.send_code_request(phone_number_msg.text)
            telethon_client.sign_in(phone_number_msg.text, otp)
            print(f"Session for {phone_number_msg.text} created successfully!")

    except PhoneCodeInvalid:
        print("Invalid OTP. Please try again.")
    except PhoneNumberInvalid:
        print("Invalid phone number. Please check the number entered.")
    except TimeoutError:
        print("Request timed out. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
# Example usage
generate_session(api_id_msg, api_hash_msg, phone_number_msg, otp_msg)

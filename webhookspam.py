import requests
import time

def send_to_discord(webhook_url, content, botName="bvqu", repeat=10, delay=1):
    """ Sends multiple messages to a Discord webhook. 
        - `repeat`: Number of messages to send.
        - `delay`: Delay between messages (in seconds).
    """
    data = {
        "content": content,
        "username": botName  
    }
    
    for i in range(repeat):
        response = requests.post(webhook_url, json=data)
        
        if response.status_code == 204:
            print(f"✅ [{i+1}/{repeat}] Message sent successfully.")
        else:
            print(f"❌ [{i+1}/{repeat}] Failed: {response.status_code} - {response.text}")
        
        time.sleep(delay)  # Prevents hitting rate limits

# User input
webhook = input("Webhook URL: ")
message = input("Message: ")
botName = input("Bot Name (default: bvqu): ") or "harm"
repeat = int(input("How many messages to send? "))
delay = float(input("Delay between messages (seconds): "))

# Start spamming
send_to_discord(webhook, message, botName, repeat, delay)

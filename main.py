from openai import OpenAI
from dotenv import find_dotenv, load_dotenv

import requests
import json
import random
import time
import datetime
load_dotenv()
# Set your OpenAI API key
api_key = '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'
client = OpenAI()
# Function to generate AI reply
def generate_reply(messages):
    # Combine input messages into a single string
    context = '\n'.join(messages)

    # Prompt with the conversation history
    prompt = f"Conversation:\n{context}\nAI:"

    # Generate a response from the AI model
    response = client.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt="""
            Reply with a general nuetral message with no grammar punctuation or capitalization that can be sent in any context and is at most 3 words long Some common terms chalking means bet misses, hitting means bet hits, selling means player is performing bad
                how does this guy sell
                what are my chances of hitting
                """,
      max_tokens=500,
      temperature=0.1
    )

    # Extract the generated reply from the response
    reply = response.choices[0].text.strip()

    return reply

# Example input messages
input_messages = [
    "You: Hey, how's it going?",
    "Friend: Not bad, just relaxing. What about you?",
    "You: Same here, just chilling at home."
]

# Generate a reply based on the input messages
generated_reply = generate_reply(input_messages)

# Print the generated reply
print("AI:", generated_reply)


get_url = "https://discord.com/api/v9/channels/689579821688291443/messages?limit=50"
url = "https://discord.com/api/v9/channels/689579821688291443/messages"
quack = "https://discord.com/api/v9/channels/896804250703757384/messages"
headers = {
    "Authorization" : "NDkwMzUzNTIyNjg1MTE2NDE2.G6FUSi.LOVPS_IqkbalgigToAdQWXYwaK7CwwR3WwKXa0"
}

current_time = datetime.datetime.now()
print("Current time:", current_time.strftime("%A"))

def task():
    string_list = ["sold","damn", "plays selling", "everything selling" , "why is everyone selling" , 
                   "barely even" ,"idk how im goin down bettin on promos","dam only app im up on is sports quack today",
                   "sq","m","can't hit a slip for the life of me","chalking crazy out here","pov can't hit a single player on a 4 man"]
    for _ in range(40):
        string_list.append(":pray:")
    for _ in range(20):
        string_list.append(":sob:")        
    for _ in range(20):
        string_list.append(":skull:")     
    for _ in range(20):
        string_list.append(":x:")
    for _ in range(20):
        string_list.append(":white_check_mark:")
    payload = {
        "content": random.choice(string_list)
    }
    res = requests.post(url,payload,headers=headers)
    return res


def morning_task():
    string_list = ["slips might chalk","cookin up some playz rn", "hopefully slips not gonna be chalking", 
                   "slips gonna be hittin" , "why is everyone selling" ,"idk y im betting im goin down bettin on promos",
                   "imma be bettin light today","sq","ez","imma be funding these dfs apps with these chalks","lines are tough today",
                   "we need more promos","all these line be in the opp direction i need them to be by .5 points","lookin tuf",
                   "why everyone selling","im really skipping some lines over half point lol","we need more promos",
                   "when next promo comin out","when next free square gonna be", "how many free squres do we need",
                   "for real tho when chess betting comin out i can help make the lines trus","is sq being laggy for any of u guys"]
    for _ in range(20):
        string_list.append(":grinning:")
    for _ in range(20):
        string_list.append(":sob:")        
    for _ in range(20):
        string_list.append(":skull:")     
    for _ in range(20):
        string_list.append(":pray:")
    for _ in range(20):
        string_list.append(":white_check_mark:")

    payload = {
        "content": random.choice(string_list)
    }
    res = requests.post(url,payload,headers=headers)
    return res

def retrieve_messages(channelid):
    headers = {
    "Authorization" : "NDkwMzUzNTIyNjg1MTE2NDE2.G6FUSi.LOVPS_IqkbalgigToAdQWXYwaK7CwwR3WwKXa0"
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit=5',headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        print(value['content'],"\n")
        print(value,"\n")
retrieve_messages("689579821688291443")
while True:
    time.sleep(random.randint(5,10))
    print(current_time.hour)
    if current_time.strftime("%A") == "Sunday" or current_time.strftime("%A") == "Saturday":   
        if current_time.hour > 11 and current_time.hour < 13:
            morning_task()
            time.sleep(random.randint(180,400))
        if current_time.hour >= 13 and current_time.hour <= 22:
            print("passed first cond")
            task()
            time.sleep(random.randint(480,600))
    else:
        if current_time.hour > 0 and current_time.hour < 19:
            morning_task()
            time.sleep(random.randint(480,600))
        if current_time.hour > 19 and current_time.hour < 22:
            task()
            time.sleep(random.randint(240,360))

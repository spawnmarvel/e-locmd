import random

def get_ran_response():
    response = ["Hi, how are you?", "Nice to see you again...", "Really...is you", "Great to see you.", "Hi!!", "Yes, well..", "No, or maybe"]
    answer = random.choice(response)
    return answer
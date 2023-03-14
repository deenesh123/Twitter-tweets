import re

def calculate_profanity(tweet, racial_slurs):
    # Split the tweet into sentences
    sentences = re.split('[.!?]', tweet)
    
    # Loop through each sentence and calculate the degree of profanity
    max_score = len(racial_slurs)
    profanity_scores = []
    for sentence in sentences:
        score = 0
        words = sentence.lower().split()
        for word in words:
            if word in racial_slurs:
                score += 1
        profanity_scores.append(score / max_score)
        
    return profanity_scores

# Load the racial slurs set
racial_slurs = set(['slur1', 'slur2', 'slur3', ...])

# Load the file of tweets
with open('tweets.txt', 'r') as f:
    tweets = f.readlines()

# Loop through each tweet and calculate the degree of profanity
for tweet in tweets:
    profanity_scores = calculate_profanity(tweet, racial_slurs)
    print(f'Tweet: {tweet}')
    print(f'Profanity scores: {profanity_scores}')

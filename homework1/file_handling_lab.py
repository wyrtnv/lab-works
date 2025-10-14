story_content = "My first book was Me and My Family. It gave me a chance to be known to the world." # Text to be written to the file.
with open('STORY.txt', 'w') as f: # Open file for writing.
    f.write(story_content) # Compose (write) the text.
    
count_me = 0 # Counter for 'me'.
count_my = 0 # Counter for 'my'.

with open('STORY.txt', 'r') as f: # Open file for reading.
    content = f.read() # Go through the entire text.
    normalized_content = content.lower() # Change the case to lowercase (case-insensitive search).
    words = normalized_content.split() # Split text into a list of words.
    
for sord in words: # Loop through each word.
    clean_word = sord.strip('.,!?"') # Take the punctuation out of the word.
    if clean_word == 'me': # Check if word is 'me'.
        count_me += 1 # Increment 'me' count.
    elif clean_word == 'my': # Check if word is 'my'.
        count_my += 1 # Increment 'my' count.
        
print(f"Quantity 'me': {count_me}") # Display final 'me' count.
print(f"Quantity 'my': {count_my}") # Display final 'my' count.
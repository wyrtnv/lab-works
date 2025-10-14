text_to_write = "I LOVE PROGRAMMING!"
with open('sentence.txt', 'w') as f:
    f.write(text_to_write)
    
with open('sentence.txt', 'r') as f:
    content = f.read()
    words = content.split()

print("Words printed separately:")
for word in words:
    print(word)
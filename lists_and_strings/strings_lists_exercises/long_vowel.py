vowels = "aeiou"

text = "scoot the door open for the cheese"
new_text = ""

n = 0
while n < len(text):
  if text[n] in vowels and (n+1) < len(text):
    if text[n] == text[n+1]:
      new_text = new_text + (text[n] * 3)
    else:
      new_text = new_text + text[n]
  else:
    new_text = new_text + text[n]
  n = n + 1

print(new_text)
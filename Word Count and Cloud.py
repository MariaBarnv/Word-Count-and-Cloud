import matplotlib.pyplot as plt

text = input("text: ")  # Input the text
# text:
# The Temple of Apollo Palatinus was a temple to the god Apollo in Rome, constructed on the Palatine Hill on the initiative of Augustus between 36 and 28 BCE. It was associated with Augustus's victories at the battles of Naulochus and Actium; the latter was extensively memorialised through its decoration. The temple represented the restoration of Rome's golden age and Augustus's devotion to religious and political duty. Its precinct was used for diplomatic functions and meetings of the Roman Senate.
words = text.split()

cword_4 = {}
word_uppercase = {}

for word in words:
    if len(word) > 4:
        cword_4[word] = cword_4.get(word, 0) + 1

for word in words:
    if any(letter.isupper() for letter in word):
        word_uppercase[word] = word_uppercase.get(word, 0) + 1

t10_4 = sorted(cword_4.items(), key=lambda x: x[1], reverse=True)[:10]
t10_uppercase = sorted(word_uppercase.items(), key=lambda x: x[1], reverse=True)[:10]

plt.figure(figsize=(10, 6))
plt.bar(range(len(t10_4)), [count for word, count in t10_4], align="center")
plt.xticks(range(len(t10_4)), [word for word, count in t10_4], rotation=45)
plt.xlabel("Words")
plt.ylabel("Occurrences")
plt.title("Top 10 Most Common Words with More Than 4 Letters")
plt.tight_layout()


plt.figure(figsize=(10, 6))
plt.bar(range(len(t10_uppercase)), [count for word, count in t10_uppercase], align="center")
plt.xticks(range(len(t10_uppercase)), [word for word, count in t10_uppercase], rotation=45)
plt.xlabel("Words")
plt.ylabel("Occurrences")
plt.title("Top 10 Most Common Words with at Least One Uppercase Letter")
plt.tight_layout()


plt.show()
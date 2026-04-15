from endee import Endee

db = Endee()

query = input("Enter your question: ")

results = db.search(query)

print("Results:")
for r in results:
    print(r)

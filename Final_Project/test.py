from Embedder import Embedder

dictionary = ["haha", "heihei", "hoho"]

embedder = Embedder(dictionary, (4, 8, 20))

print(embedder.embed("haha"))
print(embedder.embed("haha"))

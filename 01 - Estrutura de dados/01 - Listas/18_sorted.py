linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

print(sorted(linguagens))  # ["c", "csharp", "java", "js", "python"]
print(sorted(linguagens, reverse=True))  # ["python", "js", "java", "csharp", "c"]

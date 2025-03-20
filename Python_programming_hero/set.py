languages = {'ruby','javascript' ,'python' }
print(languages)
for language in languages:
    if "python" in language:
        print(language)
        break
else:
    print("python not found in the set")
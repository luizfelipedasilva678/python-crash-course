from http import client

favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}


# print(favorite_languages["jen"])
# print(favorite_languages.get("jen", "Key doesnt exists"))

# for name, language in favorite_languages.items():
# print(name, language)

"""print("___________")

for key in favorite_languages:
    print(key)

for name in sorted(favorite_languages):
    print(name)
    """

languages = set()

for language in favorite_languages.values():
    languages.add(language)

print(languages)

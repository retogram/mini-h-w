from distutils import command

DATABASE = {
    "rich": "poor",
    "fair, just": "unfair, unjust",
    "ill": "healthy",
    "big": "small",
    "try": "leave",
    "quickly": "slowly",
    "exact, precise": "inaccurate, inexact",
    "fast": "slow",
    "thin": "strong",
    "stop": "begin",
    "liberty": "captivity",
    "optimistic": "pessimist",
    "cruel, merciless": "kind, humane",
    "even, smooth": "rough, uneven",
    "silly": "clever",
    "ugly": "bеautiful",
    "hot": "cold",
    "attentive": "inattentive",
    "faithful, loyal": "unfaithful, disloyal",
    "cheerful": "sad",
    "loving": "bitter",
    "together": "separately",
    "about": "exactly",
    "dry": "wet",
    "various": "identical",
    "evident, obvious, clear": "vague, obscure",
    "front": "back",
    "thick": "slim",
    "above": "below",
    "new": "old",
    "educated": "ignorant",
    "dead": "alive",
    "empty": "full",
    "young": "mature",
    "lazy": "agile",
    "fresh": "stale",
    "famous, well-known": "uknown",
    "brave, bold": "afraid, frightened",
    "absence": "presence",
    "best": "worst",
    "abundance": "lack",
    "funny": "serious"
}
print('''HELLO!!!
My dictionary of antonyms welcomes you.
       ''')
while True:
    command_ = input(
        'Get a list of available words, type /list.\nTo get the entire dictionary, type /dictionary.\nЕnter command: '
    )

    if command_ == "/list":
        print(", ".join(DATABASE.keys()))
        break
    elif command_ == "/dictionary":
        for i, j in DATABASE.items():
            print(i, '-', j)
    else:
        print('You entered the wrong command, please try again!')
while True:
    word = input("Enter a word from the list: ")

    for antonym1, antonym2 in DATABASE.items():
        if word in antonym1:
            print('antonym of', word, 'is', antonym2)
            break
    else:
        print(f"the word {word} is not in the list")

    out = input('Press enter to continue or to exit type /out. ')
    if out == "/out":
        break

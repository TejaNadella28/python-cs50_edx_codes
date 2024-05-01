def replace_emoticons(text):
    emoticons = {
        ":)": "🙂",
        ":(": "🙁"
    }
    for emoticon, emoji in emoticons.items():
        text = text.replace(emoticon, emoji)
    return text

def main():
    user_input = input()
    print(replace_emoticons(user_input))

if __name__ == "__main__":
    main()

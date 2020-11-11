import emoji
    
def good_vibes(input):
    print(emoji.emojize('Awesome! :thumbs_up:'))

def bad_vibes(input):
    print(emoji.emojize("Awh... Sorry to hear that :disappointed_relieved:"))
    

def main():
    mood = input("Are you doing good or bad today? ")
    
    if mood == "good":
        good_vibes(mood)

    elif mood == "bad":
        bad_vibes(mood)

    else:
        print("I can't help you there bud you gotta answer my question... :confused:")
        

if __name__ == "__main__":
    main()

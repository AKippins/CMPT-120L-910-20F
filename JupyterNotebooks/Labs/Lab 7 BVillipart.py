import emoji
    
#def good_vibes(input):
   # print(emoji.emojize('Awesome! :thumbs_up:'))

#def bad_vibes(input):
    #print(emoji.emojize("Awh... Sorry to hear that :disappointed_relieved:"))

    
if __name__ == "__main__":

    print(emoji.emojize("We should get starbucks after class today Kelly!! :thumbs_up:"))
    print(emoji.emojize("O-M-Frickin G Sarah that sounds like so much frickin fun! :red_heart:",variant="emoji_type"))
    print(emoji.emojize('Starbucks is so :thumbsdown: !! I like dunkin more...', use_aliases=True))
    print(emoji.demojize('oh my heck Bailey you just shattered my friggin ❤!!'))
    print(emoji.demojize('I can\'t believe you would say I shattered your friggin ❤!!'), emoji.emojize('You\'re suppose to say it like this!! :red_heart:',variant="emoji_type"))
    print(emoji.demojize('That\'s not even physically possible to say an emoji like that. How are you saying ❤ out loud?!'))
    print(emoji.emojize('You know what, we don\'t even wanna get coffee with you anymore! :rage:', use_aliases=True))

#    mood = input("Are you doing good or bad today? ")
    
#    if mood == 'good':
#        good_vibes(mood)

 #   elif mood == 'bad':
 #       bad_vibes(mood)

 #   else:
  #      print("I can't help you there bud you gotta answer my question...:confused:")

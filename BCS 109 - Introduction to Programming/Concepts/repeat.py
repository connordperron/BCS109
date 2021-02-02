namePrompt ="\nWhat's your name? "
placePrompt = "If you could visit one place, where would it be? "
continuePrompt = "\nWould you like to let someone else respond? "


responses = {}

while True:
    name = input(namePrompt)
    place = input(placePrompt)

    responses[name]=place

    repeat = input(continuePrompt).lower()
    if repeat != 'yes':
        break

for name,place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}")

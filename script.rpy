## The script of the game goes in this file.

## All assets have been commented out, since I am not uploading the files to Github.
## Asset files were released under Creative Commons license. Link to the individual locations available in source.txt

define t = Character("Tara")
define e = Character("EVE")

image hallway = #"hallway.png"
image space = #"game_menu.png"
image tara happy = #"SpaceGal-Happy.png"
image tara surprise = #"SpaceGal-Surprised.png"
image tara main = #"SpaceGal-Neutral.png"
image tara mad = #"SpaceGal-Angry.png"
image tara enthused = #"SpaceGal-Enthused.png"

## The game starts here.

label start:

    stop music fadeout 1

    scene black

    "Tara?"

    "..."

    "Tara."

    with vpunch

    "WAKE UP."

    scene hallway
    with Dissolve(.8)

    play music #"01 Solace.mp3"

    show tara surprise

    "I bolt upright in my chair."

    t "Argh!"

    "I did it again. I fell asleep during my favourite show. At this rate I'm never going to finish the season."

    "How long was I asleep? And why hasn't one of the robots brought me coffee?"

    show tara main

    t "EVE?"

    e "Congradulations on your return to cognizance."

    show tara mad

    t "And you had nothing to do with that..."

    e "I am merely following the timetable set up by your mother before her departure."

    t "Lucky me."

    e "She was very specific."

    show tara main

    t "No doubt."

    "No doubt because she threatened to rewrite EVE's primary processes should she fail. Mom can be a bit of a control freak. Even when she's not around."

    t "Great. Well now that I'm awake I'll just--"

    e "Wait. We must discuss your schedule for today."

    menu:
        "Okay, go ahead.":
            jump duty

        "Ugh, not before I get my coffee.":
            jump coffee

    label duty:
    e "Excellent. Your mother has a set of specific algorithims that have to be programmed into the flight computer."

    t "Honestly? I hate to sound like an AI-bigot, but isn't that something you'd be better off doing?"

    e "A not insignificant percentage of my memory databanks is storing unwatched episodes of your various holovid dramas. Your mother surmised that such menial work might inspire you to reduce that percentage."

    "Mom can be such a bitch."

    "And so that was how my day was spent. Data entry and basic math. You would think that living on a space ship would be more exciting, but no."

    ".:. Boring Ending."

    call credits
    return #ending: Boring

    label coffee:

    e "Yes. About that. Your mother figured you needed the extra motivation to complete your assigned duties. So she ejected all of your coffee supplies into space."

    show tara surprise:
        parallel:
            ease .5 zoom 1.5
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5

    t "WHAT?"

    t "Why? Why would she do such a horrible thing?"

    show tara mad at default

    e "She instructed me to tell you it is due to wanting you to understand the gravity of your adulthood role onboard this ship and not at all related to you erasing her collection of vintage Bowie music files."

    t "It was an honest mistake! And who names their important files Keep This and Stay Out anyways?"

    e "You mother does. Or did."

    "The die is cast. Or some metaphor like it."

    menu:
            "She will regret this!":
                jump revenge

            "Forget vengeance, I have to rescue those coffee beans!":
                jump caffeine

label revenge:

    e "Are you thinking at full mental capacity?"

    t "For that I would need coffee. So clearly not."

    "Mother should know better. She escalated this situation already. I'm just following her example by teaching her a lesson."

    "Yeah. That seems something that a legitimate adult would say."

    "So I go and delete her Janelle Monae music files as well. Check. And. Mate."

    ".:. Petty Passive Agressive Ending"

call credits
return #ending: Revenge

label caffeine:

    e "Are you thinking at full mental capacity?"

    t "For that I would need coffee. So clearly not."

    show tara enthused

    t "Time to suit up!"

    e "...You slept in your helmet. Again."

    t "Its so cozy!"

    "EVE doesn't respond."

    stop music fadeout 1

    scene space
    with Dissolve(.8)

    play music #"21 Halo.mp3"

    "Space. Its really big and stuff. Might be hard to find my coffee unless I get help."

    t "Eve! Set the scanner for organic matter resembling my coffee beans."

    e "...Setting scanner."

    show tara enthused

    t "SCAN!"

    e "..."

    e "..."

    e "1.2 metres to your left. Follow the blinker in your helmet."

    t "Off I go!"

    hide tara enthused

    "Floating in space is hard. Maybe I should've paid more attention in school."

    t "Look! The beans!"

    "I reach out and grab them. Success! Now I just need to figure out how to get back to the ship..."

    ".:. Caffeinated Ending"

call credits
return #ending: Caffeinated

label credits:
    $ credits_speed = 20 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return

init python:
    credits = ('Writing', 'Surly Alpaca '), ('Backgrounds', 'Airgoof'), ('Backgrounds', 'Konett'), ('Sprites', 'Adryn'), ('Programming', 'Surly Alpaca'), ('Music', 'Tettrix')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version()

init:
    image cred = Text(credits_s, font="MavenPro-Regular.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)

return

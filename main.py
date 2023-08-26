def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
    music.play(music.string_playable("G D F A C E D C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C D E F G A B C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 A B G A F G E ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("G B A G C5 B A B ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("B A G A G F A C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("E G A F F A G D ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C D F E E F D C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("D G A D A F D C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C D F B A E A B ", 120),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_icon(IconNames.DUCK)
    music.play(music.string_playable("B G E C D F C B ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 B A G F E D C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 B A G F E D C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 B F E B E D A ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("F G D F D F E C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C B D G D F D A ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("G B A G C5 B A B ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 B C5 F E D A C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("E C F D F F C C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("B A G A G F A C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("B A D G E D F G ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 E B D E A F C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.GHOST)
    music.play(music.string_playable("D F A F E G E F ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("G B D F A G B G ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("B A F D E D D C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("B A F D E D D C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("F D G D A F D E ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("F D E C F E G C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("D B C5 G E B E C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("D B C5 G E B E C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("D B F C A F G D ", 120),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.show_icon(IconNames.DUCK)
    music.play(music.string_playable("B G E C D F C B ", 120),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

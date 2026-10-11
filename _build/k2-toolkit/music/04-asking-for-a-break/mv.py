# Music video timing for Topic 4 · Asking for a Break ("Break Please").
# Build:  python3 music/build_mv.py 04-asking-for-a-break --clips DIR
# Caption times come from OCR of the bold (sung) line in the Suno lyric video. Where Suno's wrap hid a line's
# first words ("Break card", "When I", "Too much"), the start is set just before the first bold fragment.
# Shared-part clips are reused from Gentle Hands (gh_*).

SONG = 'song-source.mp4'
CLIPS = 'clips'
TITLE = 'ASK FOR A BREAK'
SUBTITLE = 'Morning Meeting · K–2'
TITLE_LAYOUT = 'frame'            # title above a framed video, so it never covers a face
TITLE_UNTIL = 7.4
OPENING_CROP = (258, 8, 764, 430)  # zoom the intro clip to Lee and Tee, head to waist
BPM = 92.285                      # librosa: 92.3 tempo, first beat 0.17
BEAT0 = 0.17
SNAP_UNTIL = 83
CLIP_LEN = 8.05
END = 84.3

# (end_time, clip, src_in[, speed])
SEG = [(7.5, 'gh_wave', 0.0),
       # hook: break card high, ask, come back
       (11.2, 'abv_hero', 0.3), (14.0, 'abv_s1', 0.3), (16.3, 'abv_back', 0.5),
       # verse 1: loud center time, Lee asks, teacher says yes, timer
       (24.2, 'abv_loud', 0.1), (29.6, 'abv_card', 0.3), (33.2, 'abv_timer', 0.3),
       # chorus (shared)
       (36.4, 'gh_promise', 0.0), (41.2, 'gh_breathe', 1.0), (43.3, 'gh_corner', 2.0), (45.4, 'gh_break', 2.0),
       (47.4, 'gh_grownup', 1.0),
       # verse 2: card or words, wait for a yes, sand goes down, back to class
       (50.6, 'abv_s1', 3.5), (53.8, 'abv_card', 4.0), (55.8, 'abv_timer', 4.0), (59.3, 'abv_back', 3.0),
       # chorus (shared)
       (62.4, 'gh_promise', 0.5), (67.2, 'gh_breathe', 2.6), (69.3, 'gh_corner', 5.3), (71.4, 'gh_break', 5.0),
       (75.2, 'gh_grownup', 2.6),
       # outro
       (77.4, 'abv_hero', 4.0), (79.3, 'gh_promise', 0.3), (84.3, 'abv_s4', 1.0)]

# (start_time, caption). Text in (parentheses) is the echo, drawn yellow.
LYR = [(0.4, 'Matchbook, are you ready? (Ready!)'), (2.0, 'Hands up high, hands down low,'), (5.2, "Let's learn it, let's go!"),
       (7.5, 'Break card (break card!), hold it high,'), (9.8, 'Use my words (use my words!), I give it a try:'),
       (11.2, '"Can I have a break, please?" Wait for a yes,'), (14.0, "Take a break, come back, I'm doing my best!"),
       (16.3, 'It was center time and the room got loud,'), (20.2, 'Blocks crashing down, such a noisy crowd.'),
       (21.6, 'My ears felt full and my body got tight,'), (24.2, "I didn't run off, I asked it right."),
       (27.2, 'I held up my card, my teacher said, "Yes!"'), (29.6, 'I sat with the timer and I took a rest.'),
       (33.2, 'When I feel mad, I can choose! (I can choose!)'), (36.4, 'Breathe in slow, blow it out, whoo!'),
       (41.2, 'Calm corner, break card, use my words,'), (45.4, "Ask a grown-up, I get help, that's how it works!"),
       (47.4, "Card or words (card or words!), that's how I ask,"), (50.6, "Wait for a yes (wait for a yes!), that's my task."),
       (53.8, 'Sand goes down while I breathe real slow,'), (55.8, "Timer's done, back to class I go!"),
       (59.3, 'When I feel mad, I can choose! (I can choose!)'), (62.4, 'Breathe in slow, blow it out, whoo!'),
       (67.2, 'Calm corner, break card, use my words,'), (71.4, "Ask a grown-up, I get help, that's how it works!"),
       (75.2, 'Too much? (I ask for a break!)'), (77.4, 'Hand on your heart, say it with me:'),
       (79.3, 'I can ask for a break with my words or my card.')]

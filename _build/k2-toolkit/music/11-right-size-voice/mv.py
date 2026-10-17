# Music video timing for Topic 11 · Right-Size Voice ("Turn My Dial").
# Build:  python3 music/build_mv.py 11-right-size-voice --clips DIR
# Caption times: OCR of the Suno lyric video (lines highlight about 1.5 s early) plus a chroma + MFCC alignment against
# the Topic 9 song (same tempo 92.285 BPM, first beat about 0.17 s, same section layout). Line starts sit on the bar grid
# (7.34 + 2.60 k); verse 1 opens just after its bar.
# Every lyric line has its own matching shot, in the order of the school day: Lee looks around and turns her dial (hook,
# the dial close-up is a Veo 3.1 Quality clip), the teacher reading to the rug (0), the hallway (0), partner reading and
# whispering (1), the lunch table at 2, voices creeping up, Lee turning the dial and the table copying her, the calm
# table with the lunch helper's thumbs up, Tee presenting (3), the gym pass (3), recess (4, a slow push-in on the picture
# because Flow credits ran out), and the class walking back inside at 0. Shared-part clips are reused from Gentle Hands
# (gh_*); the final high five reuses the Topic 10 hero clip (swv_hero).

SONG = 'song-source.mp4'
CLIPS = 'clips'
TITLE = 'RIGHT-SIZE VOICE'
SUBTITLE = 'Morning Meeting · K–2'
TITLE_LAYOUT = 'frame'            # title above a framed video, so it never covers a face
TITLE_UNTIL = 7.2
OPENING_CROP = (258, 8, 764, 430)  # zoom the intro clip to Lee and Tee, head to waist
BPM = 92.285
BEAT0 = 0.17
SNAP_UNTIL = 85
CLIP_LEN = 8.05
END = 91.5

# (end_time, clip, src_in[, speed])
SEG = [(7.35, 'gh_wave', 0.0),
       # hook: look around, who needs to hear me (chin tap), turn my dial (close-up), right-size voice (her grin)
       (9.95, 'rvv_look', 0.3), (12.55, 'rvv_look', 3.0), (15.1, 'rvv_dialcu', 0.5), (17.85, 'rvv_dialcu', 4.0),
       # verse 1: teacher talking (0), hallway (0), partner reading and the whisper (1), lunch at 2, voices creep up,
       # Lee turns her dial ("Let's take it back to two!"), the whole table turns it down
       (20.35, 'rvv_talk', 0.5), (22.95, 'rvv_hall', 0.3), (25.5, 'rvv_partner', 0.3), (28.1, 'rvv_partner', 4.0),
       (30.7, 'rvv_lunch', 0.5), (33.3, 'rvv_loud', 0.3), (35.9, 'rvv_dial', 0.5), (38.5, 'rvv_calm', 0.5),
       # chorus (shared)
       (43.4, 'gh_promise', 0.0), (48.3, 'gh_breathe', 1.0), (49.6, 'gh_corner', 2.0), (50.9, 'gh_break', 2.0),
       (54.15, 'gh_grownup', 1.0),
       # verse 2: presenting (3), gym team game (3), recess (4), bell rings and the class walks back inside at 0
       (56.75, 'rvv_present', 0.3), (59.35, 'rvv_gym', 0.3), (61.95, 'rvv_recess', 0.5), (64.55, 'rvv_hall', 4.0),
       # chorus (shared)
       (69.4, 'gh_promise', 0.5), (74.3, 'gh_breathe', 2.6), (75.6, 'gh_corner', 5.3), (76.85, 'gh_break', 5.0),
       (79.5, 'gh_grownup', 2.6),
       # outro: too loud (Lee noticing), turn my dial, hand on heart, Lee and Tee high five and wave goodbye
       (80.8, 'rvv_loud', 4.6), (82.1, 'rvv_dialcu', 2.0), (85.6, 'gh_promise', 0.3), (91.5, 'swv_hero', 2.0)]

# (start_time, caption). Text in (parentheses) is the echo, drawn yellow.
LYR = [(0.2, 'Matchbook, are you ready? (Ready!)'), (3.4, 'Hands up high, hands down low,'), (5.7, "Let's learn it, let's go!"),
       (7.35, 'Look around (look around!), where am I?'), (9.95, 'Who needs to hear me? Pick my number right!'),
       (12.55, 'Turn my dial (turn my dial!), up or down,'), (15.1, 'Right-size voice, all around!'),
       (17.85, "Teacher's talking to the group? Zero, eyes on her face,"), (20.35, 'Walking down the hallway? Zero, quiet in my place.'),
       (22.95, 'Reading with my partner? One, a whisper soft and low,'),
       (25.5, 'Just loud enough for my buddy, nobody else needs to know.'),
       (28.1, 'Lunchtime! Two at the table, laughing with my crew,'), (30.7, 'But the voices got louder, three, then four, whoo!'),
       (33.3, 'I looked around, turned my dial: "Let\'s take it back to two!"'),
       (35.9, 'The whole table turned it down, and now I can hear you!'),
       (38.5, 'When I feel mad, I can choose! (I can choose!)'), (43.4, 'Breathe in slow, blow it out, whoo!'),
       (48.3, 'Calm corner, break card, use my words,'), (50.9, "Ask a grown-up, I get help, that's how it works!"),
       (54.15, 'Presenting my picture? Three (three!), loud and clear,'), (56.75, 'Gym class team game? Three! "I\'m open! Over here!"'),
       (59.35, 'Recess, big blue sky? Four (four!), "Race you to the slide!"'),
       (61.95, 'Bell rings, check it again: back to zero, walking inside!'),
       (64.55, 'When I feel mad, I can choose! (I can choose!)'), (69.4, 'Breathe in slow, blow it out, whoo!'),
       (74.3, 'Calm corner, break card, use my words,'), (76.85, "Ask a grown-up, I get help, that's how it works!"),
       (79.5, 'Too loud? Too soft? (Look around! Who needs to hear me? Turn my dial!)'),
       (82.1, 'Hand on your heart, say it with me:'), (85.6, 'I use the right voice for the place.')]

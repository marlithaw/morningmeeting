# Music video timing for Topic 10 · School Words ("Stand Tall, Strong Voice").
# Build:  python3 music/build_mv.py 10-school-words --clips DIR
# Caption times: OCR of the Suno lyric video (which highlights each line about 1.5 s early) plus a chroma + MFCC
# alignment against the Topic 9 song (same tempo 92.285 BPM, first beat 0.19 s, same section layout). Line starts sit
# on the bar grid (7.34 + 2.60 k); verse 1 opens with a pickup ("Recess bell!") just before its bar.
# Every lyric line has its own matching shot: Tee first in line, Diego cuts, Tee's hot face, the breath and standing
# tall, the words, "Oh, sorry!", then Kiara takes Lee's marker and gives it back, Malik laughs, Lee says stop, Lee tells
# the teacher. The teasing line is sung "Malik, not kind. Stop that!" (no please), so the caption matches the song.
# Shared-part clips are reused from Gentle Hands (gh_*). Lee and Tee never say a mean word on screen.

SONG = 'song-source.mp4'
CLIPS = 'clips'
TITLE = 'SCHOOL WORDS'
SUBTITLE = 'Morning Meeting · K–2'
TITLE_LAYOUT = 'frame'            # title above a framed video, so it never covers a face
TITLE_UNTIL = 7.2
OPENING_CROP = (258, 8, 764, 430)  # zoom the intro clip to Lee and Tee, head to waist
BPM = 92.285
BEAT0 = 0.19
SNAP_UNTIL = 85
CLIP_LEN = 8.05
END = 90.4

# (end_time, clip, src_in[, speed])
SEG = [(7.35, 'gh_wave', 0.0),
       # hook: stand tall, look their way, strong voice, say their name and please, strong kind school words
       (9.95, 'swv_tall', 2.5), (12.55, 'swv_words', 0.3), (15.1, 'swv_words', 3.0), (17.0, 'swv_hero', 0.2),
       # verse 1: first by the door, Diego slides in, hot face, breathe and stand tall, look at him, the words,
       # "Oh, sorry!" and he steps back, the line heads out to recess
       (20.35, 'swv_line', 0.3), (22.95, 'swv_cut', 0.2), (25.5, 'swv_cut', 3.5), (28.1, 'swv_tall', 0.2),
       (30.7, 'swv_tall', 4.5), (33.3, 'swv_words', 0.5), (35.9, 'swv_sorry', 0.2), (38.5, 'swv_sorry', 4.0),
       # chorus (shared)
       (43.4, 'gh_promise', 0.0), (48.3, 'gh_breathe', 1.0), (49.6, 'gh_corner', 2.0), (50.9, 'gh_break', 2.0),
       (54.15, 'gh_grownup', 1.0),
       # verse 2: Kiara takes the marker then gives it back, Malik laughs, Lee says stop and stays calm while he keeps
       # giggling (mad is okay, mean words are not), so she goes to get the teacher
       (55.45, 'swv_take', 0.8), (56.75, 'swv_marker', 1.5), (58.05, 'swv_tease', 0.5), (61.95, 'swv_stop', 0.3),
       (64.55, 'swv_teacher', 0.5),
       # chorus (shared)
       (69.4, 'gh_promise', 0.5), (74.3, 'gh_breathe', 2.6), (75.6, 'gh_corner', 5.3), (76.85, 'gh_break', 5.0),
       (79.5, 'gh_grownup', 2.6),
       # outro: stand tall, strong voice; hand on heart; Lee and Tee high five and wave goodbye
       (82.1, 'swv_hero', 0.2), (85.3, 'gh_promise', 0.3), (90.4, 'swv_hero', 2.6)]

# (start_time, caption). Text in (parentheses) is the echo, drawn yellow.
LYR = [(0.2, 'Matchbook, are you ready? (Ready!)'), (3.4, 'Hands up high, hands down low,'), (5.7, "Let's learn it, let's go!"),
       (7.35, 'Stand tall (stand tall!), look their way,'), (9.95, "Strong voice (strong voice!), here's what I say:"),
       (12.55, 'Say their name, then "please," and what I need,'), (15.1, "Strong, kind school words, that's the key!"),
       (17.0, 'Recess bell! I was first by the door,'), (20.35, 'Then Diego slid in where I stood before.'),
       (22.95, 'My face got hot, mean words ready to fall,'), (25.5, 'But I breathed in slow and I stood up tall.'),
       (28.1, 'I looked right at him, strong, not loud:'), (30.7, '"Diego, I was here first. Please go behind me now."'),
       (33.3, 'He said, "Oh, sorry!" and he stepped right back,'), (35.9, 'Strong, kind words keep us all on track!'),
       (38.5, 'When I feel mad, I can choose! (I can choose!)'), (43.4, 'Breathe in slow, blow it out, whoo!'),
       (48.3, 'Calm corner, break card, use my words,'), (50.9, "Ask a grown-up, I get help, that's how it works!"),
       (54.15, 'Took my marker? (Took my marker!) "Kiara, please give it back!"'),
       (56.75, 'Laughing at me? (Laughing at me!) "Malik, not kind. Stop that!"'),
       (59.35, 'Mad is okay (mad is okay!), but mean words? No way!'), (61.95, 'Still happening? I get a grown-up right away!'),
       (64.55, 'When I feel mad, I can choose! (I can choose!)'), (69.4, 'Breathe in slow, blow it out, whoo!'),
       (74.3, 'Calm corner, break card, use my words,'), (76.85, "Ask a grown-up, I get help, that's how it works!"),
       (79.5, 'Feeling mad? (Stand tall, strong voice!)'), (82.1, 'Hand on your heart, say it with me:'),
       (85.3, 'I use strong, kind school words.')]

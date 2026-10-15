# Music video timing for Topic 9 · Things Stay Safe ("Put It Down, Put It Back").
# Build:  python3 music/build_mv.py 09-things-stay-safe --clips DIR
# Caption times come from OCR of the bold (sung) line in the Suno lyric video, checked against the vocal onsets and the
# 92.285 BPM bar grid (hook, verse, and chorus starts sit on bars: 7.34 + 2.60 k). Verse 1 is 8 lines in this song.
# Every lyric line has its own matching shot: the story beats follow the lesson (drawing the tree, the scribble, mad and
# stuck, crayon down, breathe, ask for help, the bird's nest, crayons back in the box, markers in the cup).
# Shared-part clips are reused from Gentle Hands (gh_*). Lee never throws on screen; "throwing is not" shows her
# choosing to put the crayon down.

SONG = 'song-source.mp4'
CLIPS = 'clips'
TITLE = 'THINGS STAY SAFE'
SUBTITLE = 'Morning Meeting · K–2'
TITLE_LAYOUT = 'frame'            # title above a framed video, so it never covers a face
TITLE_UNTIL = 7.2
OPENING_CROP = (258, 8, 764, 430)  # zoom the intro clip to Lee and Tee, head to waist
BPM = 92.285
BEAT0 = 0.19
SNAP_UNTIL = 85
CLIP_LEN = 8.05
END = 91.0

# (end_time, clip, src_in[, speed])
SEG = [(7.35, 'gh_wave', 0.0),
       # hook: put it down, breathe, ask for help then back it goes, our things stay safe
       (9.95, 'tsv_down', 1.0), (12.55, 'tsv_breathe', 2.5), (13.85, 'tsv_help', 0.2), (15.1, 'tsv_back', 1.0),
       (17.75, 'tsv_hero', 0.2),
       # verse 1: drawing the tree, green leaves (the scribble clip starts with happy coloring), the zigzag,
       # mad and stuck, crayon down, breathe, raise a hand to ask, the bird's nest
       (20.35, 'tsv_draw', 0.1), (25.5, 'tsv_scribble', 0.2), (28.1, 'tsv_mad', 0.5), (30.7, 'tsv_down', 0.8),
       (33.3, 'tsv_breathe', 0.3), (35.9, 'tsv_help', 0.2), (38.5, 'tsv_nest', 0.5),
       # chorus (shared)
       (43.4, 'gh_promise', 0.0), (48.3, 'gh_breathe', 1.0), (49.6, 'gh_corner', 2.0), (50.9, 'gh_break', 2.0),
       (54.15, 'gh_grownup', 1.0),
       # verse 2: crayons back in the box, markers in the cup, mad is okay (her mad face) but throwing is not (she puts
       # it down instead), then the four steps as a one-beat-each montage
       (56.75, 'tsv_back', 3.0), (59.35, 'tsv_cup', 0.3), (60.65, 'tsv_mad', 4.0), (61.95, 'tsv_down', 2.0),
       (62.6, 'tsv_down', 2.4), (63.25, 'tsv_breathe', 1.0), (63.9, 'tsv_help', 0.4), (64.55, 'tsv_back', 1.6),
       # chorus (shared)
       (69.4, 'gh_promise', 0.5), (74.3, 'gh_breathe', 2.6), (75.6, 'gh_corner', 5.3), (76.85, 'gh_break', 5.0),
       (79.5, 'gh_grownup', 2.6),
       # outro: a calm breath, hand on heart, Lee and Tee high five and wave goodbye at the tidy art table
       (82.1, 'tsv_breathe', 4.5), (85.6, 'gh_promise', 0.3), (91.0, 'tsv_hero', 2.6)]

# (start_time, caption). Text in (parentheses) is the echo, drawn yellow.
LYR = [(0.2, 'Matchbook, are you ready? (Ready!)'), (3.4, 'Hands up high, hands down low,'), (5.7, "Let's learn it, let's go!"),
       (7.35, 'Put it down (put it down!), soft and slow,'), (9.95, 'Breathe in (breathe in!), let the mad go.'),
       (12.55, 'Ask for help (help me, please!), then back it goes,'), (15.1, 'Our things stay safe, and everybody knows!'),
       (17.75, "Art time, art time, I'm drawing a tree,"), (20.35, 'Green leaves, brown trunk, for my family.'),
       (22.95, 'Then a big scribble zigzagged right through,'), (25.5, "I felt mad, I felt stuck, didn't know what to do."),
       (28.1, 'My hands wanted to throw, but I put it down slow,'), (30.7, 'Breathed in, breathed out, and I let the mad go.'),
       (33.3, 'Then I raised my hand: "Can you help me, please?"'), (35.9, "We turned that scribble into a bird's nest in my tree!"),
       (38.5, 'When I feel mad, I can choose! (I can choose!)'), (43.4, 'Breathe in slow, blow it out, whoo!'),
       (48.3, 'Calm corner, break card, use my words,'), (50.9, "Ask a grown-up, I get help, that's how it works!"),
       (54.15, "Art time's done (art time's done!), crayons back in the box,"), (56.75, 'Markers in the cup with the caps on top.'),
       (59.35, 'Mad is okay (mad is okay!), but throwing is not,'), (61.95, 'Put it down, breathe, ask for help, put it back in its spot!'),
       (64.55, 'When I feel mad, I can choose! (I can choose!)'), (69.4, 'Breathe in slow, blow it out, whoo!'),
       (74.3, 'Calm corner, break card, use my words,'), (76.85, "Ask a grown-up, I get help, that's how it works!"),
       (79.5, 'Feeling mad? (Put it down, breathe!)'), (82.1, 'Hand on your heart, say it with me:'),
       (85.6, 'I keep our things safe.')]

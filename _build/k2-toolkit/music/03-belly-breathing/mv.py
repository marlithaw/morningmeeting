# Music video timing for Topic 3 · Belly Breathing ("Balloon Belly").
# Build:  python3 music/build_mv.py 03-belly-breathing --clips DIR
# The uploaded Suno file is a cover-art video (no lyrics on screen), so caption times come from
# phrase starts found in the vocals (harmonic-band energy after silence) checked against Topic 1's
# known timing for the same intro and chorus. Watch once and nudge any line that is early or late.
# Shared-part clips are reused from Gentle Hands (gh_*).

SONG = 'song-source.mp4'
CLIPS = 'clips'
TITLE = 'BELLY BREATHING'
SUBTITLE = 'Morning Meeting · K–2'
TITLE_LAYOUT = 'frame'            # title above a framed video, so it never covers a face
TITLE_UNTIL = 7.3
OPENING_CROP = (258, 8, 764, 430)  # zoom the intro clip to Lee and Tee, head to waist
BPM = 92.285                      # librosa: 92.3 tempo, first beat 0.195
BEAT0 = 0.195
SNAP_UNTIL = 85
CLIP_LEN = 8.05
END = 86.5

# (end_time, clip, src_in)
SEG = [(7.4, 'gh_wave', 0.0),
       # hook
       (12.2, 'bbv_hero', 0.3), (14.2, 'bbv_steps', 0.5), (16.8, 'bbv_hero', 4.5),
       # verse 1: clean-up time, Tee breathes, calm
       (24.6, 'bbv_busy', 0.0), (29.8, 'bbv_belly', 0.3), (33.4, 'bbv_calm', 0.5),
       # chorus (shared)
       (36.5, 'gh_promise', 0.0), (41.7, 'gh_breathe', 1.0), (43.7, 'gh_corner', 2.0), (45.2, 'gh_break', 2.0),
       (47.9, 'gh_grownup', 1.0),
       # verse 2: one, two, three, ask for more time
       (51.7, 'bbv_count', 0.3), (54.8, 'bbv_steps', 3.0), (57.2, 'bbv_belly', 4.0), (59.8, 'bbv_calm', 4.5),
       # chorus (shared)
       (63.7, 'gh_promise', 0.5), (67.6, 'gh_breathe', 2.6), (69.6, 'gh_corner', 5.3), (71.1, 'gh_break', 5.0),
       (75.0, 'gh_grownup', 2.6),
       # outro
       (77.6, 'bbv_hero', 2.0), (79.9, 'gh_promise', 0.3), (86.5, 'bbv_count', 1.0)]

# (start_time, caption). Text in (parentheses) is the echo, drawn yellow.
LYR = [(0.5, 'Matchbook, are you ready? (Ready!)'), (2.0, 'Hands up high, hands down low,'), (5.0, "Let's learn it, let's go!"),
       (7.75, 'Balloon belly (balloon belly!), hand right there,'), (9.75, 'Breathe in slow (breathe in slow!), fill it up with air.'),
       (12.4, 'Breathe out slow and let it go,'), (14.5, "My busy body's calm, now I know!"),
       (16.9, "It was clean-up time, but my drawing wasn't done,"), (20.35, 'My heart went fast like I was trying to run.'),
       (22.6, 'My shoulders went up and my breath got quick,'), (25.2, 'I needed a tool, so I knew the trick:'),
       (27.75, 'Hand on my belly, I breathed in deep,'), (29.8, 'Then out nice and slow, my calm I keep.'),
       (33.4, 'When I feel mad, I can choose! (I can choose!)'), (36.55, 'Breathe in slow, blow it out, whoo!'),
       (41.7, 'Calm corner, break card, use my words,'), (45.2, "Ask a grown-up, I get help, that's how it works!"),
       (47.9, 'One (in!), my belly gets wide,'), (51.7, 'Two (out!), I feel calm inside.'),
       (54.8, 'Three, my shoulders drop down low,'), (57.25, 'Then I ask for more time, nice and slow.'),
       (59.8, 'When I feel mad, I can choose! (I can choose!)'), (63.75, 'Breathe in slow, blow it out, whoo!'),
       (67.6, 'Calm corner, break card, use my words,'), (71.1, "Ask a grown-up, I get help, that's how it works!"),
       (75.0, 'Busy body! (I belly breathe!)'), (77.6, 'Hand on your heart, say it with me:'),
       (79.9, 'I can breathe slow to calm my body.')]

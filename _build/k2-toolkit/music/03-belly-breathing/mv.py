# Music video timing for Topic 3 · Belly Breathing ("Balloon Belly").
# Build:  python3 music/build_mv.py 03-belly-breathing --clips DIR
# Timing: the Suno file has no lyrics on screen. Verse lines come from a Canva auto-caption pass of the
# same audio (Oct 10); the hook, chorus, and outro starts come from the song's section changes (beat-synced
# novelty) and the exact chorus repeat (chorus 2 = chorus 1 + 25.9 s), lined up to 2.6 s bars.
# Shared-part clips are reused from Gentle Hands (gh_*).

SONG = 'song-source.mp4'
CLIPS = 'clips'
TITLE = 'BELLY BREATHING'
SUBTITLE = 'Morning Meeting · K–2'
TITLE_LAYOUT = 'frame'            # title above a framed video, so it never covers a face
TITLE_UNTIL = 8.5
OPENING_CROP = (258, 8, 764, 430)  # zoom the intro clip to Lee and Tee, head to waist
BPM = 92.285                      # librosa: 92.3 tempo, first beat 0.195
BEAT0 = 0.195
SNAP_UNTIL = 85
CLIP_LEN = 8.05
END = 86.5

# (end_time, clip, src_in[, speed])
SEG = [(8.6, 'gh_wave', 0.0, 0.92),
       # hook
       (11.2, 'bbv_hero', 0.3), (16.4, 'bbv_steps', 0.5), (19.3, 'bbv_hero', 4.0),
       # verse 1: clean-up time, Tee breathes, calm
       (25.0, 'bbv_busy', 0.0), (30.1, 'bbv_belly', 0.3), (35.5, 'bbv_calm', 0.5),
       # chorus (shared)
       (38.9, 'gh_promise', 0.0), (43.1, 'gh_breathe', 1.0), (45.2, 'gh_corner', 2.0), (47.3, 'gh_break', 2.0),
       (50.8, 'gh_grownup', 1.0),
       # verse 2: one, two, three, ask for more time
       (55.6, 'bbv_count', 0.3), (58.2, 'bbv_belly', 4.0), (61.4, 'bbv_calm', 4.5),
       # chorus (shared)
       (64.8, 'gh_promise', 0.5), (69.0, 'gh_breathe', 2.6), (71.1, 'gh_corner', 5.3), (73.2, 'gh_break', 5.0),
       (77.5, 'gh_grownup', 2.6),
       # outro
       (80.1, 'bbv_hero', 2.0), (82.6, 'gh_promise', 0.3), (86.5, 'bbv_count', 1.0)]

# (start_time, caption). Text in (parentheses) is the echo, drawn yellow.
LYR = [(0.6, 'Matchbook, are you ready? (Ready!)'), (3.45, 'Hands up high, hands down low,'), (6.05, "Let's learn it, let's go!"),
       (8.6, 'Balloon belly (balloon belly!), hand right there,'), (11.2, 'Breathe in slow (breathe in slow!), fill it up with air.'),
       (13.8, 'Breathe out slow and let it go,'), (16.4, "My busy body's calm, now I know!"),
       (19.3, "It was clean-up time, but my drawing wasn't done,"), (22.6, 'My heart went fast like I was trying to run.'),
       (25.0, 'My shoulders went up and my breath got quick,'), (27.6, 'I needed a tool, so I knew the trick:'),
       (30.1, 'Hand on my belly, I breathed in deep,'), (32.9, 'Then out nice and slow, my calm I keep.'),
       (35.5, 'When I feel mad, I can choose! (I can choose!)'), (38.9, 'Breathe in slow, blow it out, whoo!'),
       (43.1, 'Calm corner, break card, use my words,'), (47.3, "Ask a grown-up, I get help, that's how it works!"),
       (50.8, 'One (in!), my belly gets wide,'), (53.3, 'Two (out!), I feel calm inside.'),
       (55.6, 'Three, my shoulders drop down low,'), (58.2, 'Then I ask for more time, nice and slow.'),
       (61.4, 'When I feel mad, I can choose! (I can choose!)'), (64.8, 'Breathe in slow, blow it out, whoo!'),
       (69.0, 'Calm corner, break card, use my words,'), (73.2, "Ask a grown-up, I get help, that's how it works!"),
       (77.5, 'Busy body! (I belly breathe!)'), (80.1, 'Hand on your heart, say it with me:'),
       (82.6, 'I can breathe slow to calm my body.')]

# Music video timing for Topic 2 · Using the Calm Corner ("Calm Down", Suno, 86.4 s, 92 BPM).
# Build:  python3 music/build_mv.py 02-calm-corner --clips /path/to/clips
# Clips (Flow, 8 s each) are not in the repo. cc_* are this topic's clips; gh_* are reused Gentle Hands clips
# (gh_wave = 01, gh_breathe = 04, gh_corner = 05, gh_break = 06, gh_grownup = 07, gh_promise = 10).
# Lyric start times come from the highlighted line in Suno's lyric video. The shared intro and the
# Calm Choices chorus reuse the same Gentle Hands clips so every topic's chorus looks the same.

SONG = 'song-source.mp4'
CLIPS = 'clips'
TITLE = 'CALM CORNER'
SUBTITLE = 'Morning Meeting · K–2'
TITLE_UNTIL = 7.3                # opening card shows through the intro
TITLE_LAYOUT = 'frame'            # title above a framed video, so it never covers a face
OPENING_CROP = (258, 8, 764, 430)  # zoom the intro clip to Lee and Tee, head to waist
BPM = 92.285
BEAT0 = 0.263
SNAP_UNTIL = 83
CLIP_LEN = 8.05
END = 85.8

SEG = [
    # intro
    (7.4, 'gh_wave', 0.0),
    # hook: calm corner is where I rest / I get calm / notice, walk, get calm, come back / right on track
    (11.75, 'cc_breathe', 0.5), (14.5, 'cc_walk', 2.0), (16.75, 'cc_rug', 4.5),
    # verse 1
    (21.75, 'cc_tower', 0.5), (27.0, 'cc_notice', 0.5), (33.5, 'cc_walk', 0.3),
    # chorus 1 (same shots as Gentle Hands)
    (36.75, 'gh_promise', 0.0), (41.25, 'gh_breathe', 1.0), (43.25, 'gh_corner', 2.0), (45.5, 'gh_break', 2.0),
    (47.0, 'gh_grownup', 1.0),
    # verse 2
    (49.0, 'cc_hug', 1.5), (50.5, 'cc_book', 2.5), (54.0, 'cc_feelings', 1.0), (56.25, 'cc_breathe', 3.5),
    (59.5, 'cc_rug', 0.5),
    # chorus 2
    (62.5, 'gh_corner', 0.5), (67.25, 'gh_breathe', 2.6), (69.25, 'gh_corner', 5.3), (71.5, 'gh_break', 5.0),
    (74.25, 'gh_grownup', 2.6),
    # outro: big feelings / hand on heart / I get calm, then I come back to learn
    (77.5, 'cc_hug', 4.2), (80.0, 'gh_promise', 0.0), (85.8, 'cc_rug', 2.0),
]

LYR = [(0.5, 'Matchbook, are you ready? (Ready!)'), (2.0, 'Hands up high, hands down low,'), (5.25, "Let's learn it, let's go!"),
       (7.75, 'Calm corner (calm corner!) is where I rest,'), (9.5, 'I get calm (I get calm!), then I\'m at my best.'),
       (11.75, 'Notice, walk, get calm, come back,'), (14.5, 'Calm corner keeps me right on track!'),
       (17.0, 'My tower fell down and my face got hot,'), (20.0, 'My hands got tight, my tummy in a knot.'),
       (21.75, 'I noticed my feeling, I gave it a name,'), (24.25, "Big feelings are okay, nobody's to blame."),
       (27.0, "I walk, don't run, to the cozy spot,"), (29.5, "One friend at a time, that's the deal we got."),
       (33.5, 'When I feel mad, I can choose! (I can choose!)'), (36.75, 'Breathe in slow, blow it out, whoo!'),
       (41.25, 'Calm corner, break card, use my words,'), (45.5, "Ask a grown-up, I get help, that's how it works!"),
       (47.0, 'I hug a soft friend, I read a book,'), (49.5, 'I find my feeling and I take a look.'),
       (54.0, 'My body feels calm, my breathing is slow,'), (56.25, "Back to the rug, now I'm ready to go!"),
       (59.5, 'When I feel mad, I can choose! (I can choose!)'), (62.5, 'Breathe in slow, blow it out, whoo!'),
       (67.25, 'Calm corner, break card, use my words,'), (71.5, "Ask a grown-up, I get help, that's how it works!"),
       (74.25, 'Big feelings! (I use the calm corner!)'), (77.5, 'Hand on your heart, say it with me:'),
       (79.0, 'I get calm. Then I come back to learn.')]

# Music video timing for Topic 6 · Fixing It ("Fix It").
# Build:  python3 music/build_mv.py 06-fixing-it --clips DIR
# This Suno export has no on-screen lyrics. The song shares Topic 4's tempo (92.285 BPM, first beat 0.16 s), section
# layout, and line counts, so times come from a chroma + MFCC alignment against the Topic 4 song (timed by OCR),
# refined on the vocal-band onset envelope. Chorus 2 checks out independently by chroma self-similarity (58.8 s).
# Every cut matches its lyric: the bump on "Bump!", Lee kneeling on "I stopped and I looked", the sorry on the sorry
# line, rebuilding on "How can I help?", giving space on verse 2, and the high five that ends in a wave goodbye.
# Shared-part clips are reused from Gentle Hands (gh_*).

SONG = 'song-source.mp4'
CLIPS = 'clips'
TITLE = 'FIXING IT'
SUBTITLE = 'Morning Meeting · K–2'
TITLE_LAYOUT = 'frame'
TITLE_UNTIL = 7.4
OPENING_CROP = (258, 8, 764, 430)
BPM = 92.285
BEAT0 = 0.16
SNAP_UNTIL = 82
CLIP_LEN = 8.05
END = 83.5

# (end_time, clip, src_in[, speed])
SEG = [(7.5, 'gh_wave', 0.0),
       # hook: oops (blocks tumble), sorry (hand on heart), how can I help (building together), we fix it (high five)
       (9.8, 'ftv_bump', 0.3), (11.2, 'ftv_sorry', 0.3), (13.9, 'ftv_help', 0.3), (16.2, 'ftv_fixed', 0.2),
       # verse 1: Lee walks with the bin; "Bump!" lands on the tumble; Lee sets the bin down and looks; kneels by her side;
       # the sorry; "How can I help? We built it back"
       (19.9, 'ftv_walk', 3.6), (21.4, 'ftv_bump', 0.2), (24.1, 'ftv_bump', 3.0), (27.3, 'ftv_stop', 0.3),
       (29.5, 'ftv_sorry', 1.0), (33.0, 'ftv_help', 3.0),
       # chorus (shared)
       (36.1, 'gh_promise', 0.0), (40.8, 'gh_breathe', 1.0), (42.9, 'gh_corner', 2.0), (45.0, 'gh_break', 2.0),
       (47.0, 'gh_grownup', 1.0),
       # verse 2: friend needs space (Lee waits nearby; ftv_space is used only after 1.9 s, past a framing glitch),
       # then Kiara smiles (slightly slowed so the clean part covers both lines); a spill: Tee picks up and hands back crayons
       (50.4, 'ftv_space', 1.9), (53.3, 'ftv_space', 5.15, 0.85), (55.0, 'ftv_crayons', 0.0), (58.8, 'ftv_crayons', 2.0),
       # chorus (shared)
       (61.8, 'gh_promise', 0.5), (66.6, 'gh_breathe', 2.6), (68.7, 'gh_corner', 5.3), (70.7, 'gh_break', 5.0),
       (74.5, 'gh_grownup', 2.6),
       # outro: Lee and Tee high five, hand on heart, then Lee and Kiara wave goodbye beside the rebuilt tower
       (76.7, 'ftv_hero', 4.0), (78.6, 'gh_promise', 0.3), (83.5, 'ftv_fixed', 3.0)]

LYR = [(0.4, 'Matchbook, are you ready? (Ready!)'), (2.0, 'Hands up high, hands down low,'), (5.2, "Let's learn it, let's go!"),
       (7.5, 'Oops (oops!), I stop and see,'), (9.8, 'Sorry (sorry!), it was me.'),
       (11.2, '"How can I help?" is what I say,'), (13.9, "We fix it up, it's A-okay!"),
       (16.2, "Center time, I'm walking, carrying the bin,"), (19.9, "Bump! Kiara's tower falls, my tummy's in a spin."),
       (21.4, "She looked so sad, I didn't run or hide,"), (24.1, 'I stopped and I looked and I knelt by her side.'),
       (27.3, '"I\'m sorry I knocked your tower down," I said,'), (29.5, '"How can I help?" We built it back instead!'),
       (33.0, 'When I feel mad, I can choose! (I can choose!)'), (36.1, 'Breathe in slow, blow it out, whoo!'),
       (40.8, 'Calm corner, break card, use my words,'), (45.0, "Ask a grown-up, I get help, that's how it works!"),
       (47.0, "Friend needs space? (Needs space!) That's okay,"), (50.4, 'I give some room (some room!), try again later today.'),
       (53.3, 'A spill, a bump, a mix-up too,'), (55.0, "Stop, say sorry, ask, help fix it. That's what I do!"),
       (58.8, 'When I feel mad, I can choose! (I can choose!)'), (61.8, 'Breathe in slow, blow it out, whoo!'),
       (66.6, 'Calm corner, break card, use my words,'), (70.7, "Ask a grown-up, I get help, that's how it works!"),
       (74.5, 'Made a mistake? (Stop and fix it!)'), (76.7, 'Hand on your heart, say it with me:'),
       (78.6, 'I can help make it right.')]

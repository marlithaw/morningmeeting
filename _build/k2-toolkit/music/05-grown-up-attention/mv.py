# Music video timing for Topic 5 · Getting a Grown-Up's Attention ("Get Adult Attention").
# Build:  python3 music/build_mv.py 05-grown-up-attention --clips DIR
# This Suno export has no on-screen lyrics, so OCR timing was not possible. The song shares Topic 4's tempo
# (92.285 BPM, first beat 0.16 s), section layout, and line counts. Times come from a chroma + MFCC alignment
# against the Topic 4 song (whose times came from OCR), refined line by line on the vocal-band onset envelope.
# The intro and both choruses (same lyrics as Topic 4) matched strongly; chorus 2 also checks out independently
# by chroma self-similarity (25.8 s after chorus 1). Verse lines are the least certain.
# Shared-part clips are reused from Gentle Hands (gh_*). gav_help: only its first 4 s (the teacher stands out of frame after).

SONG = 'song-source.mp4'
CLIPS = 'clips'
TITLE = 'GET A GROWN-UP'
SUBTITLE = 'Morning Meeting · K–2'
TITLE_LAYOUT = 'frame'            # title above a framed video, so it never covers a face
TITLE_UNTIL = 7.4
OPENING_CROP = (258, 8, 764, 430)  # zoom the intro clip to Lee and Tee, head to waist
BPM = 92.285
BEAT0 = 0.16
SNAP_UNTIL = 82
CLIP_LEN = 8.05
END = 83.9

# (end_time, clip, src_in[, speed])
SEG = [(7.5, 'gh_wave', 0.0),
       # hook: hands up, calm body, she comes, thank you
       (9.8, 'gav_hero', 0.3), (11.2, 'gav_hand', 0.3), (13.9, 'gav_comes', 0.5), (16.2, 'gav_thanks', 0.3),
       # verse 1: pencil broke, teacher busy, no shouting, hand up, she walks over, thank you
       (19.6, 'gav_need', 0.3), (21.2, 'gav_need', 4.0), (24.1, 'gav_s2', 0.3), (27.4, 'gav_hand', 2.2),
       (29.4, 'gav_comes', 3.5), (33.0, 'gav_help', 0.2),
       # chorus (shared)
       (36.2, 'gh_promise', 0.0), (40.9, 'gh_breathe', 1.0), (43.0, 'gh_corner', 2.0), (45.1, 'gh_break', 2.0),
       (47.1, 'gh_grownup', 1.0),
       # verse 2: hallway, stand close and wait, excuse me, hurt means right away
       (55.0, 'gav_hall', 0.1), (58.9, 'gh_grownup', 3.5),
       # chorus (shared)
       (62.0, 'gh_promise', 0.5), (66.7, 'gh_breathe', 2.6), (68.8, 'gh_corner', 5.3), (70.9, 'gh_break', 5.0),
       (74.7, 'gh_grownup', 2.6),
       # outro
       (76.8, 'gav_hero', 0.2), (78.7, 'gh_promise', 0.3), (83.9, 'gav_thanks', 2.5)]

# (start_time, caption). Text in (parentheses) is the echo, drawn yellow.
LYR = [(0.4, 'Matchbook, are you ready? (Ready!)'), (2.0, 'Hands up high, hands down low,'), (5.2, "Let's learn it, let's go!"),
       (7.5, 'Hand up (hand up!), stay in my seat,'), (9.8, 'Calm body (calm body!), quiet hands and feet.'),
       (11.2, 'My teacher sees me, she\'s on her way,'), (13.9, 'I tell what I need, then "Thank you!" I say.'),
       (16.2, 'It was writing time and my pencil broke in two,'), (19.6, 'My teacher had a group, so what did I do?'),
       (21.2, "I didn't shout out, didn't run to her side,"), (24.1, 'I raised my hand high and I waited with pride.'),
       (27.4, 'She nodded, "I see you," then walked to my seat,'), (29.4, 'I said, "My pencil broke," and she helped me. Sweet!'),
       (33.0, 'When I feel mad, I can choose! (I can choose!)'), (36.2, 'Breathe in slow, blow it out, whoo!'),
       (40.9, 'Calm corner, break card, use my words,'), (45.1, "Ask a grown-up, I get help, that's how it works!"),
       (47.1, "In the hall (in the hall!), she's talking, I see,"), (50.4, 'Stand close (stand close!) and wait patiently.'),
       (53.4, 'When she is done, "Excuse me," I say,'), (55.0, 'If someone gets hurt, I get help right away!'),
       (58.9, 'When I feel mad, I can choose! (I can choose!)'), (62.0, 'Breathe in slow, blow it out, whoo!'),
       (66.7, 'Calm corner, break card, use my words,'), (70.9, "Ask a grown-up, I get help, that's how it works!"),
       (74.7, 'Need help? (Hand up and wait!)'), (76.8, 'Hand on your heart, say it with me:'),
       (78.7, "I can get a grown-up's help the safe way.")]

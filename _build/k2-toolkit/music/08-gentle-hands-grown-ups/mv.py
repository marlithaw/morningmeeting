# Music video timing for Topic 8 · Gentle Hands with Grown-Ups ("Hands Down, Step Back").
# Build:  python3 music/build_mv.py 08-gentle-hands-grown-ups --clips DIR
# This Suno export has no on-screen lyrics, so OCR timing was not possible. The song shares Topic 4's tempo
# (92.285 BPM, first beat 0.19 s), section layout, and line counts. Times come from a chroma + MFCC alignment
# against the Topic 4 song (whose times came from OCR). Chorus 2 lands 25.8 s after chorus 1, matching Topics 5 and 6.
# Shared-part clips are reused from Gentle Hands (gh_*). Tee never grabs or pushes on screen: the hook and verse show
# only the safe steps (hands down, step back, breathe, use words).

SONG = 'song-source.mp4'
CLIPS = 'clips'
TITLE = 'GENTLE HANDS TOO'
SUBTITLE = 'Morning Meeting · K–2'
TITLE_LAYOUT = 'frame'            # title above a framed video, so it never covers a face
TITLE_UNTIL = 7.4
OPENING_CROP = (258, 8, 764, 430)  # zoom the intro clip to Lee and Tee, head to waist
BPM = 92.285
BEAT0 = 0.19
SNAP_UNTIL = 82
CLIP_LEN = 8.05
END = 84.7

# (end_time, clip, src_in[, speed])
SEG = [(7.5, 'gh_wave', 0.0),
       # hook: hands down and step back, breathe, "I feel mad," safe with my grown-ups
       (9.8, 'gmv_hands', 0.3), (11.2, 'gmv_breathe', 0.6), (13.95, 'gmv_words', 0.3), (16.25, 'gmv_hero', 0.3),
       # verse 1: block tower, "Clean-up time!", hands feel tight (one take of the teacher calling clean-up),
       # then hands down and step back, breathe, tell her
       (24.05, 'gmv_no', 0.1), (27.0, 'gmv_hands', 0.2), (29.4, 'gmv_breathe', 1.2), (33.1, 'gmv_words', 3.0),
       # chorus (shared)
       (36.15, 'gh_promise', 0.0), (40.9, 'gh_breathe', 1.0), (43.0, 'gh_corner', 2.0), (45.1, 'gh_break', 2.0),
       (47.05, 'gh_grownup', 1.0),
       # verse 2: lunch helpers, bus drivers, teachers, family; mad is okay; the four steps as a quick montage
       (48.7, 'gmv_lunch', 0.5), (50.3, 'gmv_bus', 0.5), (51.9, 'gmv_fist', 0.3), (53.4, 'gmv_hug', 0.3),
       (55.3, 'gmv_calm', 0.2), (56.5, 'gmv_hands', 0.4), (57.7, 'gmv_breathe', 2.5), (58.9, 'gmv_words', 1.5),
       # chorus (shared)
       (61.95, 'gh_promise', 0.5), (66.7, 'gh_breathe', 2.6), (68.8, 'gh_corner', 5.3), (70.85, 'gh_break', 5.0),
       (74.65, 'gh_grownup', 2.6),
       # outro: calm breath with the teacher, hand on heart, ends on Lee, the teacher, and Tee waving goodbye
       (76.85, 'gmv_breathe', 5.0), (78.7, 'gh_promise', 0.3), (84.7, 'gmv_hero', 2.0)]

# (start_time, caption). Text in (parentheses) is the echo, drawn yellow.
LYR = [(0.4, 'Matchbook, are you ready? (Ready!)'), (2.0, 'Hands up high, hands down low,'), (5.2, "Let's learn it, let's go!"),
       (7.5, 'Hands down (hands down!), step back slow,'), (9.8, 'Breathe in (breathe in!), and let it go.'),
       (11.2, '"I feel mad," I can say it right,'), (13.95, 'Safe with my grown-ups, day and night!'),
       (16.25, 'Block time, building, my tower was tall,'), (20.1, '"Clean-up time!" my teacher called.'),
       (21.5, 'My hands felt tight, I wanted to grab,'), (24.05, 'But I pressed them down and I stepped back.'),
       (27.0, 'I breathed in slow, then I told her true:'), (29.4, '"I feel mad, I\'m not done!" She said, "Thank you!"'),
       (33.1, 'When I feel mad, I can choose! (I can choose!)'), (36.15, 'Breathe in slow, blow it out, whoo!'),
       (40.9, 'Calm corner, break card, use my words,'), (45.1, "Ask a grown-up, I get help, that's how it works!"),
       (47.05, 'Lunch helpers (lunch helpers!), bus drivers too,'), (50.3, 'Teachers and family take care of you.'),
       (53.4, 'Mad is okay (mad is okay!), but hurting is not,'), (55.3, "Hands down, step back, breathe, use the words I've got!"),
       (58.9, 'When I feel mad, I can choose! (I can choose!)'), (61.95, 'Breathe in slow, blow it out, whoo!'),
       (66.7, 'Calm corner, break card, use my words,'), (70.85, "Ask a grown-up, I get help, that's how it works!"),
       (74.65, 'Feeling mad? (Hands down, breathe!)'), (76.85, 'Hand on your heart, say it with me:'),
       (78.7, 'I keep my grown-ups safe too.')]

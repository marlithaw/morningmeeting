# Music video timing for Topic 7 · Gentle Hands with Friends (the cut published 2026-10-07).
# Build:  python3 music/build_mv.py 07-gentle-hands [--clips DIR]
# Times are seconds into the song. Clip mp4s (Flow, 8 s each) are not in the repo: put them in
# music/07-gentle-hands/clips/01.mp4 ... 10.mp4 or pass --clips.

SONG = 'song-source.mp4'          # the Suno song (audio used for the video), in this folder
CLIPS = 'clips'                   # folder of NN.mp4 clips, relative to this folder (override with --clips)
TITLE = 'GENTLE HANDS'            # title card over the opening
SUBTITLE = 'Morning Meeting · K–2'
TITLE_UNTIL = 5.95                # opening card shows through the intro
TITLE_LAYOUT = 'frame'            # title above a framed video, so it never covers a face
OPENING_CROP = (258, 8, 764, 430)  # zoom the intro clip to Lee and Tee, head to waist
BPM = 92.285                      # cuts snap to the beat grid: BEAT0 + k * 60/BPM
BEAT0 = 0.19
SNAP_UNTIL = 83                   # cuts at or after this time are not snapped (the ending)
CLIP_LEN = 8.05                   # longest usable source time per clip (in + duration must fit)
END = 83.6                        # video length; audio fades over the last 1.5 s, picture over 1.2 s

# (end_time, clip, src_in): each segment runs from the previous end to end_time, cut from clip at src_in
SEG = [(6.04, '01', 0.5), (9.6, '08', 0.0), (12.6, '03', 1.0), (16.0, '08', 4.0), (17.6, '09', 0.0),
       (21.5, '02', 0.5), (24.1, '03', 3.0), (27.5, '02', 4.5), (30.2, '08', 2.0), (33.0, '09', 2.0),
       (37.6, '10', 0.0), (43.4, '04', 1.0), (44.9, '05', 2.0), (46.4, '06', 2.0), (49.6, '07', 1.0),
       (54.2, '02', 2.6), (57.0, '09', 4.0), (59.6, '07', 4.5),
       (64.4, '05', 0.5), (68.0, '04', 3.0), (69.5, '05', 5.5), (71.0, '06', 5.0), (75.6, '07', 3.0),
       (78.2, '08', 5.0), (83.6, '10', 2.4)]

# (start_time, caption): each caption shows until the next one starts. Text in (parentheses) is the echo, drawn yellow.
LYR = [(1.0, 'Matchbook, are you ready? (Ready!)'), (2.5, 'Hands up high, hands down low,'), (4.4, "Let's learn it, let's go!"),
       (6.0, 'Gentle hands (gentle hands!) keep my friends safe,'), (9.5, 'Hitting hurts (hitting hurts!), so I give them space.'),
       (12.5, 'High five, fist bump, wave hello,'), (15.6, 'Gentle hands everywhere I go!'),
       (17.6, 'When my face gets hot and my fists get tight,'), (19.9, 'I feel it in my chest, but I can make it right.'),
       (21.6, 'Hitting hurts, hitting hurts, my friend feels sad,'), (24.0, "So I don't hit, not even when I'm mad."),
       (27.3, 'Gentle hands: high five, fist bump, wave,'), (29.9, "That's how we play, that's how we stay safe."),
       (33.0, 'When I feel mad, I can choose! (I can choose!)'), (37.6, 'Breathe in slow, blow it out, whoo!'),
       (43.3, 'Calm corner, break card, use my words,'), (46.3, "Ask a grown-up, I get help, that's how it works!"),
       (49.6, 'Somebody took my truck and I wanted to shout,'), (51.4, 'I stopped, took a breath, and I let it out.'),
       (52.8, '"Can I have a turn?" Yeah, I used my words,'), (56.9, "Calm voice, calm hands, now I'm being heard."),
       (59.4, 'When I feel mad, I can choose! (I can choose!)'), (64.3, 'Breathe in slow, blow it out, whoo!'),
       (67.9, 'Calm corner, break card, use my words,'), (70.9, "Ask a grown-up, I get help, that's how it works!"),
       (75.4, 'Hitting hurts! (We use gentle hands!)'), (78.0, 'Hand on your heart, say it with me:'),
       (80.0, 'I use gentle hands. I keep my friends safe.')]

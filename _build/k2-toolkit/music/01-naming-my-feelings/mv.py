# Music video timing for Topic 1 · Naming My Feelings ("Name It (My Feelings)").
# Build:  python3 music/build_mv.py 01-naming-my-feelings --clips DIR
# Times are seconds into the song. Clip mp4s (Flow, 8 s each) are not in the repo; pass --clips.
# Shared-part clips are reused from Gentle Hands (gh_*) and Calm Corner (cc_tower).

SONG = 'song-source.mp4'
CLIPS = 'clips'
TITLE = 'MY FEELINGS'
SUBTITLE = 'Morning Meeting · K–2'
TITLE_LAYOUT = 'frame'            # title above a framed video, so it never covers a face
TITLE_UNTIL = 7.3                 # opening card shows through the intro
BPM = 92.285                      # librosa: 92.2 fit, first beat 0.19
BEAT0 = 0.19
SNAP_UNTIL = 83
CLIP_LEN = 8.05
END = 83.8

# (end_time, clip, src_in)
SEG = [(7.4, 'gh_wave', 0.0),
       # hook
       (12.2, 'ff_cards', 0.3), (14.2, 'ff_say', 0.3), (16.6, 'ff_cards', 5.0),
       # verse 1: Lee's turn to read
       (21.3, 'ff_turn', 0.3), (26.8, 'ff_tummy', 0.3), (31.0, 'ff_tell', 0.5), (33.4, 'ff_proud', 0.3),
       # chorus (shared)
       (36.5, 'gh_promise', 0.0), (41.25, 'gh_breathe', 1.0), (43.25, 'gh_corner', 2.0), (45.5, 'gh_break', 2.0),
       (47.5, 'gh_grownup', 1.0),
       # verse 2: happy, sad, mad, name it
       (51.2, 'gh_high5', 0.5), (54.0, 'cc_tower', 0.5), (56.5, 'ff_mad', 0.5), (59.7, 'ff_say', 3.0),
       # chorus (shared)
       (63.7, 'gh_promise', 0.5), (67.25, 'gh_breathe', 2.6), (69.25, 'gh_corner', 5.3), (71.5, 'gh_break', 5.0),
       (75.5, 'gh_grownup', 2.6),
       # outro
       (77.5, 'ff_proud', 4.0), (79.2, 'gh_promise', 0.3), (83.8, 'ff_bye', 1.0)]

# (start_time, caption): timed from the Suno lyric video. Text in (parentheses) is the echo, drawn yellow.
LYR = [(0.5, 'Matchbook, are you ready? (Ready!)'), (2.0, 'Hands up high, hands down low,'), (5.0, "Let's learn it, let's go!"),
       (7.75, 'Name it (name it!), say how I feel,'), (9.5, "All my feelings (all my feelings!) are okay, they're real."),
       (12.25, 'Happy, sad, mad, worried too,'), (14.25, 'I say "I feel," and I name it true!'),
       (16.75, 'It was my turn to read and my tummy felt funny,'), (19.5, "My hands got shaky, wasn't feeling so sunny."),
       (21.5, 'I stopped and I noticed what my body said,'), (24.0, 'I found the word that was right in my head.'),
       (27.0, 'I said, "I feel worried," out loud and clear,'), (28.75, 'My teacher said, "Thank you, I\'m right here."'),
       (33.5, 'When I feel mad, I can choose! (I can choose!)'), (36.5, 'Breathe in slow, blow it out, whoo!'),
       (41.25, 'Calm corner, break card, use my words,'), (45.5, "Ask a grown-up, I get help, that's how it works!"),
       (47.5, "When I'm happy, I smile and I feel so bright,"), (51.25, "When I'm sad, my eyes get wet, and that's alright."),
       (54.0, "When I'm mad, my face gets hot and my hands get tight,"), (56.5, 'I can name it, I can say it, then I make it right!'),
       (59.75, 'When I feel mad, I can choose! (I can choose!)'), (63.75, 'Breathe in slow, blow it out, whoo!'),
       (67.25, 'Calm corner, break card, use my words,'), (71.5, "Ask a grown-up, I get help, that's how it works!"),
       (75.5, 'Big feelings! (I can name my feeling!)'), (77.5, 'Hand on your heart, say it with me:'),
       (79.25, 'I can name my feeling. I can say, "I feel..."')]

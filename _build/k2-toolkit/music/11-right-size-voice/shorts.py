# Vertical shorts for Topic 11 · Right-Size Voice. Build: python3 music/build_short.py 11-right-size-voice all --clips DIR
# All cuts sit on the song's bar grid (7.34 + 2.60064 k), so the song jumps loop cleanly. No Matchbook logo or intro.
B = 60 / 92.285            # one beat
BAR = 4 * B
SKY, YEL, GRN, RED = (47, 128, 237), (249, 220, 124), (31, 138, 76), (226, 28, 36)

HOOK = [(0.0, 'Look around (look around!), where am I?'), (2.61, 'Who needs to hear me? Pick my number right!'),
        (5.21, 'Turn my dial (turn my dial!), up or down,'), (7.76, 'Right-size voice, all around!')]
P1 = 17.743 - 7.34          # first pass (4 bars)
P2 = 17.80 - 7.34           # second pass rings out a little

# 1. Sing the Hook: listen once, then sing the yellow echo parts.
hook = dict(
    title='SING THE HOOK!', sub='Right-Size Voice with Lee & Tee',
    audio=[('song', 7.34, 17.743), ('song', 7.34, 17.80)],
    clips=[(2.61, 'rvv_look', 0.3), (2.60, 'rvv_look', 3.0), (2.55, 'rvv_dialcu', 0.5), (P1 - 7.76, 'rvv_dialcu', 4.0),
           (2.61, 'rvv_look', 0.3), (2.60, 'rvv_dial', 0.5), (2.55, 'rvv_dialcu', 2.0), (P2 - 7.76, 'rvv_calm', 0.5)],
    captions=[(t, (HOOK[i + 1][0] if i < 3 else P1), x) for i, (t, x) in enumerate(HOOK)]
            + [(P1 + t, P1 + (HOOK[i + 1][0] if i < 3 else P2), x) for i, (t, x) in enumerate(HOOK)],
    badges=[(0, P1, 'LISTEN FIRST', SKY), (P1, P1 + P2, 'YOUR TURN! SING THE YELLOW', YEL)],
)

# 2. What Number? Watch the scene, count down, see the answer. Lyric-free drum bed, then the hook to finish.
ROUNDS = [('rvv_lunch', 0.15, 'Lunch with my friends.', 2, 'Table talk', 'Two! Table talk.'),
          ('rvv_hall', 0.15, 'Walking down the hallway.', 0, 'Lips closed', 'Zero! Lips closed.'),
          ('rvv_gym', 0.15, 'Team game in gym class.', 3, 'Whole room', 'Three! Loud and clear for my team.')]
Q = dict(title='WHAT NUMBER?', sub='Guess the voice level!', audio=[('beat', 4 * len(ROUNDS))],
         clips=[], captions=[], meter=[], counts=[], reveals=[], sfx=[], badges=[])
for r, (clip, src, scene, lv, name, answer) in enumerate(ROUNDS):
    R = r * 4 * BAR
    Q['clips'] += [(round(12 * B, 4), clip, src), (round(4 * B, 4), clip, 0.0)]
    Q['captions'] += [(R, R + 6 * B, scene), (R + 6 * B, R + 12 * B, 'What voice level?'), (R + 12 * B, R + 16 * B, answer)]
    Q['meter'] += [(R, R + 12 * B, None), (R + 12 * B, R + 16 * B, lv)]
    Q['counts'] += [(R + (6 + 2 * k) * B, R + (8 + 2 * k) * B, 3 - k) for k in range(3)]
    Q['sfx'] += [('tick', R + (6 + 2 * k) * B) for k in range(3)] + [('chime', R + 12 * B)]
    Q['reveals'] += [(R + 12 * B, R + 16 * B, lv, name)]
E = len(ROUNDS) * 4 * BAR    # finish on the hook: "Turn my dial, up or down, right-size voice, all around!"
Q['audio'] += [('song', 12.541, 17.80)]
Q['clips'] += [(2.56, 'rvv_dialcu', 0.5), (round(17.80 - 12.541 - 2.56, 4), 'rvv_calm', 0.5)]
Q['captions'] += [(E, E + 2.56, 'Turn my dial (turn my dial!), up or down,'), (E + 2.56, E + 5.259, 'Right-size voice, all around!')]
Q['badges'] += [(E, E + 5.259, 'SING ALONG!', YEL)]
quiz = Q

# 3. Back to Two: the lunch verse with a live voice meter, then the hook.
L0 = 28.0                    # just before the bar, to keep the "Lunchtime!" pickup
L1 = 38.45                   # just before the chorus pickup
H0 = 12.541 - (38.548 - L1)  # same distance before a bar, so the jump stays on the beat
S1 = L1 - L0
lunch = dict(
    title='BACK TO TWO!', sub='A Lee & Tee lunch story',
    audio=[('song', L0, L1), ('song', H0, 17.80)],
    clips=[(2.7, 'rvv_lunch', 0.5), (2.6, 'rvv_loud', 0.3), (2.6, 'rvv_dial', 0.5), (round(S1 - 7.9, 4), 'rvv_calm', 0.5),
           (round(15.1 - H0, 4), 'rvv_dialcu', 0.5), (round(17.80 - 15.1, 4), 'swv_hero', 2.0)],
    captions=[(0.0, 2.7, 'Lunchtime! Two at the table, laughing with my crew,'),
              (2.7, 5.3, 'But the voices got louder, three, then four, whoo!'),
              (5.3, 7.9, 'I looked around, turned my dial: "Let\'s take it back to two!"'),
              (7.9, S1, 'The whole table turned it down, and now I can hear you!'),
              (S1, S1 + 15.1 - H0, 'Turn my dial (turn my dial!), up or down,'),
              (S1 + 15.1 - H0, S1 + 17.80 - H0, 'Right-size voice, all around!')],
    meter=[(0.0, 2.7 + 2 * B, 2), (2.7 + 2 * B, 2.7 + 3 * B, 3), (2.7 + 3 * B, 5.3 + 2 * B, 4),
           (5.3 + 2 * B, 5.3 + 2.6 * B, 3), (5.3 + 2.6 * B, S1 + 17.80 - H0, 2)],
)

SHORTS = dict(hook=hook, quiz=quiz, lunch=lunch)

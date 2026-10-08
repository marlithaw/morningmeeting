"""Content shared by every topic, plus the defaults a topic file can leave out.

Topic files import from here, e.g. `from shared import COPING, BREATHING`.
`resolve(TOPIC)` fills every default and derived value; the builders only read resolved topics.
"""
from common import deep_merge, lang3

# The five calm choices used across the toolkit: (image key, EN, ES, KR)
COPING = [('c_corner', 'Go to the calm corner', 'Ir al rincón de calma', 'Ale nan kwen kalm nan'),
          ('c_breathe', 'Take deep breaths', 'Respirar profundo', 'Respire fon'),
          ('c_break', 'Ask for a break', 'Pedir un descanso', 'Mande yon ti repo'),
          ('c_words', 'Use my words', 'Usar mis palabras', 'Sèvi ak pawòl mwen'),
          ('c_grownup', 'Ask a grown-up', 'Pedir ayuda a un adulto', 'Mande yon granmoun èd')]

# Slide 2 breathing cards: (icon, label, text). The same two gestures open every K-2 lesson.
BREATHING = [('🌸', 'Smell the flower', 'Slow breath in.'),
             ('🕯️', 'Blow the candle', 'Long breath out.')]

# Slide 7 default steps: (icon, label)
LEAVE_STEPS = [('🧍', 'Stand up'), ('🤲', 'Gentle hands'), ('👣', 'Walk'), ('⭐', 'Ready to learn')]

LANGS = ('en', 'es', 'kr')

DEFAULTS = dict(
    deck=dict(
        s1=dict(img='welcome', pos='center 20%'),
        s2=dict(eyebrow='First, We Get Calm', title='GET CALM FIRST', color='var(--green)',
                img='calm', pos='center 30%', cards=BREATHING, pill='3 times together'),
        s3=dict(eyebrow='Watch the Story', title='WHAT HAPPENED?', color='var(--red)', say_label='We say:'),
        s4=dict(eyebrow='Turn and Talk', color='var(--sky)', frame='Say this', face_pos='center 30%',
                talk_img='talk', talk_pos='center 30%', talk_text='Knee to knee.<br>Take turns.'),
        s5=dict(eyebrow='Watch Me, Then Show Me', color='var(--orange)', pos='center 40%', choice_pos='center 30%'),
        s6=dict(eyebrow='One Thing I Will Do', title='MY PROMISE TODAY', color='var(--red)',
                img='promise', pos='center 25%', frame='Point to one', choice_pos='center 30%'),
        s7=dict(eyebrow='How We Leave', title='HOW WE LEAVE', color='var(--green)', img='leave', pos='center 40%',
                steps=LEAVE_STEPS),
    ),
    poster=dict(header_img='welcome', footer_img='thumbs'),
    minibook=dict(
        back_title=('I did it!', '¡Lo logré!', 'Mwen fè l!'), back_img='promise', back_pos='center 20%',
        days=['Mon', 'Tue', 'Wed', 'Thu', 'Fri']),
    centers=dict(
        sort=dict(dirs=[('✂️', 'cut'), ('👀', 'look'), ('👉', 'sort')], title_size=None,
                  cards_title='SORT IT: PICTURE CARDS',
                  yes=dict(symbol='✓', size='40px', color='var(--green)', bg='var(--green-l)'),
                  no=dict(symbol='✋', size='36px', color='var(--red)', bg='var(--red-l)')),
        seq=dict(title='PUT IT IN ORDER', cards_title='PUT IT IN ORDER: CARDS',
                 dirs=[('👀', 'look'), ('🔢', '1 2 3 4'), ('🗣️', 'tell it')],
                 slots=['First', 'Next', 'Then', 'Last'], pos='center 35%'),
        roleplay=dict(title='ACT IT OUT', dirs=[('🃏', 'pick'), ('😠', 'show mad'), ('😌', 'show calm')]),
        strips=dict(count=4),
        color=dict(tag='🖍 color'),
    ),
    family=dict(
        hero_pos='center 15%',
        en=dict(eb='This week in Morning Meeting · Kindergarten to 2nd Grade', sayh='At school we say:',
                ch='Calm choices', th='Try at home', ft='Questions? Talk with your child’s teacher.'),
        es=dict(eb='Esta semana en la Reunión de la Mañana · Kínder a 2.º grado', sayh='En la escuela decimos:',
                ch='Opciones de calma', th='Practiquen en casa',
                ft='¿Preguntas? Hable con el maestro o la maestra de su hijo o hija.'),
        kr=dict(eb='Semèn sa a nan Reyinyon Maten · Kindègadenn rive 2yèm ane', sayh='Nan lekòl la nou di:',
                ch='Chwa pou kalme', th='Eseye lakay ou', ft='Ou gen kesyon? Pale ak pwofesè pitit ou a.'),
    ),
    guide=dict(
        before_title='Before you teach',
        lesson_title='The lesson, slide by slide',
        lesson_note='The same script is in the deck’s presenter notes. Press N while presenting.',
        bridges_title='Practice bridges for slide 5',
        bridges_note='Students model, not the teacher. The teacher narrates and asks the class what they saw.',
        centers_title='Centers',
        centers_note='Print one kit per group. Laminate the mats and cards so they last. Students work in groups of 2 to 4.',
        keys_title='Answer keys',
        minibook_title='The mini book (one child, Tier 2)',
        when_title='When it happens',
        when_intro='Follows the Responsive Behavior Plan: the adult response is the intervention. Fewer words as escalation rises.',
        when_outro='',
        family_title='Family connection',
        family=['Send the family half-sheet home the day you teach. It is in English, Spanish, and Haitian Creole.'],
    ),
    site=dict(
        hero_pos=None,
        deck_desc='Get calm, watch the story, turn and talk, practice, make a promise, and leave calmly.',
        guide_desc='The lesson at a glance, the slide-by-slide script, how to run the centers, and what to do when it happens.',
        poster_hint='Hang it at student eye level near your meeting space.',
        poster_large='The same poster, sized for a hallway or the front of the room.',
        centers_desc='Sort mat and 8 picture cards, sequencing mat and cards, role-play cards, desk strips, and a coloring page.',
        minibook_desc='A private, read-together story for students who need more practice. Read it one on one or in a small group.',
        family_desc='What your child is learning, what we say at school, and three things to try at home. One page per language, two half-sheets per page.',
    ),
)

REQUIRED = ['num', 'slug', 'file_prefix', 'deck_slug', 'title', 'full_title', 'title_lines', 'subtitle',
            'value', 'part', 'promise', 'card_line', 'choices', 'choices_head', 'deck', 'poster', 'minibook',
            'centers', 'family', 'guide', 'site']


def resolve(topic):
    """Return a full topic: defaults merged under the topic file, derived values filled in, shape checked."""
    missing = [k for k in REQUIRED if k not in topic]
    if missing:
        raise KeyError(f'Topic is missing: {", ".join(missing)}')
    T = deep_merge(DEFAULTS, topic)
    T.setdefault('song', None)
    T['promise'] = dict(zip(LANGS, lang3(T['promise'])))
    T['choices_head'] = dict(zip(LANGS, lang3(T['choices_head'])))
    ch = T['choices']
    D = T['deck']
    D.setdefault('eyebrow', f"Morning Meeting · {T['value']}")
    D['s5'].setdefault('choices', ch)
    D['s6'].setdefault('choices', ch[:3])
    assert len(D['notes']) == 7, 'deck.notes needs one entry per slide (7)'
    P = T['poster']
    P.setdefault('choices', ch)
    P.setdefault('choices_head', T['choices_head'])
    P.setdefault('say', T['promise'])
    P['say'] = dict(zip(LANGS, lang3(P['say'])))
    assert len(P['panels']) == 4, 'poster.panels needs 4 panels (2 x 2 grid)'
    M = T['minibook']
    assert len(M['pages']) == 6, 'minibook.pages needs 6 pages (cover + 6 + back = 4 sheets)'
    C = T['centers']
    C['roleplay'].setdefault('choices', ch)
    C['strips'].setdefault('choices', ch)
    C['strips'].setdefault('head', T['choices_head'])
    C['strips']['head'] = dict(zip(LANGS, lang3(C['strips']['head'])))
    col = C['color']
    assert ('png' in col) != ('trace' in col), 'centers.color needs exactly one of png (ready art) or trace (image to trace)'
    F = T['family']
    F.setdefault('choices', ch)
    F.setdefault('hero', 'high_five')
    return T

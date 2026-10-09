"""The 12 K-2 Behavior Toolkit topics in teaching order: the registry the toolkit home page is built from.

status: 'live' shows a "Ready to teach" card linking to <slug>/index.html plus an Offline ZIP row;
        'soon' shows a "Coming soon" card. A topic whose folder has been published is shown as live
        even if it still says 'soon' here, but set it to 'live' when you publish so this file stays true.
thumb:  image key for the live card (copied to resources/k2-behavior-toolkit/shared/img/<key>.jpg on publish).
title and line must match the topic file's full_title and card_line.
"""

TOPICS = [
    dict(num=1, title='Naming My Feelings', line='I can name how I feel.',
         part='Skills I can use', slug='01-naming-my-feelings', status='soon', thumb=None),
    dict(num=2, title='Using the Calm Corner', line='I can use the calm corner, get calm, and come back.',
         part='Skills I can use', slug='02-calm-corner', status='live', thumb='in_corner'),
    dict(num=3, title='Belly Breathing', line='I can breathe slow to calm my body.',
         part='Skills I can use', slug='03-belly-breathing', status='soon', thumb=None),
    dict(num=4, title='Asking for a Break', line='I can ask for a break with my words or my card.',
         part='Skills I can use', slug='04-asking-for-a-break', status='soon', thumb=None),
    dict(num=5, title="Getting a Grown-Up's Attention", line="I can get a grown-up's help the safe way.",
         part='Skills I can use', slug='05-grown-up-attention', status='soon', thumb=None),
    dict(num=6, title='Fixing It', line='I can help make it right.',
         part='Skills I can use', slug='06-fixing-it', status='soon', thumb=None),
    dict(num=7, title='Gentle Hands with Friends', line='I use gentle hands. I keep my friends safe.',
         part='Safe choices', slug='07-gentle-hands', status='live', thumb='high_five'),
    dict(num=8, title='Gentle Hands with Grown-Ups', line='I keep my grown-ups safe too.',
         part='Safe choices', slug='08-gentle-hands-grown-ups', status='soon', thumb=None),
    dict(num=9, title='Things Stay Safe', line='I keep our things safe and in their place.',
         part='Safe choices', slug='09-things-stay-safe', status='soon', thumb=None),
    dict(num=10, title='School Words', line='I use kind school words, even when I am mad.',
         part='Safe choices', slug='10-school-words', status='soon', thumb=None),
    dict(num=11, title='Right-Size Voice', line='I use the right voice for the place.',
         part='Safe choices', slug='11-right-size-voice', status='soon', thumb=None),
    dict(num=12, title='I Stay With My Class', line='I stay with my class so I stay safe.',
         part='Safe choices', slug='12-i-stay-with-my-class', status='soon', thumb=None),
]


def find(slug):
    return next((t for t in TOPICS if t['slug'] == slug), None)

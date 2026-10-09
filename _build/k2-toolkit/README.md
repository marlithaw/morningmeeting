# K–2 SEL Toolkit builder

Source files for the K–2 Behavior Toolkit on the Morning Meeting site. GitHub Pages does not
publish folders that start with an underscore, so nothing here appears on the site.

- `assets/img/` curated, named images the builder uses (key = file name without .jpg)
- `assets/library/` every Flow image so far, compressed, for reuse in later topics
- `assets/fonts/` Lilita One, Fredoka, Andika (OFL)
- `legacy/gentle-hands/` the original one-off scripts for Topic 7 (reference only)
- `music/<topic>/` song source files and music-video timing

Lee & Tee characters © AH-HA Coaching and Consulting, used with permission.

## How to build a topic

Everything a topic says lives in one content file, `topics/NN-slug.py` (a `TOPIC` dict). The builder in `builder/`
turns it into the full bundle. `topics/07-gentle-hands.py` is the complete reference; `builder/shared.py` holds the
shared calm choices (`COPING`), the breathing cards, and the defaults a topic can leave out.

```
python3 build.py topics/07-gentle-hands.py                       # everything into out/07-gentle-hands/
python3 build.py topics/07-gentle-hands.py --only deck,poster    # some parts: deck, poster, minibook, centers,
                                                                 #   family, guide, song, thumbs, zip, site
python3 build.py topics/07-gentle-hands.py --publish             # also copy into resources/k2-behavior-toolkit/<slug>/
                                                                 #   and regenerate the toolkit home from toolkit.py
python3 build.py topics/07-gentle-hands.py --publish --publish-root /tmp/k2-test   # test publish (or K2_PUBLISH_ROOT)
python3 music/build_mv.py 07-gentle-hands --clips <folder>       # captioned song video into out/<slug>/<deck>-song.mp4
python3 music/build_mv.py 07-gentle-hands --dry-run              # captions + ffmpeg command only
python3 builder/lineart.py <image key> out.png                   # coloring-page line art from a picture
```

Checklist for a new topic:

1. Copy `topics/07-gentle-hands.py` to `topics/NN-slug.py` and replace the content (identity, deck, notes, poster,
   mini book, center kit, family text, teacher guide, site text). Keep the 7 notes, 4 poster panels, and 6 mini book pages.
2. Put new images in `assets/img/` as `<key>.jpg` (or `.png`) and refer to them by key. For the coloring page, use
   `color=dict(png='<key>')` for ready line art or `color=dict(trace='<key>')` to trace a picture.
3. Build into `out/NN-slug/`. Until the song exists (`song=None` or no video found), the deck has no Play the song
   button and the topic page has no Watch section.
4. Check: render every PDF page and look at it, step through all 7 slides with notes (N), open `out/NN-slug/index.html`.
5. Set the topic to `status='live'` (and its `thumb`) in `toolkit.py`, then `--publish`. Check every local link and the
   Weekly Videos and Do Now – First 5 links on the topic page and toolkit home before opening the PR.

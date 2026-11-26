# Winter Wonderland theme layer (weeks of Nov 30, Dec 7, Dec 14, 2026).
# Each builder appends the matching block after the template's own styles when the week's content file sets WINTER = True.
# Palette: midnight navy, frost, ice blue, cranberry, evergreen, warm gold. Snow and string lights are CSS only,
# sit above the slide content with pointer-events off, and stop moving for reduced-motion users.

NAVY, NAVY2, FROST, ICE, SKY = '#0E2244', '#1B3A6B', '#F3F9FE', '#D7ECFA', '#8EC5EC'
CRAN, CRAN2, PINE, PINE2, GOLD = '#B3203B', '#8C1730', '#146B54', '#0D4A3B', '#E9C46A'

SNOW_DARK = ('radial-gradient(circle at 20% 30%,rgba(255,255,255,.95) 0 2px,transparent 3px),'
             'radial-gradient(circle at 70% 60%,rgba(255,255,255,.8) 0 1.5px,transparent 2.5px),'
             'radial-gradient(circle at 45% 85%,rgba(255,255,255,.9) 0 2.5px,transparent 3.5px),'
             'radial-gradient(circle at 85% 15%,rgba(255,255,255,.7) 0 1px,transparent 2px)')
SNOW_LIGHT = SNOW_DARK.replace('255,255,255,', '142,197,236,')
LIGHTS = (f'radial-gradient(circle at 12px 14px,{GOLD} 0 5px,transparent 6px) 0 0/96px 26px repeat-x,'
          f'radial-gradient(circle at 36px 18px,{CRAN} 0 5px,transparent 6px) 0 0/96px 26px repeat-x,'
          f'radial-gradient(circle at 60px 14px,{SKY} 0 5px,transparent 6px) 0 0/96px 26px repeat-x,'
          f'radial-gradient(circle at 84px 18px,#3FBF8F 0 5px,transparent 6px) 0 0/96px 26px repeat-x,'
          'linear-gradient(transparent 7px,rgba(30,40,60,.55) 7px 9px,transparent 9px) 0 0/100% 26px no-repeat')
KEYS = ('@keyframes wwsnow{from{background-position:0 0,0 0,0 0,0 0}to{background-position:40px 220px,-30px 160px,20px 300px,-10px 120px}}'
        '@media (prefers-reduced-motion:reduce){.ww-snow,.slide::after,.hero::after,#stage::after,header::after{animation:none!important}}')


def _snow(sel, light=False, opacity=.75):
    img = SNOW_LIGHT if light else SNOW_DARK
    return (f'{sel}{{content:"";position:absolute;inset:0;pointer-events:none;z-index:40;opacity:{opacity};'
            f'background-image:{img};background-size:220px 220px,160px 160px,300px 300px,120px 120px;animation:wwsnow 22s linear infinite}}')


def _lights(sel, top=0):
    return f'{sel}{{content:"";position:absolute;left:0;right:0;top:{top}px;height:26px;pointer-events:none;z-index:41;background:{LIGHTS}}}'


# Morning Meeting lesson decks
DECK_CSS = ('<style>/* winter wonderland */'
            f':root{{--charcoal:{NAVY};--spark-red:{CRAN};--ember:{CRAN2};--mb-yellow:#F6E3A8;--ink:#0F1E36;--slate:#3E5373}}'
            'html,body{background:#081630}'
            f'.slide{{background:linear-gradient(180deg,{FROST},{ICE})}}'
            f'.slide.dark{{background:radial-gradient(ellipse at 82% -10%,rgba(142,197,236,.38),transparent 55%),linear-gradient(180deg,{NAVY},{NAVY2})}}'
            f'.slide.red{{background:radial-gradient(ellipse at 12% 112%,rgba(233,196,106,.32),transparent 52%),linear-gradient(160deg,{PINE},{PINE2})}}'
            '.slide.yellow{background:linear-gradient(180deg,#FCF3D6,#F3DFA2)}'
            '.slide .frame,.slide .item,.slide .step,.slide .qrow{border-color:rgba(14,34,68,.25)}'
            f'.notes{{border-top-color:{GOLD}}}'
            + _lights('.slide::before') + _snow('.slide.dark::after,.slide.red::after') + _snow('.slide:not(.dark):not(.red)::after', light=True, opacity=.55)
            + KEYS + '</style>')

# Spark decks
SPARK_CSS = ('<style>/* winter wonderland */'
             f':root{{--red:{CRAN};--ember:{CRAN2};--yellow:#CFE7F8;--charcoal:{NAVY};--paper:{FROST};--ink:#0F1E36}}'
             'html,body{background:#081630}'
             f'.slide{{background:linear-gradient(180deg,{FROST},#E6F2FB)}}'
             f'.hd{{background:linear-gradient(90deg,#CFE7F8,#E9F4FD)!important;border-bottom-color:{NAVY}!important;position:relative}}'
             f'.b68 .hd{{background:linear-gradient(90deg,{NAVY},{NAVY2})!important;border-bottom-color:{GOLD}!important}}'
             f'.b68 .slide{{background:linear-gradient(180deg,#EEF4FA,#DCE9F5)}}'
             f'.b1k .slide.dark,.b23 .slide.dark,.b45 .slide.dark,.b68 .slide.dark,.slide.dark{{background:radial-gradient(ellipse at 85% -10%,rgba(233,196,106,.35),transparent 55%),linear-gradient(180deg,{NAVY},{NAVY2})!important}}'
             f'.w5bar{{background:{NAVY}!important;box-shadow:6px 6px 0 {CRAN}!important}}'
             + _lights('.slide::before', top=-9) + _snow('.slide.dark::after') + _snow('.slide:not(.dark)::after', light=True, opacity=.45)
             + KEYS + '</style>')

# Ember boards: a cozy fire on a snowy night
EMBER_CSS = ('<style>/* winter wonderland */'
             f':root{{--dusk:{NAVY};--charcoal:{NAVY};--paper:{FROST};--red:{CRAN};--ember:{CRAN2}}}'
             'html,body{background:#071226}'
             f'.hd{{background:linear-gradient(90deg,{NAVY},{NAVY2} 60%,#24467C)!important;position:relative}}'
             f'#stage{{background:linear-gradient(180deg,{FROST},{ICE})}}'
             + _lights('.hd::before', top=-9) + _snow('#stage::after', light=True, opacity=.4)
             + KEYS + '</style>')

# Unit hub, teacher guide, printables, media (site.css pages)
PAGE_CSS = ('<style>/* winter wonderland */'
            f':root{{--charcoal:{NAVY};--red:{CRAN};--ember:{CRAN2};--yellow:#F6E3A8}}'
            f'body{{background:{FROST}}}'
            f'.hero{{position:relative;overflow:hidden;background:radial-gradient(ellipse at 85% -20%,rgba(142,197,236,.4),transparent 55%),linear-gradient(180deg,{NAVY},{NAVY2});border-bottom-color:{CRAN}}}'
            '.hero .kicker::before{content:"❄ ";color:#CFE7F8}'
            + _lights('.hero::before') + _snow('.hero::after') + KEYS
            + '@media print{.hero::before,.hero::after{display:none}}</style>')

# Spark + Ember package page and teacher guide
PKG_CSS = ('<style>/* winter wonderland */'
           f'body{{background:{FROST}!important;color:#0F1E36}}'
           f'header{{position:relative;overflow:hidden;background:radial-gradient(ellipse at 85% -20%,rgba(142,197,236,.4),transparent 55%),linear-gradient(180deg,{NAVY},{NAVY2})!important;border-bottom-color:{CRAN}!important}}'
           f'header p{{color:{GOLD}!important}}'
           f'a{{background:{CRAN}}}section{{border-color:#CFE0EE}}'
           + _lights('header::before') + _snow('header::after') + KEYS
           + '@media print{header::before,header::after{display:none}}</style>')

# Printable PDFs (student pages, slips): print-friendly, navy bar with a snowflake
PDF_CSS = (f'.bar{{background:{NAVY}!important;border-bottom:4px solid {CRAN}}}.bar small{{color:{GOLD}!important}}'
           '.bar b::after{content:"  ❄";color:#CFE7F8}'
           f'.art{{border-color:{NAVY}!important}}')

# Hub sections for winter weeks (index.html): a frosty band at the top of the week's section
HUB_SECTION_STYLE = (f'background:linear-gradient(180deg,{FROST},#fff 140px);border-top:6px solid {SKY};border-radius:14px')

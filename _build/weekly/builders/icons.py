S='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">{}</svg>'
P='fill="none" stroke="#232323" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"'
ICONS={
'walk': S.format(f'<circle cx="54" cy="14" r="8" {P}/><path d="M50 26 L40 54 L52 62 L46 90 M44 40 L28 50 M48 34 L66 44 M40 54 L28 86" {P}/>'),
'tray': S.format(f'<path d="M8 62 H92 L84 76 H16 Z" {P}/><circle cx="34" cy="48" r="12" {P}/><path d="M58 36 V58 M66 36 V58 M74 36 V58" {P}/>'),
'ball': S.format(f'<circle cx="50" cy="50" r="36" {P}/><path d="M14 50 H86 M50 14 V86 M24 24 Q50 50 24 76 M76 24 Q50 50 76 76" {P}/>'),
'fix': S.format(f'<path d="M62 12 A20 20 0 0 0 46 40 L14 72 A8 8 0 0 0 26 84 L58 52 A20 20 0 0 0 86 36 L74 42 L62 36 L58 24 Z" {P}/>'),
'own': S.format(f'<circle cx="50" cy="22" r="11" {P}/><path d="M28 90 V56 Q50 34 72 56 V90" {P}/><path d="M50 50 V72 M40 62 H60" fill="none" stroke="#E21C24" stroke-width="6" stroke-linecap="round"/>'),
'sorry': S.format(f'<path d="M12 15 H88 V65 H48 L25 85 V65 H12 Z" {P}/><path d="M50 30 C44 22 32 26 36 36 L50 50 L64 36 C68 26 56 22 50 30Z" fill="#E21C24" stroke="none"/>'),
'scale': S.format(f'<path d="M50 14 V86 M30 86 H70 M18 30 H82 M18 30 L8 56 H28 Z M82 30 L72 56 H92 Z" {P}/>'),
'door': S.format(f'<path d="M22 90 V12 H70 V90 M10 90 H90 M58 52 H60" {P}/><path d="M70 12 L84 20 V82 L70 90" {P}/>'),'mic': S.format(f'<rect x="38" y="10" width="24" height="44" rx="12" {P}/><path d="M26 42 Q26 66 50 66 Q74 66 74 42 M50 66 V86 M36 88 H64" {P}/>'),
'blocks': S.format(f'<rect x="14" y="62" width="34" height="26" {P}/><rect x="52" y="62" width="34" height="26" {P}/><rect x="33" y="34" width="34" height="26" {P}/><rect x="40" y="8" width="20" height="24" fill="#E21C24" stroke="#232323" stroke-width="5" stroke-linejoin="round"/>'),
'badge': S.format(f'<rect x="20" y="22" width="60" height="68" rx="8" {P}/><path d="M40 10 H60 V24 H40 Z" {P}/><circle cx="50" cy="48" r="10" {P}/><path d="M32 78 Q50 60 68 78" {P}/>'),
'thumb': S.format(f'<path d="M14 46 H30 V88 H14 Z M30 50 L46 16 Q56 14 56 26 L52 42 H80 Q88 44 86 54 L78 82 Q76 88 68 88 H30" {P}/>'),
'chat2': S.format(f'<path d="M8 12 H58 V46 H30 L16 60 V46 H8 Z" {P}/><path d="M42 54 H92 V86 H84 V98 L70 86 H42 Z" fill="none" stroke="#E21C24" stroke-width="5" stroke-linejoin="round"/>'),
'hands': S.format(f'<path d="M10 70 Q30 52 60 58 L88 50 M10 54 Q32 38 62 44 L90 36 M14 38 Q36 24 64 30 L88 22" {P}/><circle cx="50" cy="80" r="6" fill="#E21C24"/>'),
'plus': S.format(f'<circle cx="50" cy="50" r="38" {P}/><path d="M50 30 V70 M30 50 H70" fill="none" stroke="#E21C24" stroke-width="7" stroke-linecap="round"/>'),
'loop': S.format(f'<path d="M78 40 A30 30 0 1 0 80 62" {P}/><path d="M66 36 L80 40 L84 24" {P}/>'),
}

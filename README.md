# Post-Generator

Dieses Repo enthält HTML-Generatoren für Instagram-Posts (H.264/MP4 oder WebM per MediaRecorder), inkl. animierter Canvas-Overlays.

## Dateien
- `instagram_post_h264_final.html` – ursprüngliche Version mit H.264/WebM-Fallback
- `instagram_post_h264_arc6705.html` – Variante für das Bild `_ARC6705.jpg` (DE)
- `instagram_post_h264_arc6705_en.html` – englische Version (EN)
- `instagram_post_h264_arc6705_pl.html` – polnische Version (PL)

## Starten (lokal)
Optionaler lokaler Server, dann Seiten im Browser öffnen:

1) Port freimachen und Server starten

2) Seite aufrufen, z. B.:
- `http://localhost:8080/instagram_post_h264_arc6705.html`
- `http://localhost:8080/instagram_post_h264_arc6705_en.html`
- `http://localhost:8080/instagram_post_h264_arc6705_pl.html`

Hinweis: Je nach Browser kann kein MP4 direkt aufgenommen werden, dann wird automatisch WebM erzeugt. Der Dateiname und die UI passen sich an.
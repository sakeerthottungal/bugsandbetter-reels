# Reel toolkit
Final step for every reel: python3 -c "import make_reel as m; m.add_sound('in.mp4','out_snd.mp4')" -> post the _snd file (typing sound). 
cd toolkit; python3 -c "import make_reel as m; m.render(QUOTE_LIST,'out.mp4')"; last.png = final frame (use as cover).
QUOTE_LIST = [hook, [3 short clauses], "But ...", "**Verb. Verb. Verb.**", "That's how you X, not just **Y**."]  (** = bold/white words)
Needs: Pillow, ffmpeg, DejaVu Sans Mono fonts. Run from inside toolkit/.

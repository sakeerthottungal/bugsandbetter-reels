import make_reel as m, shutil
q=["GTS 6 is not **GTS 5**.",["It has new features,","fresh bugs,","and bigger promises."],"But newer is not automatically better.","**Test. Compare. Decide.**","That's how you upgrade, not just **follow hype**."]
m.render(q,"gts.mp4",wps=5.5)
shutil.copy("last.png","gts_cover.png")
m.add_sound("gts.mp4","gts_snd.mp4")

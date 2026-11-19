import make_reel as m
q1=["Cynicism is not **realism**.",["It has doubt,","sarcasm,","and a wall around hope."],"But it blocks good chances.","**Ask. Test. Trust.**","That's how you stay sharp, not just **guarded**."]
q2=["Impatience is not **ambition**.",["It has rushed calls,","short tempers,","and half-built work."],"But speed without care backfires.","**Pause. Plan. Finish.**","That's how you go far, not just **fast**."]
for q,n in((q1,"reel1.mp4"),(q2,"reel2.mp4")):
    m.render(q,n,wps=5.5)
    import shutil;shutil.copy("last.png",n.replace("reel","cover").replace(".mp4",".png"))
    m.add_sound(n,n.replace(".mp4","_snd.mp4"))

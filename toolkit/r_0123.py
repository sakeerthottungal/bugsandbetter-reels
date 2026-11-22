import make_reel as m, shutil
q1=["Hustle is not **purpose**.",["It has late nights,","empty weekends,","and a vague finish line."],"But rest is part of work.","**Plan. Pause. Push.**","That's how you last, not just **look busy**."]
q2=["Being late is not **busy**.",["It has rushed excuses,","waiting people,","and borrowed trust."],"But one early day changes it.","**Plan. Leave. Arrive.**","That's how you earn trust, not just **forgiveness**."]
for q,n in((q1,"reel1.mp4"),(q2,"reel2.mp4")):
    m.render(q,n,wps=5.5)
    shutil.copy("last.png",n.replace("reel","cover").replace(".mp4",".png"))
    m.add_sound(n,n.replace(".mp4","_snd.mp4"))

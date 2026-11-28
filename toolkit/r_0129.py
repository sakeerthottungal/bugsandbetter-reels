import make_reel as m, shutil
q1=["Hoarding information is not **control**.",["It has locked folders,","late updates,","and a stuck team."],"But shared context moves work faster.","**Share. Explain. Trust.**","That's how you build a team, not just **a bottleneck**."]
q2=["A clique is not a **team**.",["It has inside jokes,","closed circles,","and quiet outsiders."],"But one invite can change the room.","**Notice. Include. Repeat.**","That's how you build belonging, not just **a circle**."]
for q,n in((q1,"reel1.mp4"),(q2,"reel2.mp4")):
    m.render(q,n,wps=5.5)
    shutil.copy("last.png",n.replace("reel","cover").replace(".mp4",".png"))
    m.add_sound(n,n.replace(".mp4","_snd.mp4"))

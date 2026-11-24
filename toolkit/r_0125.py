import make_reel as m, shutil
q1=["Passive aggression is not **honesty**.",["It has sarcasm,","cold shoulders,","and hints nobody can answer."],"But say it plainly.","**Name it. Ask. Resolve.**","That's how you clear tension, not just **hide it**."]
q2=["A bad mood is not **leadership**.",["It has short replies,","tense rooms,","and people who tiptoe."],"But the team feels it first.","**Pause. Breathe. Reset.**","That's how you lead, not just **react**."]
for q,n in((q1,"reel1.mp4"),(q2,"reel2.mp4")):
    m.render(q,n,wps=5.5)
    shutil.copy("last.png",n.replace("reel","cover").replace(".mp4",".png"))
    m.add_sound(n,n.replace(".mp4","_snd.mp4"))

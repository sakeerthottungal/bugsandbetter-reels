import make_reel as m, shutil
q1=["Motivation is not **discipline**.",["It has hype,","big plans,","and a short shelf life."],"But mood never shows up daily.","**Start. Stay. Repeat.**","That's how you finish, not just **feel ready**."]
q2=["Positivity is not **honesty**.",["It has forced smiles,","quick fixes,","and unspoken worries."],"But ignored feelings don't vanish.","**Pause. Name it. Act.**","That's how you heal, not just **pretend**."]
for q,n in((q1,"reel1.mp4"),(q2,"reel2.mp4")):
    m.render(q,n,wps=5.5)
    shutil.copy("last.png",n.replace("reel","cover").replace(".mp4",".png"))
    m.add_sound(n,n.replace(".mp4","_snd.mp4"))

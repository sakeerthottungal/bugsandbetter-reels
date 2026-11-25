import make_reel as m, shutil
q1=["Interrupting is not **engagement**.",["It has half-heard ideas,","cut-off sentences,","and people who stop sharing."],"But listening costs nothing.","**Wait. Hear. Respond.**","That's how you build trust, not just **talk over it**."]
q2=["Favoritism is not **loyalty**.",["It has quiet resentment,","unfair chances,","and good people leaving."],"But everyone sees it.","**Notice. Include. Rotate.**","That's how you build a team, not just **a circle**."]
for q,n in((q1,"reel1.mp4"),(q2,"reel2.mp4")):
    m.render(q,n,wps=5.5)
    shutil.copy("last.png",n.replace("reel","cover").replace(".mp4",".png"))
    m.add_sound(n,n.replace(".mp4","_snd.mp4"))

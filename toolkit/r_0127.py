import make_reel as m, shutil
q1=["Ghosting is not **being busy**.",["It has unread messages,","stalled work,","and people left guessing."],"But a short reply is enough.","**Read. Reply. Close.**","That's how you earn trust, not just **dodge questions**."]
q2=["Office politics is not **strategy**.",["It has side deals,","hidden agendas,","and work nobody trusts."],"But clarity beats clever.","**Speak. Share. Own.**","That's how you build influence, not just **alliances**."]
for q,n in((q1,"reel1.mp4"),(q2,"reel2.mp4")):
    m.render(q,n,wps=5.5)
    shutil.copy("last.png",n.replace("reel","cover").replace(".mp4",".png"))
    m.add_sound(n,n.replace(".mp4","_snd.mp4"))

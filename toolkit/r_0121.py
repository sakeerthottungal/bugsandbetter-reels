import make_reel as m, shutil
q1=["Comfort is not **peace**.",["It has routine,","safe choices,","and a quiet fear of trying."],"But it slowly shrinks you.","**Try. Stumble. Repeat.**","That's how you grow, not just **settle**."]
q2=["Scrolling is not **rest**.",["It has endless tabs,","tired eyes,","and a restless mind."],"But it never recharges you.","**Pause. Breathe. Walk.**","That's how you recover, not just **escape**."]
for q,n in((q1,"reel1.mp4"),(q2,"reel2.mp4")):
    m.render(q,n,wps=5.5)
    shutil.copy("last.png",n.replace("reel","cover").replace(".mp4",".png"))
    m.add_sound(n,n.replace(".mp4","_snd.mp4"))

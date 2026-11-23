import make_reel as m, shutil
q1=["FOMO is not **ambition**.",["It has endless scrolling,","constant comparing,","and chasing every trend."],"But you can't do everything.","**Choose. Commit. Finish.**","That's how you grow, not just **keep up**."]
q2=["Being right is not **winning**.",["It has cold silence,","bruised egos,","and people who stop talking."],"But the team remembers.","**Listen. Ask. Adjust.**","That's how you lead, not just **argue**."]
for q,n in((q1,"reel1.mp4"),(q2,"reel2.mp4")):
    m.render(q,n,wps=5.5)
    shutil.copy("last.png",n.replace("reel","cover").replace(".mp4",".png"))
    m.add_sound(n,n.replace(".mp4","_snd.mp4"))

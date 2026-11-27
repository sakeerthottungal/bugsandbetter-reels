import make_reel as m, shutil
q1=["A long meeting is not **progress**.",["It has slides,","side talk,","and no owner."],"But one clear decision is enough.","**Decide. Assign. Leave.**","That's how you move work, not just **fill calendars**."]
q2=["Last-minute changes are not **agility**.",["They have late nights,","rushed fixes,","and a tired team."],"But a plan shared early saves weeks.","**Plan. Share. Stick.**","That's how you lead change, not just **cause chaos**."]
for q,n in((q1,"reel1.mp4"),(q2,"reel2.mp4")):
    m.render(q,n,wps=5.5)
    shutil.copy("last.png",n.replace("reel","cover").replace(".mp4",".png"))
    m.add_sound(n,n.replace(".mp4","_snd.mp4"))

import make_reel as m
q1=["Delegating is not **abandoning**.",["It has trust,","clear goals,","and some discomfort."],"But hovering kills growth.","**Explain. Release. Review.**","That's how you build leaders, not just **finish tasks**."]
q2=["Bad news is not **betrayal**.",["It has early warnings,","honest data,","and time to fix it."],"But late news costs double.","**Speak. Listen. Fix.**","That's how you build trust, not just **look fine**."]
for i,q in enumerate([q1,q2],1):
    m.render(q,f'reel{i}.mp4',wps=5.5)
    import shutil;shutil.copy('last.png',f'cover{i}.png')
    m.add_sound(f'reel{i}.mp4',f'reel{i}_snd.mp4')

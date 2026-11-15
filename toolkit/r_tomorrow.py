import make_reel as m, shutil
q1=["Micromanaging is not **care**.",["It has hovering,","constant check-ins,","and a fear of letting go."],"But it shrinks your team.","**Brief. Trust. Step back.**","That's how you grow people, not just **control tasks**."]
q2=["Multitasking is not **skill**.",["It has constant switching,","shallow work,","and tired attention."],"But it halves your quality.","**Pick. Block. Finish.**","That's how you do good work, not just **feel productive**."]
for i,q in enumerate([q1,q2],1):
    m.render(q,f'reel{i}.mp4',wps=5.5)
    shutil.copy('last.png',f'cover{i}.png')
    m.add_sound(f'reel{i}.mp4',f'reel{i}_snd.mp4')

import make_reel as m, shutil
q1=["Blame is not **feedback**.",["It has anger,","pointing fingers,","and a team that hides."],"But it hides the real problem.","**Pause. Ask. Fix.**","That's how you solve it, not just **assign fault**."]
q2=["Complaining is not **venting**.",["It has loops,","bad moods,","and zero next steps."],"But it spreads fast.","**Name it. Choose. Act.**","That's how you move on, not just **stay upset**."]
for i,q in enumerate([q1,q2],1):
    m.render(q,f'reel{i}.mp4',wps=5.5)
    shutil.copy('last.png',f'cover{i}.png')
    m.add_sound(f'reel{i}.mp4',f'reel{i}_snd.mp4')

import make_reel as m, shutil
q1=["Ego is not **confidence**.",["It has defensiveness,","image control,","and a fear of being wrong."],"But it costs honest feedback.","**Listen. Own. Learn.**","That's how you earn respect, not just **protect your image**."]
q2=["Gossip is not **bonding**.",["It has whispers,","side glances,","and trust that quietly leaks."],"But it travels back to you.","**Pause. Redirect. Speak up.**","That's how you build trust, not just **fit in**."]
for i,q in enumerate([q1,q2],1):
    m.render(q,f'reel{i}.mp4',wps=5.5)
    shutil.copy('last.png',f'cover{i}.png')
    m.add_sound(f'reel{i}.mp4',f'reel{i}_snd.mp4')

import make_reel as m, shutil
q1=["Listening is not **waiting**.",["It has questions,","silence,","and full attention."],"But interrupting costs trust.","**Pause. Ask. Hear.**","That's how you understand people, not just **reply fast**."]
q2=["Clear expectations are not **control**.",["They have a goal,","a deadline,","and a shared picture of done."],"But vague costs everyone.","**Define. Confirm. Check.**","That's how you build trust, not just **assign tasks**."]
for i,q in enumerate([q1,q2],1):
    m.render(q,f'reel{i}.mp4',wps=5.5)
    shutil.copy('last.png',f'cover{i}.png')
    m.add_sound(f'reel{i}.mp4',f'reel{i}_snd.mp4')

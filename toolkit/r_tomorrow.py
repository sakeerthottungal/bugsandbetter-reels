import make_reel as m, shutil
q1=["Excuses are not **reasons**.",["It has comfort,","blame,","and a story you keep retelling."],"But it keeps you stuck.","**Own. Adjust. Move.**","That's how you grow, not just **explain why not**."]
q2=["Rushing is not **speed**.",["It has skipped checks,","sloppy replies,","and a redo later."],"But slow is not the answer.","**Plan. Check. Ship.**","That's how you move fast, not just **fix twice**."]
for i,q in enumerate([q1,q2],1):
    m.render(q,f'reel{i}.mp4',wps=5.5)
    shutil.copy('last.png',f'cover{i}.png')
    m.add_sound(f'reel{i}.mp4',f'reel{i}_snd.mp4')

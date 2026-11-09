import make_reel as m, shutil
q2=["Clarity is not **control**.",["It has a goal,","a deadline,","and a shared picture of done."],"But vague costs everyone.","**Define. Confirm. Check.**","That's how you build trust, not just **assign tasks**."]
m.render(q2,'reel2.mp4',wps=5.5)
shutil.copy('last.png','cover2.png')
m.add_sound('reel2.mp4','reel2_snd.mp4')

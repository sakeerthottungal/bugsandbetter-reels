import make_reel as m, shutil
q1=["Stubbornness is not **strength**.",["It has pride,","old habits,","and a fear of looking weak."],"But it costs you allies.","**Listen. Bend. Adapt.**","That's how you lead, not just **win arguments**."]
q2=["Overexplaining is not **clarity**.",["It has long replies,","nervous apologies,","and a point buried deep."],"But shorter lands better.","**Cut. Clarify. Stop.**","That's how you get heard, not just **talk more**."]
for i,q in enumerate([q1,q2],1):
    m.render(q,f'reel{i}.mp4',wps=5.5)
    shutil.copy('last.png',f'cover{i}.png')
    m.add_sound(f'reel{i}.mp4',f'reel{i}_snd.mp4')

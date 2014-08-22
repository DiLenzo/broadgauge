from blinker import signal

trainer_signup = signal('trainer_signup')
org_signup = signal('org_signup')
new_workshop = signal('new_workshop')
new_comment = signal('new_comment')
workshop_confirmed = signal('workshop_confirmed')
workshop_edited = signal('workshop_edited')
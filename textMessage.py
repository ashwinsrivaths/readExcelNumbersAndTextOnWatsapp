import pywhatkit



def sendWatsappMessage(name, phNo):
    text = getText(name)
    pywhatkit.sendwhatmsg_instantly("+91" + str(phNo), text)

def getText(name):
    return f'''Hi {name}
I have a job for a non technical roll - internet router helpline attender.
good communication skill in english and hindi is required.
The job is to receive customer calls on the helpline number and help them resolve the internet router issues.
please let me know if you are interested.'''
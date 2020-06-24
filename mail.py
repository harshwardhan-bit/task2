import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls() #tls for security

s.login("harshwardhankakra@gmail.com", "gmail9784")

message = "Your code has been deployed :)"

s.sendmail(("harshwardhankakra@gmail.com"), "harshwardhan17cs017@secs.ac.in", message)

s.quit()
s
 


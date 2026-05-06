import smtplib
from flask import Flask, request, redirect
from email.mime.text import MIMEText

app = Flask(__name__)

# Íàñòðîéêè âàøåé ïî÷òû
MY_EMAIL = "anymock@yandex.ru"
PASSWORD = "ngyxwfqlgnudswag" # Íå îáû÷íûé ïàðîëü, à ñïåöèàëüíûé äëÿ ïðèëîæåíèé

@app.route('/send_mail', methods=['POST'])
def send_mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Ôîðìèðóåì ïèñüìî
    msg_text = f"Èìÿ: {name}\nEmail: {email}\nÑîîáùåíèå: {message}"
    msg = MIMEText(msg_text)
    msg['Subject'] = 'Íîâàÿ çàÿâêà ñ ñàéòà'
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL

    try:
        # Íàñòðîéêà äëÿ Gmail/Yandex/Mail.ru (ïîðò 587 è TLS)
        with smtplib.SMTP("://gmail.com", 587) as server: # Çàìåíèòå íà smtp.yandex.ru äëÿ ßíäåêñà
            server.starttls()
            server.login(MY_EMAIL, PASSWORD)
            server.send_mail(MY_EMAIL, MY_EMAIL, msg.as_string())
        return "Óñïåøíî îòïðàâëåíî!"
    except Exception as e:
        return f"Îøèáêà: {e}"

if __name__ == "__main__":
    app.run(port=8080, debug=True)
Èñïîëüçóéòå êîä ñ îñòîðîæíîñòüþ.Øàã 2: Èçìåíèòå HTML-êîä ôîðìûÂ âàøåì index.html óêàæèòå â action, ÷òî äàííûå íóæíî ñëàòü íà àäðåñ çàïóùåííîãî Python-ñåðâåðà:html<form class="contact-form" action="http://127.0.0" method="POST">
    <input type="text" name="name" placeholder="Âàøå èìÿ" required>
    <input type="email" name="email" placeholder="Email" required>
    <textarea name="message" rows="5" placeholder="Ñîîáùåíèå"></textarea>
    <button type="submit" class="btn">Îòïðàâèòü ÷åðåç Python</button>
</form>

import smtplib
from flask import Flask, request, redirect
from email.mime.text import MIMEText

app = Flask(__name__)

# Настройки вашей почты
MY_EMAIL = "anymock@yandex.ru"
PASSWORD = "ngyxwfqlgnudswag" # Не обычный пароль, а специальный для приложений

@app.route('/send_mail', methods=['POST'])
def send_mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Формируем письмо
    msg_text = f"Имя: {name}\nEmail: {email}\nСообщение: {message}"
    msg = MIMEText(msg_text)
    msg['Subject'] = 'Новая заявка с сайта'
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL

    try:
        # Настройка для Gmail/Yandex/Mail.ru (порт 587 и TLS)
        with smtplib.SMTP("://gmail.com", 587) as server: # Замените на smtp.yandex.ru для Яндекса
            server.starttls()
            server.login(MY_EMAIL, PASSWORD)
            server.send_mail(MY_EMAIL, MY_EMAIL, msg.as_string())
        return "Успешно отправлено!"
    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    app.run(debug=True)
Используйте код с осторожностью.Шаг 2: Измените HTML-код формыВ вашем index.html укажите в action, что данные нужно слать на адрес запущенного Python-сервера:html<form class="contact-form" action="http://127.0.0" method="POST">
    <input type="text" name="name" placeholder="Ваше имя" required>
    <input type="email" name="email" placeholder="Email" required>
    <textarea name="message" rows="5" placeholder="Сообщение"></textarea>
    <button type="submit" class="btn">Отправить через Python</button>
</form>
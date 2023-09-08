import smtplib
from email.mime.text import MIMEText
from .models import Campaign, Subscriber


def send_campaign(campaign_id):
    campaign = Campaign.objects.get(pk=campaign_id)
    recipients = Subscriber.objects.get_active_subscribers()
    for subscriber in recipients:
        subject = campaign.subject
        message = MIMEText(campaign.html_content, 'html')
        message['From'] = 'hemasaitej@gmail.com'
        message['To'] = subscriber.email
        message['Subject'] = subject
        try:
            server = smtplib.SMTP('smtp.yourprovider.com', 587)
            server.starttls()
            server.login('your@email.com', 'your_password')
            server.sendmail('your@email.com', [subscriber.email], message.as_string())
            server.quit()
        except Exception as e:
            print(f"Error sending email to {subscriber.email}: {str(e)}")


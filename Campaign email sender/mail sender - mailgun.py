import requests
import threading

MAILGUN_API_KEY = '7438af13f1baad728ec240651d31ad8c-7ca144d2-fc4c4767'
MAILGUN_DOMAIN = 'sandbox90e7a1a5cf824c5ba87f5dada6d09d0e.mailgun.org'
MAILGUN_BASE_URL = f'https://api.mailgun.net/v3/{MAILGUN_DOMAIN}'

campaigns = [
    {
        'subject': 'Campaign 1',
        'preview_text': 'Preview text for Campaign 1',
        'article_url': 'https://www.google.com/',
        'html_content': '<p>HTML content for Campaign 1</p>',
        'plain_text_content': 'Plain text content for Campaign 1',
        'published_date': '2023-09-10',
        'receiver_email': 'manasamadhan8@gmail.com',
    },
    {
        'subject': 'Campaign 2',
        'preview_text': 'Preview text for Campaign 2',
        'article_url': 'https://www.google.com/',
        'html_content': '<p>HTML content for Campaign 2</p>',
        'plain_text_content': 'Plain text content for Campaign 2',
        'published_date': '2023-09-11',
        'receiver_email': 'manasamadhan8@gmail.com',
    },
]


def send_email(api_key,email_data):
    try:
        response = requests.post(
            f'{MAILGUN_BASE_URL}/messages',
            auth=('api', api_key),
            data=email_data
        )
        response.raise_for_status()
        print(f"Email sent to {email_data['to']} - Subject: {email_data['subject']}")

    except Exception as e:
        print(f"Error sending email to {email_data['to']}: {str(e)}")


def send_campaign(campaign):
    email_data = {
        'from': f'hemasaitej@gmail.com',
        'subject': campaign['subject'],
        'to': campaign['receiver_email'],
        'html': campaign['html_content'],
    }
    send_email(MAILGUN_API_KEY, email_data)


def main():
    threads = []
    for campaign in campaigns:
        thread = threading.Thread(target=send_campaign, args=(campaign,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()

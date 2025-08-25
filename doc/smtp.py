import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP 서버 설정
# smtp_server = 'smtp.naver.com'
# smtp_port = 465  # SMTP 서버의 포트 번호 (보통 587 또는 465)

# 보내는 이메일 계정 정보
sender_email = 'okuo94@naver.com'
password = 'qf10477wg147@'

# 수신자 이메일 주소
receiver_email = 'okuo94@naver.com'

# 이메일 내용 설정
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = '파이썬을 이용한 이메일 전송'

# 이메일 내용
body = '파이썬으로 이메일을 보내봅니다.'
message.attach(MIMEText(body, 'plain'))

# SMTP 서버 연결 및 이메일 전송
try:
    server = smtplib.SMTP("smtp.naver.com", 587)
    server.starttls()  # TLS 암호화 사용
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print('이메일이 성공적으로 전송되었습니다.')
except Exception as e:
    print('이메일을 보내는 중 오류가 발생했습니다:', str(e))
finally:
    server.quit()  # SMTP 서버 연결 종료

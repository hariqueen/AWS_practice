from polly_client import create_polly_client
from text_to_speech import synthesize_speech, save_speech

# 환경 설정 및 클라이언트 생성
polly_client = create_polly_client()

# 텍스트를 음성으로 변환
# response = synthesize_speech(polly_client, "Hey there, I'm Hailey. You know what? I'm already at home, but I'm feeling this strong urge to go home. Does that sound confusing? I know. I can't quite explain it either, but I just really want to be at home.")

response = synthesize_speech(polly_client, "shi-ball, na zip ae gagoshipa.")


# 음성 파일 저장
directory = '/Users/haribo/Downloads/AWS_POLLY/mp3_flie'
file_path = save_speech(response, directory)

print(f"Saved speech to {file_path}")
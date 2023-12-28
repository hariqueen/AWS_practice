import os

__all__ = ["synthesize_speech", "save_speech"]

def synthesize_speech(polly_client, text, voice_id='Danielle', engine='long-form', output_format='mp3'):
    return polly_client.synthesize_speech(VoiceId=voice_id,
                                          Engine=engine,
                                          OutputFormat=output_format, 
                                          Text=text)

def save_speech(response, directory, prefix='speech'):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.startswith(prefix)]
    next_number = len(files) + 1
    file_path = os.path.join(directory, f'{prefix}{next_number}.mp3')
    
    with open(file_path, 'wb') as file:
        file.write(response['AudioStream'].read())
    return file_path

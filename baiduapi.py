from aip import AipSpeech

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

""" 你的 APPID AK SK """
APP_ID = '21218655'
API_KEY = 'RRETI8P3qecuvzkNzsDGt2Xh'
SECRET_KEY = 'ykFapYnECRvgla6fxajmHMXHBbwjGPCi'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

print(
    client.asr(get_file_content('D:\\work\\voiceparser\\python\\1594280264770.m4a'), 'm4a', 16000, {
    'dev_pid': 1537,
})
)

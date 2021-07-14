import re

def modifyScripts():
    r = open('example.txt', 'r+', encoding='UTF-8')    # 원본 파일 읽어오기
    w = open('example_raw.txt', 'a+', encoding='UTF-8')    # 전처리 된 raw 파일 생성

    while True:
        line = r.readline()
        if not line: break

        if '"' in line:  # '"' 제거
            print('before : ' + line)
            line = line.replace('"', '')
            print('after : ' + line)

        if '#' in line:  # '#' 제거
            line = line.replace('#', '')

        if '- ' in line:  # '- ' 제거
            line = line.replace('- ', '')

        if '!' in line:  # '!' -> '.'
            line = line.replace('!', '.')

        if '&' in line:  # '&' -> 'and'
            line = line.replace('&', 'and')

        if 'um...' in line:  # 'um...' -> 'um.'
            line = line.replace('um...', 'um.')

        if 'Um...' in line:  # 'Um...' -> 'Um.'
            line = line.replace('Um...', 'Um.')

        if 'so...' in line:  # 'so...' -> 'so.'
            line = line.replace('so...', 'so.')

        if 'uh...' in line:  # 'uh...' -> 'uh.'
            line = line.replace('uh...', 'uh.')

        if 'a.m.' in line:  # 'a.m.' -> 'am'
            line = line.replace('a.m.', 'am')

        if 'p.m.' in line:  # 'p.m.' -> 'pm'
            line = line.replace('p.m.', 'pm')

        line = re.sub(pattern='\([A-Z].*\)\s', repl='', string=line)
        line = re.sub(pattern='\[[A-Z].*\]\s', repl='', string=line)
        line = re.sub(pattern='^♪\s[A-Z].*', repl='', string=line)

        w.write(line)

    r.close()
    w.close()

def attachTag() :
    r = open('example_raw.txt', 'r+', encoding='UTF-8')  # raw 파일 읽어오기
    w = open('example_tag.txt', 'a+', encoding='UTF-8')  # tag가 부착된 tag 파일 생성

    while True:
        line = r.readline()
        if not line: break

        line = re.sub(pattern='\s', repl='\tO\n', string=line)
        line = re.sub(pattern='^	O', repl='', string=line)
        line = re.sub(pattern='\,\tO', repl='\tCOMMA', string=line)
        line = re.sub(pattern='\.\tO', repl='\tPERIOD', string=line)
        line = re.sub(pattern='\?\tO', repl="\tQUESTION", string=line)
        line = re.sub(pattern="'s\tO", repl="\tO\n's\tO", string=line)
        line = re.sub(pattern="'re\tO", repl="\tO\n're\tO", string=line)
        line = re.sub(pattern="'m\tO", repl="\tO\n'm\tO", string=line)
        line = re.sub(pattern="'m\tO", repl="\tO\n'm\tO", string=line)
        line = re.sub(pattern="'ll\tO", repl="\tO\n'll\tO", string=line)
        line = re.sub(pattern="n't\tO", repl="\tO\nn't\tO", string=line)

        w.write(line)


    r.close()
    w.close()
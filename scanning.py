import re
import shlex
from maltiverse import Maltiverse

parol="1939njfjslxnbn2"
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY


class Parser:
    IP = 0

    def parse_line(self, line):
        try:
            line = re.sub(r"[\[\]]", "", line)
            data = shlex.split(line)
            result = f'{data[self.IP]}'
            return result
        except Exception as e:
            raise e

if __name__ == '__main__':
    parser = Parser()
    LOG_FILE = 'Laba_1/career_nginx_all.log'
    count = 0
    log_entries = set()
    try:
        with open(LOG_FILE, "r") as f:
            i = 0
            for line in f:
                if i >= 40:
                    break
                log_entries.add(parser.parse_line(line))
                i += 1

        api = Maltiverse(auth_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjIzMjY0MjcwNjYsImlhdCI6MTY5NTcwNzA2Niwic3ViIjoxNjg1OCwidXNlcm5hbWUiOiJNeWtoYWlsb19Uc2ViYWsiLCJhZG1pbiI6ZmFsc2UsInRlYW1faWQiOjI3OSwidGVhbV9uYW1lIjoibHBudSIsInRlYW1fbGVhZGVyIjpmYWxzZSwidGVhbV9yZXNlYXJjaGVyIjpmYWxzZSwidGVhbV9pbmRleCI6ImlvYy1scG51LWI3MTk2NDk2LTUxYTItMTFlZS1iOWQwLTAyNDJhYzEyMDAwNyIsImFwaV9saW1pdCI6MjUwMDB9.xRbM0v_O0irDLFvYwP2Y4P87zIEdT9sFM0nmbEsMsYE")
        for ip in log_entries:
            result = api.ip_get(ip)
            if "ip_addr" in result:
                print(f"{result['ip_addr']} - {result['classification']}") 
            else:
                print(f"{ip} - No Info")
    except:
        print("An error has occured")
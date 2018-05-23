import requests




se = requests.session()

class login(object):

    def login_222zhe(user,password):
        headers ={
            'referer':'https://www.222zhe.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.222zhe.com%2Fwp-admin%2F&reauth=1',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'cookie':'Hm_lvt_1ff5481335fbc6ef1042680ebf392fa5=1525849859,1525959816; wordpress_test_cookie=WP+Cookie+check',
        }

        data = {
            'log':user,
            'pwd':password,
            'rememberme':'forever',
            'wp-submit':'登录',
            'redirect_to':'https://www.222zhe.com/wp-admin/',
            'testcookie':'1',
        }

        Reads = se.post("https://www.222zhe.com/wp-login.php",data=data,headers=headers,allow_redirects=True).text
        if '仪表盘' in Reads:
            print('登录成功')
            return se.cookies




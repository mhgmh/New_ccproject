import requests
se = requests.session()
import re
from pyquery import PyQuery as pq
import lxml
import  time
import requests
import time
import json
import random


se = requests.session()
class articles(object):

    def Pub_article(url):
        tag = ''
        user_agent = articles.user_agent(url)
        time.sleep(10)
        headers = {
            'authority': 'm.toutiao.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'UM_distinctid=16352d801092ac-0eb0a388034e86-33657f07-1fa400-16352d8010afee; tt_webid=6554563661830604302; uuid="w:a904362acac346dbb2b84c78fd6a868f"; sso_login_status=0; _ga=GA1.2.1416607795.1526551943; __utma=24953151.1416607795.1526551943.1526553949.1526553949.1; __utmz=24953151.1526553949.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gid=GA1.2.1927624416.1526711605; __tasessionId=ocugf0p0c1526714508060',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent,
        }
        urls = str(url).replace('//www','//m').replace('/a','/group/')
        ip = requests.get('http://165704599489980799.dev.checkerproxy.org/?num=1&area_type=1&level=2').text
        proxies = {"http": ip}
        print("Pub_article:"+str(proxies))
        html = requests.get(urls, headers=headers, allow_redirects=False,proxies=proxies)
        head = str(html.headers)
        if 'location' in head:
            urll = html.headers['location'] + "info/"
            if 'www.' not in urll:
                print("当前可执行连接为:" + urll)  # 若成功，即可返回执行连接地址......
                if 'm.toutiao' in urll:   #判断链接地址是否是正常的提取连接
                    se.headers.clear()
                    se.headers.update(headers)
                    se.proxies = proxies
                    alltxt = se.get(urll,proxies=proxies).text
                    # respon = se.get('http://2018.ip138.com/ic.asp').text
                    # print(respon)
                    f = json.loads(alltxt)
                    if '视频加载中' in str(f):
                        print('视频连接')
                        return '错误信息'
                    else:
                        try:
                            content = f['data']['content'] #获取到m页面的content内容。
                            title = f['data']['title']     #获取到m页面的title 信息
                            headers = {
                                'authority': 'www.toutiao.com',
                                'method': 'GET',
                                'path': '/a6288525231876096257/',
                                'scheme': 'https',
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'zh-CN,zh;q=0.9',
                                'cache-control': 'max-age=0',
                                'cookie': 'tt_webid=6554563661830604302; tt_webid=6554563661830604302; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16352d801092ac-0eb0a388034e86-33657f07-1fa400-16352d8010afee; tt_webid=6554563661830604302; uuid="w:a904362acac346dbb2b84c78fd6a868f"; sso_login_status=0; _ga=GA1.2.1416607795.1526551943; __utma=24953151.1416607795.1526551943.1526553949.1526553949.1; __utmz=24953151.1526553949.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gid=GA1.2.1927624416.1526711605; CNZZDATA1259612802=102088705-1526101527-%7C1526713008; __tasessionId=jvjx1667x1526717882212',
                                'upgrade-insecure-requests': '1',
                                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
                            }




                            se.headers.clear()
                            se.headers.update(headers)
                            se.proxies = proxies

                            Read = se.get(url,proxies=proxies).text
                        except KeyError:
                            return '错误信息'
                        if 'tagInfo' in Read:  #判断是否有标签存在。
                            tag1 = 'tagInfo: {'
                            tag2 = 'groupId:'
                            allred = re.compile(tag1+"(.*?)"+tag2,re.S).findall(Read)[0]
                            tags = re.compile('{"name":"(.*?)"}').findall(re.compile('tags:(.*?)],').findall(allred)[0] + "]")
                            if len(tags) == 0:
                                tag = ''
                            elif len(tags) > 3:
                                for i in range(0,3):
                                    tag += tags[i] + "、"
                            else :
                                if len(tags) <= 3 and len(tags) != 0:
                                    for l in tags:
                                        tag += l + "、"
                        else:
                            tag = ""
                        se.close()
                        print(title,content,tag)
                        return title,content,tag
                else:
                    se.close()
                    return  '错误信息'
            se.close()
            return '错误信息'
        else:
            se.close()
            return '错误信息'

    def Blog_article(name,title,content,tags):
        if name == '哈士奇' or name == '拉布拉多' or name == '萨摩耶' or name == '巴哥' or name == '汪星人' or name == '金毛' or name == '秋田犬' or name == '中华田园犬' \
                or name == '比熊' or name == '藏獒' or name == '松狮' or name == '泰迪'or name == '二哈' or name == '宠物' or name == '柴犬' or name == '德牧' or name == '流浪狗' \
                or name == '茶杯犬' or name == '博美' or name == '法斗' or name == '牛头梗' or name == '比格猎犬' or name == '雪纳瑞' or name == '高加索' or name == '流浪狗':
            fid = '2'
        elif name == '暹罗猫' or name =='龙猫' or name =='喵星人' or name =='流浪猫' or name =='布偶猫' or name =='折耳猫' or name =='加菲猫' or name =='英国短尾猫' or name =='波斯猫' \
                or name == '短毛猫'  or name =='英短' or name =='美短':

            fid = '1'

        else :
            return  "暂无分类"

        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://www.222zhe.com/wp-admin/edit.php?ids=1898',
            'cookie': 'wordpress_sec_284f142291139beef380432d2e4ec353=222zhe%7C1527565355%7CBgmz7FFfJboOsHgYAQBynuaWIf850B5iv2lxV5wlH0a%7C3c9731bb715f3db07242055314f459c50f0c21ddb6bada037b2d2852a5170a73; wordpress_logged_in_284f142291139beef380432d2e4ec353=222zhe%7C1527565355%7CBgmz7FFfJboOsHgYAQBynuaWIf850B5iv2lxV5wlH0a%7Ce1818a306f5653cd4eead92a605a71f2a02dad59ed5e92aa942516401860cd6a; Hm_lvt_1ff5481335fbc6ef1042680ebf392fa5=1526355800,1526550876,1526704447,1526888652; wp-settings-1=posts_list_mode%3Dlist%26mfold%3Do%26libraryContent%3Dbrowse%26editor%3Dtinymce%26hidetb%3D1; wp-settings-time-1=1527059299'
        }
        ip = requests.get('http://165704599489980799.dev.checkerproxy.org/?num=1&area_type=1&level=2').text
        proxies = {"http": ip}
        se.proxies = proxies
        se.headers.clear()
        se.headers.update(headers)
        string = se.get("https://www.222zhe.com/wp-admin/post-new.php").text
        ponce = re.compile('name="_wpnonce" value="(.*?)" />').findall(str(string))[0]
        postid = re.compile("id='post_ID' name='post_ID' value='(.*?)' />",re.S).findall(str(string))[0]
        meta = re.compile('name="meta-box-order-nonce" value="(.*?)" />',re.S).findall(string)[0]
        close = re.compile('name="closedpostboxesnonce" value="(.*?)" />',re.S).findall(string)[0]
        samp = re.compile('name="samplepermalinknonce" value="(.*?)" />',re.S).findall(string)[0]
        _ajax_nonce = re.compile('name="_ajax_nonce-add-category" value="(.*?)" />',re.S).findall(str(string))[0]
        my_custom = re.compile('name="my-custom-fields_wpnonce" value="(.*?)" />',re.S).findall(str(string))[0]
        _ajax_meta = re.compile('name="_ajax_nonce-add-meta" value="(.*?)" />',re.S).findall(str(string))[0]
        times = list(time.localtime(time.time()))

        data = {
            '_wpnonce': ponce,
            '_wp_http_referer': '/wp-admin/post-new.php',
            'user_ID': '1',
            'action': 'editpost',
            'originalaction': 'editpost',
            'post_author': '1',
            'post_type': 'post',
            'original_post_status': 'auto-draft',
            'referredby': 'https://www.222zhe.com/wp-admin/',
            '_wp_original_http_referer': 'https://www.222zhe.com/wp-admin/',
            'auto_draft': '',
            'post_ID': postid,
            'meta-box-order-nonce': meta,
            'closedpostboxesnonce': close,
            'post_title': title,
            'samplepermalinknonce': samp,
            'content': content,
            'wp-preview': '',
            'hidden_post_status': 'draft',
            'post_status': 'draft',
            'hidden_post_password': '',
            'hidden_post_visibility': 'public',
            'visibility': 'public',
            'post_password': '',
            'aa': times[0],
            'mm': times[1],
            'jj': times[2],
            'hh': times[3],
            'mn': times[4],
            'ss': times[5],
            'hidden_mm': times[1],
            'cur_mm': times[1],
            'hidden_jj': times[2],
            'cur_jj': times[3],
            'hidden_aa': times[0],
            'cur_aa': times[0],
            'hidden_hh': '16',
            'cur_hh': '16',
            'hidden_mn': '31',
            'cur_mn': '31',
            'original_publish': '发布',
            'publish': '发布',
            'post_category[]': '0',
            'post_category[]': fid,
            'newcategory': '新分类目录名',
            'newcategory_parent': '-1',
            '_ajax_nonce-add-category': _ajax_nonce,
            'tax_input[post_tag]': tags,
            'newtag[post_tag]': '',
            '_thumbnail_id': '-1',
            'my-custom-fields_wpnonce': my_custom,
            'git_thumb': '',
            'git_zhuanzai_name': '',
            'git_zhuanzai_link': '',
            'git_download_name': '',
            'git_download_size': '',
            'git_download_link': '',
            'git_demo': '',
            'excerpt': '',
            'trackback_url': '',
            'metakeyselect': '#NONE#',
            'metakeyinput': '',
            'metavalue': '',
            '_ajax_nonce-add-meta': _ajax_meta,
            'advanced_view': '1',
            'comment_status': 'open',
            'ping_status': 'open',
            'post_name': '',
            'post_author_override': '1',
        }
        se.headers.clear()
        se.headers.update(headers)
        respon = se.post("https://www.222zhe.com/wp-admin/post.php",data=data,allow_redirects=False,verify=False).text
        respon_x = se.get('https://www.222zhe.com/wp-admin/edit.php?post_status=publish&post_type=post',verify=False).text
        class_one = '<span class={this}view{this}><a href="(.*?)" rel="bookmark" aria-label="查看“{}”">查看</a>'.replace("{this}","'").format(title)
        try:
            article_url = re.compile(class_one,re.S).findall(respon_x)[0]
            print(article_url)
            bd_url = 'http://data.zz.baidu.com/urls?site=https://www.222zhe.com&token=yIZ5kYk4fSeNRTfe'
            readtxt = requests.post(bd_url,data=article_url).text
            print(readtxt)
        except IndexError:
            print("暂时未获取到成功后的链接")

    def user_agent(self):
        ua = open('ua.txt').read()
        ualist = ua.rsplit("\n")
        sjs = len(ualist)
        randoms = random.randint(2,sjs-1)
        print(randoms)
        return ualist[randoms]


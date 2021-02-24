import random
import re
import urllib.request

# 用户代理池
uapools=[
     'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
     ]

# 随机选择请求头的User-Agent
def ua(uapools):
     thisua=random.choice(uapools)
     print(thisua)
     headers=("User-Agent",thisua)
     openner=urllib.request.build_opener()
     openner.addheaders=[headers]
     urllib.request.install_opener(openner)

# 获取当前页面
def getCurrentPage(cursor,number):
    url = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + str(cursor)+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=" + str(number)
    return urllib.request.urlopen(url).read().decode("utf-8")

# 获取下一个cursor
def getNextCursor(html):
    pat = '"last":"(.*?)",'
    return re.compile(pat,re.S).findall(html)[0]

# 获取下一个number
def getNextNumber(number):
    return number + 1

# 获取当前页面中的评论
def getCurrentPageComments(html):
    pat = '"content":"(.*?)"'
    return re.compile(pat,re.S).findall(html)

# 保存到文件中
def save(commentList):
    with open("comments.txt","a",encoding="utf-8") as f:
        for item in commentList:
            f.write(item + "\n")

def main():
    cursor = 0
    number = 1613881359521
    totalCommentsNumber = 12696
    totalPage = totalCommentsNumber // 10
    commentList = []    # 存放所有评论的列表
    for i in range(0,totalPage):
        ua(uapools)
        print("cursor:" + str(cursor) + "   number:" + str(number))
        html = getCurrentPage(cursor,number)
        cursor = getNextCursor(html)
        number = getNextNumber(number)
        commentList += getCurrentPageComments(html)
    save(commentList)
main()

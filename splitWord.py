import jieba
import json


# 获取停用词
def getStopWords():
    stopWords = []
    with open("baidu_stopwords.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            stopWords.append(line.strip())
    return stopWords


# 删除分词后的停用词
def delStopWords(stopWords, words):
    lists = []
    for word in words:
        if word not in stopWords:
            lists.append(word)
    return lists


# 转成echarts需要的格式
def format(words):
    counts = {}
    formatStr = []
    temp = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for name, value in items:
        if value > 50:
            temp["name"] = name
            temp["value"] = value
            formatStr.append(temp)
            temp = {}
    return formatStr


# 保存分词后的json文件
def save(fotmatList):
    jsonStr = json.dumps(fotmatList, indent=4)
    with open("word.json", "w", encoding="utf-8") as f:
        f.write(jsonStr)


# 分词
def splitWord():
    data = open("comments.txt", "r", encoding="utf-8").read()
    words = jieba.lcut(data)
    return words


def main():
    stopWords = getStopWords()
    words = splitWord()
    # print(len(words))
    words = delStopWords(stopWords, words)
    # print(len(words))
    fotmatList = format(words)
    # print(fotmatStr)
    save(fotmatList)


main()

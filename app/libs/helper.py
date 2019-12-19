_date_ = "2019/1/17 8:24"
_author_ = "xing"


def list_to_jsonlist(list_obj):
    """
    因为序列化很麻烦 所以必须查询出来一个对象的list 先传进来 然后挨个转换为dict 返回一个 字典的list 才可以序列化呢
    :param list_obj:
    :return:
    """
    json_list = []
    for each_item in list_obj:
        json_list.append(dict(each_item))
    return json_list

def is_isbn_or_key(word):
    """
    判断是关键字还是isbn搜索
    :param word:
    :return:
    """
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "isbn"
    short_word = word.replace("-", "")
    if "-" in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = "isbn"

    return isbn_or_key
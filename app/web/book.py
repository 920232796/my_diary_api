import random

from flask import jsonify, request, render_template, flash
import json

from app.models.response_result import ResponseResult

from flask import request
_date_ = "2019/1/18 14:59"
_author_ = "xing"

#引入web
from app.web import web
from app.models.book import Book
from app.models.book import db
from app.models.book_collection import BookCollection
from app.libs.helper import  list_to_jsonlist
import os
import uuid

@web.route("/api/book/getAllBookCollection")
def getAllBookCollection():
    """"""
    response_result = ResponseResult()
    book_collection = BookCollection().query.all()
    print(type(book_collection))
    json_list = list_to_jsonlist(book_collection)

    response_result.arrays = json_list

    return json.dumps(response_result, default=lambda o:o.__dict__)

@web.route("/api/book/getBook")
def getBook():
    """"""
    response_result = ResponseResult()
    book_collection_name = request.args.get("book_collection_name")
    book_collection = BookCollection().query.filter_by(name=book_collection_name).first()
    books = Book().query.filter_by(book_collection_id=book_collection.id).all()
    books = list_to_jsonlist(books)
    response_result.arrays = books
    # book_collection_id = book_collection.id
    #
    # book_book_collection = BookBookCollection().query.filter_by(book_collection_id=book_collection_id)
    # book_list = []
    #
    # for each_item in book_book_collection:
    #     book_id = each_item.book_id
    #     book = Book().query.filter_by(id=book_id).first()
    #     book_list.append(book)
    #
    # book_list = list_to_jsonlist(book_list)
    #
    # response_result.arrays = book_list
    return json.dumps(response_result, default=lambda o: o.__dict__)


@web.route("/api/book/submitBook")
def submitBook():
    """"""
    response_result = ResponseResult()
    book_id = request.args.get("editBookId")
    book_content = request.args.get("editContent")
    print(book_id)
    print(book_content)
    if (book_id != "-1"):
        try:
            edit_book = Book().query.filter_by(id=book_id).first()
            edit_book.content = book_content
            db.session.commit()
            response_result.message = "提交成功"
        except Exception as e:
            print(e)
            response_result.ret = "fail"
            response_result.message = "提交失败"
    else:
        response_result.ret = "fail"
        response_result.message = "还没有选中笔记呢！"
    return json.dumps(response_result, default=lambda o: o.__dict__)



@web.route("/api/book/addBookCollection")
def addBookCollectionSubmit():
    """"""
    response_result = ResponseResult()
    book_collection_name = request.args.get("submitBookCollectionName")
    book_collection = BookCollection()
    try:
        book_collection.name = book_collection_name
        db.session.add(book_collection)
        db.session.commit()
        response_result.message = "添加成功"
    except:
        response_result.ret = "fail"

    return json.dumps(response_result, default=lambda o: o.__dict__)

@web.route("/api/book/addBook")
def addBook():
    """"""
    response_result = ResponseResult()
    book_collection_name = request.args.get("currentBookCollectionName")
    book_content = request.args.get("bookContent")

    book_collection = BookCollection().query.filter_by(name=book_collection_name).first()
    book_collection_id = book_collection.id

    book = Book()
    book.book_collection_id = book_collection_id
    book.content = book_content
    db.session.add(book)
    db.session.commit()

    return json.dumps(response_result, default=lambda o: o.__dict__)

@web.route("/api/book/imageUpload",methods=["POST"])
def image_upload():
    """"""
    # file_dir = "d://python"
    file_dir = "/usr/image"
    # file_dir = "./image"
    f = request.files["image"]
    fname = f.filename
    ext = fname.rsplit(".", 1)[1]
    print(ext)
    if (ext != "png" and ext != "jpg" and ext!="jpeg"):
        print("error")
        return "hello world"
    else:
        # print("hello")
        fname = str(uuid.uuid1()) + "." + ext
        f.save(os.path.join(file_dir, fname))
    # print({"url":"http://zhxing.online/image/" + fname})
    return jsonify({"url":"http://www.zhxing.online/image/" + fname})



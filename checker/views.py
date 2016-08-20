from django.shortcuts import render
import MySQLdb
import pymongo


class Tester(object):

    @classmethod
    def mysql(cls, endpoint):
        try:
            MySQLdb.connect(endpoint, "admin1", "test", "test", connect_timeout=2)
            return True
        except Exception as e:
            if e[0] == 1045:  # password error
                return True
            return False

    @classmethod
    def mongodb(cls, endpoint):
        try:
            result = pymongo.MongoClient(host=endpoint,
                                         serverSelectionTimeoutMS=1000)
            result.server_info()
            return True
        except:
            return False


def index(request):
    test_types = [
        {"name": "mysql", "result": ""},
        {"name": "mongodb", "result": ""},
    ]
    if request.method == "POST":
        for test_type in test_types:
            endpoint = request.POST.get(test_type["name"], None)
            if hasattr(Tester, test_type["name"]):
                if endpoint:
                    test_type["result"] = getattr(Tester, test_type["name"])(endpoint)

        return render(request, "checker/index.html",
                                  dict(test_types=test_types))
    else:
        return render(request, "checker/index.html",
                                  dict(test_types=test_types))

from flask import Flask, Request, request, json

app = Flask(__name__)

class Person:
    def __init__(self):
        self.firstName = ""
        self.lastName  = ""
        self.age       = 0

    def load(self, json):
        jsonAttr = list(json.keys())
        for attr in vars(self):
            if attr in jsonAttr:
                self.__setattr__(attr, json[attr])

    def __repr__(self):
        return "FirstName = "+self.firstName+" Last Name = "+ self.lastName+ " age = "+str(self.age)


def customdec(function):
    number = 0
    def wrapper(*args, **kwargs):
        nonlocal number
        print("Request #"+str(number))
        return function(*args,**kwargs)
    return wrapper


@app.route("/", methods=['POST'])
@customdec
def hello():
    p  = Person()
    p.load(json.loads(request.data))
    return "Hello, World!"

if __name__ == "__main__":
    app.run(port=8989)
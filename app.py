from flask import Flask, request

app = Flask(__name__)

@app.route("/pyramidWordCheck")
def pyramidWordCheck():
    dictOfChars = dict()
    string = request.args.get('word')
    errorString = string+" is not a pyramid word"
    if string.isalpha() ==False:
        return errorString + " and it is not a word"
    for char in string:
        count = string.count(char)
        if count in dictOfChars.keys() and dictOfChars[count]!=char:
            return errorString
        else:
            dictOfChars[count] = char
    for i in range(len(dictOfChars.values())):
        if i+1 not in dictOfChars.keys():
            return errorString
    return string +" is a pyramid word"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

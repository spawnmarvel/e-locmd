
import codecs
def read_file(fi):
    print("Reading book " + fi + " from file")
    location = "./information/" + fi
    sentences = 0
    words = 0
    msg = ""
    try :
        with codecs.open(location, "r", encoding="utf-8") as f:
            if f.readable():
                cont = f.read().split(".")
                sentences = len(cont)
                # print(cont)
                print(type(cont))
                if len(cont) != 0:
                    for x in range(len(cont)):
                        tmp = cont[x]
                        # print(type(tmp))
                        # print(type(parse_string(tmp)))
                        msg += tmp
                        # need to add back .
                        msg += "."
                # words
                word = msg.split(" ")
                words = len(word)
    except UnicodeEncodeError as uce:
        msg = "There is a strange sign in your text " + fi
    except Exception as ex:
        msg = "helper.py " + format(ex)
    # remove the last . we added
    rm_last =  len(msg)
    msg = msg[:rm_last-1]
    tu = (msg, sentences, words)
    return tu

def parse_string(st):
    st = st.encode("utf-8", "replace")
    return st


import sys
import alp
from alp.item import Item as I

def build_line(words,start=1):
    """Returns a line made of the concatenation of all words
    starting from start
    words: list of words
    start: list index to start concatenation"""
    line = ''
    for word in words[start:]:
        if len(line)==0:
            line = word
        else:
            line = line + ' ' + word
    return line

def main():
    q = sys.argv

    # Load todos from file
    todo_file = q.pop(1) # Path to todo.txt file
    f = open(todo_file,'r')
    todos = f.readlines()
    f.close()

    feedback = []
    line = ''

    # Build command line.
    line = build_line(q,1)
    addItem = I(title="Add Todo", subtitle=line, arg=u"add {0}".format(line), valid=True)

    if len(q)==1:
        if len(todos):
            for r in todos:
                feedback.append(I(title=format(todos.index(r)+1)+':'+r, subtitle="Mark as Done", arg=u"do {0}".format(todos.index(r)+1), valid=True))
        else:
            feedback.append(addItem)
    elif len(q)==2:
        if q[1] in ['archive','deduplicate']:
            # Leave other specific actions unaltered by the program.
            feedback.append(I(title="Parse to todo.sh", subtitle="Other Actions", arg=u"-f {0}".format(line), valid=True))
        feedback.append(addItem)
        if len(todos):
            t = alp.fuzzy_search(line, todos, key=lambda x: x)
            for r in t:
                feedback.append(I(title=format(todos.index(r)+1)+':'+r, subtitle="Mark as Done", arg=u"do {0}".format(todos.index(r)+1), valid=True))
    else:
        if q[1] in ['a','add','ls','list']: # Ignore these key words.
            line = build_line(q,2)
            addItem = I(title="Add Todo", subtitle=line, arg=u"add {0}".format(line), valid=True)
        if q[1] in ['addm','addto','append','app','pri','p','del','rm','depri','dp','do']:
            # Leave other specific actions unaltered by the program.
            feedback.append(I(title="Parse to todo.sh", subtitle="Other Actions", arg=u"-f {0}".format(line), valid=True))
            feedback.append(addItem)
        else:
            feedback.append(addItem)
            t = alp.fuzzy_search(line, todos, key=lambda x: x)
            for r in t:
                feedback.append(I(title=format(todos.index(r)+1)+':'+r, subtitle="Mark as Done", arg=u"do {0}".format(todos.index(r)+1), valid=True))

    alp.feedback(feedback)

if __name__ == "__main__":
    main()

import tkinter as tk
from nltk import tokenize
from nltk import tag
from nltk import chunk


root = tk.Tk()
root.title("Tokenizer App")
root.geometry('450x450')

myvar = tk.StringVar()
myvar2 = tk.StringVar()

#   Hello. My name is Anthony. Today you'll be learning NLTK. In Düsseldorf I took my hat off. But I can't put it back on.#

def mywarWritten(*args):
    #print (myvar.get())
    sents = tokenize.sent_tokenize(myvar.get())
    print (len(sents)) 
    
    sent = tokenize.word_tokenize(sents[0])
    tagged_sent = tag.pos_tag(sent)
    print(tagged_sent)
    JJ_count = 0
    NN_count = 0

    for tweet in tagged_sent:
       for pair in tweet:
        tag1 = pair[1]
        if tag1 == 'JJ':
            JJ_count += 1
        elif tag1 == 'NN':
            NN_count += 1
    print('Total number of adjectives = ', JJ_count)
    print('Total number of nouns = ', NN_count)
    
    tree = chunk.ne_chunk(tagged_sent)
    tree.draw()


      
def mywarWritten2(*args):
     
    
      sents = tokenize.sent_tokenize(myvar.get())
   
      sent = tokenize.word_tokenize(sents[int(myvar2.get())])
      tagged_sent = tag.pos_tag(sent)
      print(tagged_sent)
      JJ_count = 0
      NN_count = 0

      for tweet in tagged_sent:
       for pair in tweet:
        tag1 = pair[1]
        if tag1 == 'JJ':
            JJ_count += 1
        elif tag1 == 'NN':
            NN_count += 1
      print('Total number of adjectives = ', JJ_count)
      print('Total number of nouns = ', NN_count)
      tree = chunk.ne_chunk(tagged_sent)
      tree.draw()
       





text_entry = tk.Entry(root, textvariable=myvar ,width=2000)
button1 = tk.Button(root, text="Tokenizer", command=mywarWritten ) 
button1.pack()
button2 = tk.Button(root, text="Next sent", command=mywarWritten2) 
button2.pack()
text_entry2 = tk.Entry(root, textvariable=myvar2 ,width=20  )
text_entry.pack()
text_entry2.pack()


root.mainloop()



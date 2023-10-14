import os
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader




# def file_to_data(file_paths):
#     data = []
#     for file_path in file_paths:
#         loader = PyPDFLoader(file_path)
#         data  += loader.load() 
#     return data
chat_history = []

def split_data(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
    all_splits = text_splitter.split_text(data)
    vectorstore = Chroma.from_texts(all_splits, embedding=OpenAIEmbeddings())
    return vectorstore

def anser_question(question, data):
    prompt = hub.pull("rlm/rag-prompt")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    # data = file_to_data(files)
    vectorstore = split_data(data)
    similarity_search = vectorstore.similarity_search(question, 4)
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectorstore.as_retriever(),
        # chain_type_kwargs={"prompt": question}
    )
    result = qa_chain({"query": question, "chat_history": chat_history})
    chat_history.append((question, result['result']))
    return result['result']
    # return docs[0:10]


# file_path_1 = "/Users/aryanverma/Desktop/HACKGT_PROJECT/cs.pdf"
# file_path_2 = "/Users/aryanverma/Desktop/HACKGT_PROJECT/cs2.pdf"
# file_paths = [file_path_1,file_path_2]
data = ['Arrays and Array List\nArrays and Array Lists\nSaikrishna Arcot\nM. Hudachek-Buswell\nJuly 18, 2020\n1Arrays and Array List\nArray Deﬁnition\n•Anarrayis a sequenced collection of variables all of the same\ntype. Every cellin an array has an indexdenoting its location\nwithin the array. The index uniquely refers to the value stored\nin that cell. The cells of an array, A, are numbered (or\nindexed) beginning with 0, 1, 2, and so on.•Each value stored in an array is often called an element of\nthat array.\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n2Arrays and Array List\nArray Deﬁnition\n•Anarrayis a sequenced collection of variables all of the same\ntype. Every cellin an array has an indexdenoting its location\nwithin the array. The index uniquely refers to the value stored\nin that cell. The cells of an array, A, are numbered (or\nindexed) beginning with 0, 1, 2, and so on.\n•Each value stored in an array is often called an element of\nthat array.\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n2Arrays and Array List\nArray Length and Capacity\n•Since the length of an array determines the maximum number\nof items that can be stored in the array, we refer to the length\nof an array as its capacity.The length of an array is\nestablished when the array is created, and the length is ﬁxed.•In Java, the length of an array named acan be accessed\nusing the syntax a.length . Thus, the cells of an array, a, are\nnumbered 0, 1, 2, and so on, up through a.length-1 , and\nthe cell with index kcan be accessed with syntax a[k].\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n3Arrays and Array List\nArray Length and Capacity\n•Since the length of an array determines the maximum number\nof items that can be stored in the array, we refer to the length\nof an array as its capacity.The length of an array is\nestablished when the array is created, and the length is ﬁxed.\n•In Java, the length of an array named acan be accessed\nusing the syntax a.length . Thus, the cells of an array, a, are\nnumbered 0, 1, 2, and so on, up through a.length-1 , and\nthe cell with index kcan be accessed with syntax a[k].\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n3Arrays and Array List\nArray Creation\n•There are a couple of ways to declare an array. One can use\nan array literal or an array declaration. The element type for\nthe array is any Java base type or class type.•Given a capacity of N = 4,\nArray literal: int[] myArray = {1, 3, 3, 2}\nArray declaration: int[] myArray = new int[4]\n4Arrays and Array List\nArray Creation\n•There are a couple of ways to declare an array. One can use\nan array literal or an array declaration. The element type for\nthe array is any Java base type or class type.\n•Given a capacity of N = 4,\nArray literal: int[] myArray = {1, 3, 3, 2}\nArray declaration: int[] myArray = new int[4]\n4Arrays and Array List\nArrays of Character or Object References\n•An array can store primitive elements, such as characters.\nS\n0\nA\n1\nM\n2\nP\n3\nL\n4\nE\n5•An array can also store references to objects.\n"Rene"\n "Joseph"\n "Janet"\n "Jonas"\n "Helen"\n0\n1\n2\n3\n4\n5Arrays and Array List\nArrays of Character or Object References\n•An array can store primitive elements, such as characters.\nS\n0\nA\n1\nM\n2\nP\n3\nL\n4\nE\n5\n•An array can also store references to objects.\n"Rene"\n "Joseph"\n "Janet"\n "Jonas"\n "Helen"\n0\n1\n2\n3\n4\n5Arrays and Array List\nArray Lists\n•An array can be used as a backing structure for a list. In\nessence, array lists store objects and not primitive data types.\nWhereas, arrays can store both, primitives and objects.•When an array list is full, it dynamically resizes to a larger\narray list. Typically, a new, larger backing array is created and\nthe content is copied from the old array to the new array.\n•The resizing policy depends on the implementation. Java’s\nimplementation resizes the backing array to 1.5 times the\noriginal size.\n6Arrays and Array List\nArray Lists\n•An array can be used as a backing structure for a list. In\nessence, array lists store objects and not primitive data types.\nWhereas, arrays can store both, primitives and objects.\n', 'rrays and Array List\nArrays of Character or Object References\n•An array can store primitive elements, such as characters.\nS\n0\nA\n1\nM\n2\nP\n3\nL\n4\nE\n5\n•An array can also store references to objects.\n"Rene"\n "Joseph"\n "Janet"\n "Jonas"\n "Helen"\n0\n1\n2\n3\n4\n5Arrays and Array List\nArray Lists\n•An array can be used as a backing structure for a list. In\nessence, array lists store objects and not primitive data types.\nWhereas, arrays can store both, primitives and objects.•When an array list is full, it dynamically resizes to a larger\narray list. Typically, a new, larger backing array is created and\nthe content is copied from the old array to the new array.\n•The resizing policy depends on the implementation. Java’s\nimplementation resizes the backing array to 1.5 times the\noriginal size.\n6Arrays and Array List\nArray Lists\n•An array can be used as a backing structure for a list. In\nessence, array lists store objects and not primitive data types.\nWhereas, arrays can store both, primitives and objects.\n•When an array list is full, it dynamically resizes to a larger\narray list. Typically, a new, larger backing array is created and\nthe content is copied from the old array to the new array.•The resizing policy depends on the implementation. Java’s\nimplementation resizes the backing array to 1.5 times the\noriginal size.\n6Arrays and Array List\nArray Lists\n•An array can be used as a backing structure for a list. In\nessence, array lists store objects and not primitive data types.\nWhereas, arrays can store both, primitives and objects.\n•When an array list is full, it dynamically resizes to a larger\narray list. Typically, a new, larger backing array is created and\nthe content is copied from the old array to the new array.\n•The resizing policy depends on the implementation. Java’s\nimplementation resizes the backing array to 1.5 times the\noriginal size.\n6Arrays and Array List\nAdding an Entry\n•To add an entry einto array myArray at index i, we need to\nmake room for it by shifting forward the n−ientries\nmyArray[i], ..., myArray[n - 1] .\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\nIn this example, the capacity of myArray is 16 and size of\nmyArray is n = 10. So adding at i = 6, shifts myArray\nelements 6-9 to elements 7-10.\n7Arrays and Array List\nAdding an Entry\n•To add an entry einto array myArray at index i, we need to\nmake room for it by shifting forward the n−ientries\nmyArray[i], ..., myArray[n - 1] .\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\nIn this example, the capacity of myArray is 16 and size of\nmyArray is n = 10. So adding at i = 6, shifts myArray\nelements 6-9 to elements 7-10.\n7Arrays and Array List\nAdding an Entry\n•To add an entry einto array myArray at index i, we need to\nmake room for it by shifting forward the n−ientries\nmyArray[i], ..., myArray[n - 1] .\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\nIn this example, the capacity of myArray is 16 and size of\nmyArray is n = 10. So adding at i = 6, shifts myArray\nelements 6-9 to elements 7-10.\n7Arrays and Array List\nAdding an Entry\nprocedure Add(i,e)\nifsize>=arr.lenthen\nRegrow the array\nend if\nforj←size−1,ido\narr[j+1]←arr[j]\nend for\narr[i]←e\nsize←size+1\nend procedure\n8Arrays and Array List\nRemoving an Entry\n•To remove an entry eat index t, we need to ﬁll the hole left\nbyeby shifting backward the n−i−1 elements board[i +\n1], ..., board[n - 1] .\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\nIn this example, the capacity of myArray is 16 and size of\nmyArray is n = 11. So removing at i = 6, shifts myArray\nelements 7-10 to elements 6-9.\n9Arrays and Array List\nRemoving an Entry\n•To remove an entry eat index t, we need to ﬁll the hole left\nbyeby shifting backward the n−i−1 elements board[i +\n1], ..., board[n - 1] .\n0\n1\n2\n3\n4\n5\n6\n7\n8', '\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\nIn this example, the capacity of myArray is 16 and size of\nmyArray is n = 10. So adding at i = 6, shifts myArray\nelements 6-9 to elements 7-10.\n7Arrays and Array List\nAdding an Entry\nprocedure Add(i,e)\nifsize>=arr.lenthen\nRegrow the array\nend if\nforj←size−1,ido\narr[j+1]←arr[j]\nend for\narr[i]←e\nsize←size+1\nend procedure\n8Arrays and Array List\nRemoving an Entry\n•To remove an entry eat index t, we need to ﬁll the hole left\nbyeby shifting backward the n−i−1 elements board[i +\n1], ..., board[n - 1] .\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\nIn this example, the capacity of myArray is 16 and size of\nmyArray is n = 11. So removing at i = 6, shifts myArray\nelements 7-10 to elements 6-9.\n9Arrays and Array List\nRemoving an Entry\n•To remove an entry eat index t, we need to ﬁll the hole left\nbyeby shifting backward the n−i−1 elements board[i +\n1], ..., board[n - 1] .\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\nIn this example, the capacity of myArray is 16 and size of\nmyArray is n = 11. So removing at i = 6, shifts myArray\nelements 7-10 to elements 6-9.\n9Arrays and Array List\nRemoving an Entry\n•To remove an entry eat index t, we need to ﬁll the hole left\nbyeby shifting backward the n−i−1 elements board[i +\n1], ..., board[n - 1] .\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\nIn this example, the capacity of myArray is 16 and size of\nmyArray is n = 11. So removing at i = 6, shifts myArray\nelements 7-10 to elements 6-9.\n9Arrays and Array List\nRemoving an Entry\nprocedure Remove (i)\nitem←arr[i]\narr[i]←NULL\nforj←i,size−2do\narr[j]←arr[j+1]\nend for\nsize←size−1\nreturnitem\nend procedure\n10Arrays and Array List\nArray List Summary and Complexity\n•Array lists are dynamic and store objects.•Accessing elements is a cost of O(1), constant time\n•Inserting, searching or removing from anywhere other than the\nback of the array list is a cost of O(n), linear time\n•Array lists are used in tracking characters in an online game\nmap\n11Arrays and Array List\nArray List Summary and Complexity\n•Array lists are dynamic and store objects.\n•Accessing elements is a cost of O(1), constant time•Inserting, searching or removing from anywhere other than the\nback of the array list is a cost of O(n), linear time\n•Array lists are used in tracking characters in an online game\nmap\n11Arrays and Array List\nArray List Summary and Complexity\n•Array lists are dynamic and store objects.\n•Accessing elements is a cost of O(1), constant time\n•Inserting, searching or removing from anywhere other than the\nback of the array list is a cost of O(n), linear time•Array lists are used in tracking characters in an online game\nmap\n11Arrays and Array List\nArray List Summary and Complexity\n•Array lists are dynamic and store objects.\n•Accessing elements is a cost of O(1), constant time\n•Inserting, searching or removing from anywhere other than the\nback of the arrxay list is a cost of O(n), linear time\n•Array lists are used in tracking characters in an online game\nmap\n11']

question = "give me any date in the information"+"limit answer to 100 words."
print('hey')

if __name__ == '__main__':
    answer = anser_question(question, "".join(data))
    print(answer)

# print(answer)
#list declair
Top10Tools=["python", "R", "Julia", "TensorFlow", "Pytorch" "Jupyter Notebook", "Apache Hadoop", "PapidMiner", "Anaconda", "MATHLAB"]
print(Top10Tools)
fileObj=open("datascience.txt", "w")
for top10 in Top10Tools:
    fileObj.write(top10 +" ")

fileObj.close()



import clusters
blognames,words,data=clusters.readfile('vktrouw_kranten_data.txt')
clust=clusters.hcluster(data)
clusters.drawdendrogram(clust,blognames,jpeg='krantclust_dendrogram.jpg')

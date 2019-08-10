ncdg5 <- read.csv("NDCG5.csv", header = TRUE)
plot(ncdg5$Query,ncdg5$Value,type = "o",col = "red", xlab = "Query Index", ylab = "NCDG5", 
     main = "NCDG5 for CACM Query Set",  ylim=c(0,1))
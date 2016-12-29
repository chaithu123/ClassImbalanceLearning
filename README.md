# ClassImbalanceLearning

The data I took to address this perform is our RAT ANABILGI data. As the data is very small I replicated it several times so that it is compatible to the big data.
So I noticed that the number of samples of majority class=7770 and number of minority class samples are=90.
And as we can see that there is a huge difference in between the number of samples of both minority and majority classes it effects the system even though the accuracy is high as either of the number of false negatives and false positives increases.
That is when the system will not be able to predict the attacks and it classifies attacks as normal samples.
So it is very much important to select the majority class samples which actually represents the essence of all the majority samples and will not lead the classifier to conclusion to reduce the false negative rate.


In the first method I calculated the ratio of the number of samples of majority class to the number of samples of minority class.
 In the data set that I took the ration is  
                                                      ratio=7770/90=86.333
I applied K-means clustering on the majority class samples ,that is on 7770 by taking k as the integer value of ratio that is 86.
As I applied Kmeans I got 86 number of clusters and there is a problem aroused as the number of samples in each cluster are not balanced that is some clusters the number of elements are less the number of minority class samples and if we consider a cluster with less number appended with minority class appended as training set then again the class imbalance problem arise. 


So to address that problem I moved the elements of cluster with less in number when compared to the number of minority samples to other nearest cluster which has more number of sampled when compared to the samples in minority class, that is 90 in our case.
The method that I followed to find the nearest cluster is by sorting the distance of that particular cluster centroid to the centroids of other clusters which has samples more than samples in minority class.
Detailed Block Diagram is available in next slide.

# recommender-system-demo
gonne build on this

Methods will be used in this task:

1. Content-Based recommender system 

Steps:

1. For the target user, we pick two sets of his previous rating records. One set gives his highest rating and the other gives his lowest rating. 

2. For this given user, we extract the tf-idf value from the two items sets that he/she ranks as "like" and “dislike”.

3. Based on the above knowledge we have of this user we build a SVM that can classify the jokes into "like" or "dislike" based on his taste we learn.

4.    Finally, we put the unrated datasets into the SVM we build above to generate recommended jokes for this user marked as “like” or “dislike” to build the recommender system

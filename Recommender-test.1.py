
def main():
    import pandas as pd
    from rake_nltk import Rake
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.feature_extraction.text import CountVectorizer




    df = pd.read_csv('file:///Users/Brian/Desktop/joke.csv',header=None)
    #df = pd.DataFrame(joke,columns=['content'])

    #按格式加column title
    df.columns = ["Content"]
    #加一个column
    df.insert(loc=0, column='idn', value=(np.arange(len(df))))
    df['idn'] = df['idn'].apply(lambda x: "joke " + str(x))
    #确定dataset的格式
    df = df[["idn","Content"]]
    #以idn为index排序jokes
    df.set_index('idn', inplace = True)
    #print(df)



    df['key_words'] = ""

    for index, row in df.iterrows():
        content = row['Content']

        # instantiating Rake, by default is uses english stopwords from NLTK
        # and discard all puntuation characters
        r = Rake()

        # extracting the words by passing the text
        r.extract_keywords_from_text(content)

        # getting the dictionary whith key words and their scores
        key_words_dict_scores = r.get_word_degrees()

        # assigning the key words to the new column
        row['key_words'] = list(key_words_dict_scores.keys())
    # dropping the Plot column
    #df.drop(columns = ['Content'], inplace = True)


    #print (df)
    #创建一个叫key_words_bag的column
    df["key_words_bag"]=" "
    columns = ["key_words"]
    for index, row in df.iterrows():
        words=""
        for col in columns:
            words = words+ ' '.join(row[col])+''
        row ['key_words_bag'] = words
    #df.drop(columns = [col for col in df.columns if col!= 'key_words_bag'], inplace = True)

    # creating a Series for the movie titles so they are associated to an ordered numerical
    # list I will use later to match the indexes

    indices = pd.Series(df.index)

    count = CountVectorizer()

    count_matrix = count.fit_transform(df["key_words_bag"])



    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    #df.reset_index("idn", inplace=True)

    #df.set_index("key_words_bag", inplace=True)

    urchoice = input("choose the number of the joke you like (1-100) ")



    def recommendations(urchoiced, cosine_sim = cosine_sim):

        urchoiced = "joke "+ urchoice

        recommended_movies = []



    # gettin the index of the movie that matches the title
        idx = indices[indices == urchoiced].index[0]

        # creating a Series with the similarity scores in descending order
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

        # getting the indexes of the 10 most similar movies
        top_2_indexes = list(score_series.iloc[1:3].index)

        # populating the list with the titles of the best 2 matching movies
        for i in top_2_indexes:
            recommended_movies.append(list(df.index)[i])

        return recommended_movies

    youwilllike = recommendations(urchoice)



    intro = "You will like:"
    print(intro,youwilllike)
    #jokei =""
    #for i in youwilllike:
    #jokei = "".join(youwilllike)
    #jokei = "\n".join(youwilllike)
    #print(jokei)
    for i in youwilllike:
        print (df.at[i,"Content"])

while True:
        main()
        #if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
            #break




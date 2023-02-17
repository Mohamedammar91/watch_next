# import spacy
import spacy

nlp = spacy.load("en_core_web_md")


def find_similarity():
    # hulk movie with nlp model en_core_web_md
    Planet_Hulk = " Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    hulk = nlp(Planet_Hulk)

    y=1
    # make similarity list and compare all movies with hulk movie
    similarity_list = []
    for i in range(len(movie_list)-1):
        print(hulk.similarity(movie_list[y]))
        similarity_list.append(hulk.similarity(movie_list[y]))
        y+=1

    # put largest similarity in large_similarity
    larger_similarity = 0
    # check similarity list
    print(similarity_list)
    index = 0
    for i in range (len(similarity_list)-1):
        if similarity_list[index] >= similarity_list[index+1]:
            if similarity_list[index]> larger_similarity:
              larger_similarity = similarity_list[index]

        elif similarity_list[index+1]> similarity_list[index]:
            if similarity_list[index+1]> larger_similarity:
                larger_similarity = similarity_list[index+1]

        index += 1
    index_number = 0
    # check largest similarity
    print(larger_similarity)
    for index, i in enumerate(similarity_list):
        if i == larger_similarity:
            index_number = index

    # check index number for large similarity
    print(index_number)
    print(f"the movie should be next:  {movie_list[index_number]}")
    the_movie = (movie_list1[index_number]).split()
    movie = " ".join(the_movie[0:2])
    # the movie should be (movie)
    print(f"the movie: {movie}")

# ======================= [START]====================
#  open movie txt file and read it and save it in a list and save another list with nlp spacy module
file = open("movies.txt","r")
movie_list = []
movie_list1 = []
for i in file:
    print(i)
    movie_list1.append(i)
    movie_list.append(nlp(i))

# make function for find the similarity in the movies compare with hulk movie
find_similarity()


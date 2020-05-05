from sklearn.feature_extraction.text import CountVectorizer
with open('c:/Users/hamad/OneDrive/Dokumenter/Datamatiker/4.semester/Python/SemesterPlan/Exercises/OPGAVER/uge9/moby_dick.txt', 'r', encoding="utf8") as f:
    moby = f.readlines()

vectorizer = CountVectorizer()

fit = vectorizer.fit_transform(moby)
print(type(fit))
res = fit.todense()  # returns a numpy array of same shape"

wood_idx = vectorizer.vocabulary_['wood']
wood_count = sum(res[:, wood_idx])  # sum all row cells where column == index
print('wood occurs {} times in the text'.format(wood_count))

# matcher.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_mentees_to_mentors(mentees, mentors):
    if not mentees or not mentors:
        return {}

    mentee_bios = [mentee.bio or "" for mentee in mentees]
    mentor_bios = [mentor.bio or "" for mentor in mentors]

    vectorizer = TfidfVectorizer()
    all_bios = mentee_bios + mentor_bios
    tfidf_matrix = vectorizer.fit_transform(all_bios)

    mentee_matrix = tfidf_matrix[:len(mentees)]
    mentor_matrix = tfidf_matrix[len(mentees):]

    similarity = cosine_similarity(mentee_matrix, mentor_matrix)

    matches = {}
    for i, mentee in enumerate(mentees):
        mentor_index = similarity[i].argmax()
        matches[mentee.id] = mentors[mentor_index].id

    return matches

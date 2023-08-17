import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
split_sentences = []

text = """
The motto of science is not “trust us.” (!) The true motto of science is the opposite. It is that of the Royal Society: nullius in verba, or roughly: “take no one's word.”

There is no capital-S Science—a new authority to substitute for God or King. There is only science, which is nothing more or less than the human faculty of reason exercised deliberately, systematically, methodically, meticulously to discover general knowledge about the world.

So when someone laments a lack of “trust” in science today, what do they mean? Do they mean placing religion over science, faith over reason? Do they mean the growing distrust of elites and institutions, a sort of folksy populism that dismisses education and expertise in general? Or do they mean “you have to follow my favored politician / political program, because Science”? (That’s the one to watch out for. Physics, chemistry and biology can point out problems, but we need history, economics and philosophy to solve them.)
"""

def main():
    # text = input("Please enter the body of text: ")
    sentences = sent_tokenize(text)
    print("\n\n")
    print(sentences)

if __name__ == "__main__":
    main()

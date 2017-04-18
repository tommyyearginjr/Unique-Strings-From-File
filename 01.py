words = list()
uniqueWords = list()

originalText = open('gettysburg.txt', 'r').read()

for i in originalText.split():
	i = (i.rstrip('?:!.,;-')).lower()
	words.append(i)

for i in words:
	if i != '':
		if i not in uniqueWords:
			uniqueWords.append(i)
		
print(uniqueWords)
"""
>> ['four', 'score', 'and', 'seven', 'years', 'ago', 'our', 'fathers', 'brought', 'forth', 'on', 'this', 'continent', 'a', 'new', 'nation', 'conceived', 'in', 'liberty', 'dedicated', 'to', 'the', 'proposition', 'that', 'all', 'men', 'are', 'created', 'equal', 'now', 'we', 'engaged', 'great', 'civil', 'war', 'testing', 'whether', 'or', 'any', 'so', 'can', 'long', 'endure', 'met', 'battle-field', 'of', 'have', 'come', 'dedicate', 'portion', 'field', 'as', 'final', 'resting', 'place', 'for', 'those', 'who', 'here', 'gave', 'their', 'lives', 'might', 'live', 'it', 'is', 'altogether', 'fitting', 'proper', 'should', 'do', 'but', 'larger', 'sense', 'not', 'consecrate', 'hallow', 'ground', 'brave', 'living', 'dead', 'struggled', 'consecrated', 'far', 'above', 'poor', 'power', 'add', 'detract', 'world', 'will', 'little', 'note', 'nor', 'remember', 'what', 'say', 'never', 'forget', 'they', 'did', 'us', 'rather', 'be', 'unfinished', 'work', 'which', 'fought', 'thus', 'nobly', 'advanced', 'task', 'remaining', 'before', 'from', 'these', 'honored', 'take', 'increased', 'devotion', 'cause', 'last', 'full', 'measure', 'highly', 'resolve', 'shall', 'died', 'vain', 'under', 'god', 'birth', 'freedom', 'government', 'people', 'by', 'perish', 'earth']
"""

import requests
import lxml.html as lh
import pandas as pd

url = 'http://pokemondb.net/pokedex/all'

# Create a handle, page, to handle the contents of the website
page = requests.get(url)

# Store the contents of the website under doc
doc = lh.fromstring(page.content)

# Parse data that are stored between <tr>..</tr> of the site's HTML code
tr_elements = doc.xpath('//tr')

# Check the length of the first 12 rows
[len(T) for T in tr_elements[:12]]

tr_elements = doc.xpath('//tr')

# Create empty list
col = []
i = 0

# For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i += 1
    name = t.text_content()
    print(f'{i}:{name}')
    col.append((name, []))

# Since out first row is the header, data is stored on the second row onwards
for j in range(1, len(tr_elements)):
    # T is our j'th row
    T = tr_elements[j]

    # If row is not of size 10, the //tr data is not from our table
    if len(T) != 10:
        break

    # i is the index of our column
    i = 0

    # Iterate through each element of the row
    for t in T.iterchildren():
        data = t.text_content()
        # Check if row is empty
        if i > 0:
            # Convert any numerical value to integers
            try:
                data = int(data)
            except:
                pass
        # Append the data to the empty list of the i'th column
        col[i][1].append(data)
        # Increment i for the next column
        i += 1

print([len(C) for (title, C) in col])

Dict = {title: column for (title, column) in col}
df = pd.DataFrame(Dict)

print(df.head())


def str_bracket(word):
    """Add brackets around second term"""
    str_list = [x for x in word]
    for char_ind in range(1, len(str_list)):
        if str_list[char_ind].isupper():
            str_list[char_ind] = ' ' + str_list[char_ind]
    fin_list = ''.join(str_list).split(' ')
    length = len(fin_list)
    if length > 1:
        fin_list.insert(1, '(')
        fin_list.append(')')
    return ' '.join(fin_list)


def str_break(word):
    """Break strings at upper case"""
    # TODO
    str_list = [x for x in word]
    for char_ind in range(1, len(str_list)):
        if str_list[char_ind].isupper():
            str_list[char_ind] = ' ' + str_list[char_ind]
    # TODO
    fin_list = ''.join(str_list).split(' ')
    return fin_list


df['Name'] = df['Name'].apply(str_bracket)
df['Type'] = df['Type'].apply(str_break)
print(df.head())

df.to_json('PokemonData.json')

df = pd.read_json('PokemonData.json')
df = df.set_index(['#'])
print(df.head())


def max_stats(df, col_list):
    """Get Pokemon highest value of the column in the Data Frame"""
    message = ''
    for max_col in col_list:
        stat = df[max_col].max()
        max_name = df[df[max_col] == df[max_col].max()]['Name'].values[0]
        message += max_name+' has the greatest '+max_col+' of '+str(stat)+'.\n'
    return message


def min_stats(df, col_list):
    """Get Pokemon lowest value of the column in the Data Frame"""
    message = ''
    for min_col in col_list:
        stat = df[min_col].min()
        min_name = df[df[min_col] == df[min_col].min()]['Name'].values[0]
        message += min_name+' has the worst '+min_col+' of '+str(stat)+'.\n'
    return message


stats = ['Attack', 'Defense', 'HP', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total']

print(max_stats(df, stats))

print(min_stats(df, stats))

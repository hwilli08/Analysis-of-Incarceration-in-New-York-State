"""
crime-classes.py
Apr 2024 PJW

Use ChatGPT to group NYS crimes into classes.
"""

import openai
import pandas as pd

#
#  Set up alternative prompts
#

prompts = {}

prompts[1] = '''
The following is a list of categories of crimes: violent crimes;
weapons offenses; drug offenses; burglary and theft; sex crimes;
crimes involving children; white-collar crimes.
The text in quotes is a short description of a crime committed by a person
incarcerated in New York State: "{}".
In which category is this crime?
If you are able to determine the category, answer with just the category.
If you are unable to determine the category explain why.
'''

#
#  Remove returns
#

for k,v in prompts.items():
    prompts[k] = v.replace('\n',' ')

#
#  Configure ChatGPT
#

gpt_model = 'gpt-4-turbo-2024-04-09'
gpt_cost_i = 10/1e6
gpt_cost_o = 30/1e6

openai.organization = 'ORG-HERE'
openai.api_key = 'KEY-HERE'

pver = 1

prompt  = prompts[pver]

#
#  Set up functions
#

def do_query(prompt,crime):

    content = prompt.format(crime)

    completion = openai.chat.completions.create(
        model = gpt_model,
        messages=[{
            'role':'user',
            'content': content
            }],
        )

    msg = completion.choices[0].message

    tokens_i = completion.usage.prompt_tokens
    tokens_o = completion.usage.completion_tokens

    print(f'Result: {msg}\nTokens: i={tokens_i}, o={tokens_o}\n')

    return (msg,tokens_i,tokens_o)

#
#  Set up the run
#

raw = pd.read_csv('total_crime_counts.csv')
raw.columns = ['crime','count']

subset = raw # Can use to trim input for testing

#  Output file

ofile = f'Prof_Wilcoxen_GPT.csv'

#
#  Do the work
#

results = []

for i,r in subset.iterrows():

    if r.isna()['crime']:
        continue

    crime = r['crime'].strip()

    print(f'Checking:: {crime}\n',flush=True)

    (msg,tokens_i,tokens_o) = do_query(prompt,crime)

    results.append( {
        'crime':crime,
        'gpt':msg.content,
        'tokens_i':tokens_i,
        'tokens_o':tokens_o,
        })

#
#  Build a dataframe
#

result = pd.DataFrame(results)

#
#  Organize the answers a bit
#

is_long = result['gpt'].str.len() > 30
result['long'] = result['gpt'].where( is_long, "" )
result['gpt'] = result['gpt'].where( is_long==False, "na")
result['gpt'] = result['gpt'].str.lower()

#
#  Write it out
#

result.to_csv(ofile)

#
#  Calculate the cost
#

tot_tok_i = result['tokens_i'].sum()
tot_tok_o = result['tokens_o'].sum()
tot_cost = round(gpt_cost_i*tot_tok_i + gpt_cost_o*tot_tok_o,3)

print(f'\ntotal tokens: i={tot_tok_i}, o={tot_tok_o}\ntotal cost: ${tot_cost}')

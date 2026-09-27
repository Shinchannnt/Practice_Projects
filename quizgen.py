import random as rd
def main():
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':
    'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
    'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
    'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    for quiz_num in range(2):
    
        quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w', encoding='UTF-8') 
        answer_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w', encoding='UTF-8') 

        quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quiz_file.write("\t State Capitals Quiz\n")
        states=list(capitals.keys())
        city=list(capitals.values())
        rd.shuffle(states)
        for i in range(10):
            options=[]
            quiz_file.write(f"{i+1}.What is the capital of {states[i]}?\n")
            right_ans=capitals[f'{states[i]}']
            options.append(right_ans)
            for j in range(3):
                options.append(city[rd.randint(0,49)])
            rd.shuffle(options)
            
            quiz_file.write(f"A.{options[0]}")
            quiz_file.write(f"\nB.{options[1]}")
            quiz_file.write(f"\nC.{options[2]}")
            quiz_file.write(f"\nD.{options[3]}\n")

            answer_file.write(f"{i+1}.{answer(options.index(right_ans))}\n")
def answer(index):
    if index==0: #i
        return "A"
    elif index==1:
        return "B"
    elif index==2:
        return "C"
    elif index==3:
        return "D"
main()
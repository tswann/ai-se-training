import datetime

def process_seq(data):
    # Process list of locations
    for item in data:
        if item['rate'] > 30:
            if item['category'] == 'GHT':
                print('Do some cool processinig') 
            else:
                print('This processing is less cool')


def run():
    ymdstr = datetime.date.today().strftime("%y-%m-%d")
    seq = ({'name': 'Austin', 'rate': 31, 'category': 'AGH' }, 
            {'name': 'New York', 'rate': 27, 'category': 'GHT'}, 
            {'name': 'Las Vegas', 'rate': 56, 'category': 'GHT' })
    process_seq(seq)
    print('Process completed on ' + ymdstr)


if __name__ == '__main__':
    run()

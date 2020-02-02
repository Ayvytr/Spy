import pandas

if __name__ == '__main__':
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop':[1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pandas.DataFrame(data)
    print(frame)

    print(frame.head())
    print(frame.tail())
    

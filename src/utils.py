

def recording_file(filename):
    with open('../data/vacancies.json', 'w') as file:
        json.dump(good_vacancy, file, ensure_ascii=False, default=lambda x: x.__dict__)
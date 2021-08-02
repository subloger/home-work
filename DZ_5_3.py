tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) <= len(klasses):
    tutors_klas_gen = ((tutors[t], klasses[t], ) for t in range(len(tutors)) if len(tutors) <= len(klasses))
else:
    [klasses.append(None) for i in range(len(tutors) - len(klasses))]
    tutors_klas_gen = ((tutors[i], klasses[i], ) for i in range(len(tutors)))

print(next(tutors_klas_gen))
print(next(tutors_klas_gen))
print(next(tutors_klas_gen))
print(next(tutors_klas_gen))
print(next(tutors_klas_gen))
print(next(tutors_klas_gen))
print(next(tutors_klas_gen))
print(next(tutors_klas_gen))

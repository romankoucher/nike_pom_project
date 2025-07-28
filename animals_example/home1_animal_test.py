from animals_example.animal_object import animal

dog1 = animal("Jack",4)
dog2 = animal("Punch", 2)

dog1.make_noise()
dog2.make_noise()

distance_1 = dog1.calculate_distance(12,5, "dog1")
distance_2 = dog2.calculate_distance(10,3, "dog2")
dog2.calculate_distance(4,6, "Roman")
if(distance_1>distance_2):
    print("Distance 1 is longer")
def func(d1, d2):
    new_d = {i : d1[i] for i in d1 if i in d2 and d1[i]==d2[i]}
    return new_d
d1 = {'Janet':87,'Logan':62,'Whitaker':46,'Alyssa':100,'Stef':80,'Jeff':88,'Kim':52,'Sylvia':95}
d2 = {'Logan':62,'Kim':52,'Whitaker':52,'Jeff':88,'Stef':80,'Brian':60,'Lisa':83,'Sylvia':87}

new_d = func(d1,d2)
print(new_d)


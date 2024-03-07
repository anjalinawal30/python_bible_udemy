students = {"Alice":["ID001",26,"A"],
            "Bob":["ID002",27,"B"],
            "Claire":["ID003",17,"C"],
            "Dan":["ID004",21,"D"],
            "Emma":["ID005",22,"E"]
           }

students2 = {"Alice": {"id":"ID001","age":26,"grade":"A"},
            "Bob":{"id":"ID002","age":27,"grade":"B"},
            "Claire":{"id":"ID003","age":17,"grade":"C"},
            "Dan":{"id":"ID004","age":21,"grade":"D"},
            "Emma":{"id":"ID005","age":22,"grade":"E"}
           }

print(students["Claire"])
print(students["Alice"][0])
print(students["Dan"][1:])

print(students2["Alice"]["id"])
print(students2["Dan"]["age"])
print(students2["Emma"]["age"],students2["Emma"]["id"])


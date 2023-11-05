import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/
#
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is
# created in the file `pets_db.py`.
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """
SELECT
    name,
    species,
    age
FROM animals
EXCEPT
SELECT 
    name, 
    species, 
    age 
FROM animals 
INNER JOIN people_animals
ON animals.animal_id = people_animals.pet_id;
"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners.
# The output should be an integer.

sql_pets_older_than_owner = """
SELECT DISTINCT
    COUNT(*)
FROM animals 
INNER JOIN people_animals
ON animals.animal_id = people_animals.pet_id
INNER JOIN people
ON people_animals.owner_id = people.person_id
WHERE animals.age > people.age;
"""

# Part 4.C: BONUS CHALLENGE!
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """
SELECT 
    people.name,
    an.name,
    an.species
FROM animals AS an
INNER JOIN people_animals
ON an.animal_id = people_animals.pet_id
INNER JOIN people 
ON people_animals.owner_id = people.person_id
WHERE people.name = 'bessie'
AND
(SELECT 
    COUNT(*)
 FROM animals AS an2
 INNER JOIN people_animals
 ON an2.animal_id = people_animals.pet_id
 WHERE people_animals.pet_id = an.animal_id) = 1;
"""
# WHERE an2.animal_id = an.animal_id

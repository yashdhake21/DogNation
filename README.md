# DogNation
# Database Management Project (DBMS-Mini-Proj)


## Problem Statement:
The main aim is to design a system that would easily help an adoptee find a pet that matches their preferences. This will be done by considering various factors according to the users needs. Incase an owner loses their dog, we aim to help them find their dog by using our centralised rescued dog database.

( run - in terminal ---   >> python3 mainpage.py )

## Objectives:
    1 To help an adoptee find a dog matching their needs.
    2 Return lost dogs to their owners or help find them.


## Functional Requirements:
    • Search for dog matching the characteristics input by the user.
    • User can apply for a membership after signing up.
    • User can delete membership and his/her details.
    • Let a lost dog be up for adoption after a suitable vetting period.
    • User can store the her/her pertinent details in the user and location tables during sign-up.
    • Users are able to modify their details.
    • Adoption status modification is allowed.

![a1d0f8ec-2876-4813-a2f5-906a968675f2](https://user-images.githubusercontent.com/69303551/140671663-5b6a7cd8-8311-44e7-9e43-4a5b4f7ba34b.jpeg)


## Entity-Relationship Diagram:

![image](https://user-images.githubusercontent.com/69303551/140671440-6977c09c-9ced-431a-8b4c-e97231c50f57.png)

## Highlighting the foreign keys
![Screenshot from 2021-11-08 07-15-04](https://user-images.githubusercontent.com/69303551/140671912-a458a763-3afa-4f5c-8b5b-a37b378e686b.png)




## Functional Dependencies:

### Dog Table:
    • dog_id <- gender
    • dog_id <- weight
    • dog_id <- adoption
    • dog_id <- breed_name
    • dog_id <- liking
### Health Table:
    • dog_id <- neuter_status
    • dog_id <- dna_test
    • dog_id <- special_needs
    • dog_id <- age
### Breed Table:
    • breed_name <- breed_group
    • breed_name <- breed_type
### Dogtag table:
    • dog_id <- tag_name
    • dog_id <- serial_no
    • dog_id <- tag_manufacturer
    • dog_id <- tag_colour
    • dog_id <- tag_material
### Lost Table:
    • dog_id <- found_date
    • dog_id <- age
    • dog_id <- gender
    • dog_id <- location_id
    • dog_id <- breed_name
### Looks Table:
    • dog_id <- dog_size
    • dog_id <- dog_colour
    • dog_id <- weight
### Location Table:
    • location_id <- zipcode
    • location_id <- city
    • location_id <- state
    • location_id <- country
      (all interconnected)
### Users Table:
    • user_id <-  email_id
    • user_id <-  phone_number
    • user_id <-  name
    • user_id <-  liking
    • user_id <-  location
    • user_id <-  breed_want
    • user_id <-  max_dog_age
    • location_id <- user_id
### Membership Table:
    • user_id <-  membership_type
    • user_id <-  payment_status
    • user_id <-  mem_end
    • user_id <-  last_active



## Normalization:
### dog table:
• PK- dog_id, FK-user_id, FK-breed_name
• 2NF as no partial dependencies, 3NF – as no transitive dependencies, BCNF

### user table:
• PK-user_id, FK-location_id
• 2NF as no partial dependencies, 3NF – as no transitive dependencies, BCNF

### location table:
• PK-location_id
• 2NF as no partial dependencies

### breed table:
• PK-breed_name
• 2NF as no partial dependencies,3NF – as no transitive dependencies, BCNF

### health table:
• FK-dog_id, PK-dog_id
• 2NF as no partial dependencies,3NF – as no transitive dependencies, BCNF

### lost table:
• FK-dog_id, PK-dog_id
• 2NF as no partial dependencies,3NF – as no transitive dependencies, BCNF

### looks table:
• FK-dog_id, PK-dog_id
• 2NF as no partial dependencies,3NF – as no transitive dependencies, BCNF

### dogtag table:
• FK-dog_id, PK-dog_id
• 2NF as no partial dependencies,3NF – as no transitive dependencies, BCNF

### membership table:
• FK-uder_id, PK-user_id
• 2NF as no partial dependencies,3NF – as no transitive dependencies, BCNF

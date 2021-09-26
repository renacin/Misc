/*
Name:                                            Renacin Matadeen
Date:                                               09/25/2021
Title                                      Review Of Core SQL Concepts

----------------------------------------------------------------------------------------------------------------------

Notes:
    The Importance Of Databases
        Information is everywhere. All of our interactions produce data; and there is an increasing need to store the
        data that we create.

        Heirarchical & Network Based Databases [Graph Model]
            + Computerized databases systems were first introduced in the early 1960s. The most successful of the first 
            database systems was the SABRE storage methodology introduced by IBM. 
            + Note that these early databases were hierarchical in
            nature; this meant that all entries were stored with some kind of a connection to a parent node. These types
            of databases are very simple in nature. They resemble the structure of tree data stuctures, as well as
            directories within a computer system.

            Benefits:
                + Primarialy worked by having data state their position; heavy use of pointers
                + Main benefits of this type of database where the learning curve, and the speed of operations. Being
                based in pointers data could be accessed very quickly.

            Draw-backs:
                + Pointers, and location of data was always known, primarialy due to pinned addresses. This made it 
                difficult to shuffle data.
                + Data could only have parent/child relationships. A child could only have one parent, but parent multiple
                childs.
                + In many cases a many-to-one relationship would be highly benefitial; ie two parents having 
                relationships to one child.

        Relational Databases
            + In 1970 E.F. Codd published a revolutionaly paper describing an alternative to hierarchical models
            + Main advantage of relational databases over previous models was the ability to allow one record to relate to
            any number of other tables within the dataset.
            + Data duplcation is reduced in the inherent setup, and entry of data

        Database Management System Vs. Relational Database Management System
            + A DBMS is software used to store and manage data.
            + DBMS store data as files, RDBMS store data in tables within the entire database
            + DBMS allow multiple users to access data, where as RDBMS allows multiple users at the same time
            + In DBMS data redundancy is common, while in RDBMS keys, and indexes do not allow redundancy

*/
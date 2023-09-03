package main

import (
	"fmt"

	"github.com/gocql/gocql"
)

func main() {
	session := createSession()
	defer session.Close()

	selectValues(session)
}

func createSession() *gocql.Session {
	cluster := gocql.NewCluster("localhost")
	cluster.Keyspace = "sample"
	cluster.Authenticator = gocql.PasswordAuthenticator{
		Username: "cassandra",
		Password: "cassandra",
	}

	session, err := cluster.CreateSession()
	if err != nil {
		panic(err) // Handle error, for now we'll panic
	}
	return session
}

func selectValues(s *gocql.Session) {
	var id gocql.UUID
	var name string
	var age int

	fmt.Println("Selecting values from users table")

	iter := s.Query(("SELECT id, name, age FROM sample.sample_table")).Iter()
	for iter.Scan(&id, &name, &age) {
		fmt.Println("id:", id, "name:", name, "age:", age)
	}
}

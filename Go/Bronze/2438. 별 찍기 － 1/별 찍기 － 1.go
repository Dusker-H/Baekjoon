package main

import (
	"fmt"
)

func main() {

	var num int
	_, err := fmt.Scan(&num)
	if err != nil {
		fmt.Println(err)
	}

	for i := 1; i <= num; i++ {
		for j := 1; j <= i; j++ {
			fmt.Print("*")
		}
		fmt.Println()

	}
}

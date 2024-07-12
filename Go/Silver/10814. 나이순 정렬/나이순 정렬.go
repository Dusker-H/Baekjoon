package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type user struct {
	age  int
	name string
}

func main() {

	var n int

	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	defer w.Flush()

	fmt.Fscanln(r, &n)

	slice := make([]user, n)

	for i := 0; i < n; i++ {
		fmt.Fscanln(r, &slice[i].age, &slice[i].name)
	}

	sort.SliceStable(slice, func(i, j int) bool {
		if slice[i].age < slice[j].age {
			return true
		} else {
			return false
		}
	})
	//return slice[i].age < slice[j].age

	for i := 0; i < n; i++ {
		fmt.Fprintln(w, slice[i].age, slice[i].name)
	}

}

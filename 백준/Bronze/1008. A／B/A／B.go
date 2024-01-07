package main

import (
	"bufio"
	"fmt"
	"os"
)

func div(a int, b int) float64 {

	fa := float64(a)
	fb := float64(b)
	c := fa / fb

	return c
}

func main() {

	stdin := bufio.NewReader((os.Stdin))

	var a int
	var b int

	_, err := fmt.Scan(&a, &b)
	if err != nil {
		fmt.Println(err)
	}

	if (a < 0) || (b < 0) || (a > 10) || (b > 10) {
		fmt.Print("값에 범위를 초과하였습니다. 다시 입력 바랍니다.")
		stdin.ReadString('\n')
		_, err := fmt.Scan(&a, &b)
		if err != nil {
			fmt.Println(err)
		}
	}

	c := div(a, b)
	fmt.Printf("%.9f", c)

	fmt.Println()

}

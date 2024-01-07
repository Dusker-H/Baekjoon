package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	stdin := bufio.NewReader((os.Stdin))

	var a int
	var b int

	_, err := fmt.Scan(&a, &b)
	if err != nil {
		fmt.Println(err)
	}

	if (a < -10000) || (b < -10000) || (a > 10000) || (b > 10000) {
		fmt.Print("값에 범위를 초과하였습니다. 다시 입력 바랍니다.")
		stdin.ReadString('\n')
		_, err := fmt.Scan(&a, &b)
		if err != nil {
			fmt.Println(err)
		}
	}

	if a > b {
		fmt.Println(">")
	} else if a < b {
		fmt.Println("<")
	} else {
		fmt.Println("==")
	}

}

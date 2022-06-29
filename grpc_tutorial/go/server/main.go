package main

import (
	"fmt"
	"net"
	"os"

	"github.com/y05h1k1ng/grpc-tutorial/go/deepthought"
	"google.golang.org/grpc"
)

const portNumber = 13333

func main() {
	serv := grpc.NewServer()

	deepthought.RegisterComputeServer(serv, &Server{})

	fmt.Println("[+] listening... :", portNumber)
	l, err := net.Listen("tcp", fmt.Sprintf(":%d", portNumber))
	if err != nil {
		fmt.Println("faialed to listen:", err)
		os.Exit(1)
	}

	serv.Serve(l)
}

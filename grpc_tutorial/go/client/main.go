package main

import (
	"context"
	"errors"
	"fmt"
	"io"
	"os"
	"time"

	"github.com/y05h1k1ng/grpc-tutorial/go/deepthought"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

func main() {
	err := subMain()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

func subMain() error {
	if len(os.Args) != 2 {
		return errors.New("usage: client HOST:PORT")
	}

	addr := os.Args[1]

	conn, err := grpc.Dial(addr, grpc.WithInsecure())
	if err != nil {
		return err
	}
	defer conn.Close()

	cc := deepthought.NewComputeClient(conn)

	ctx, cancel := context.WithCancel(context.Background())
	go func(cancel func()) {
		time.Sleep(2500 * time.Millisecond)
		cancel()
	}(cancel)

	stream, err := cc.Boot(ctx, &deepthought.BootRequest{})
	if err != nil {
		return err
	}

	for {
		resp, err := stream.Recv()
		if err != nil {
			if err == io.EOF {
				break
			}

			if status.Code(err) == codes.Canceled {
				break
			}

			return fmt.Errorf("reveiveing boot response: %w", err)
		}
		fmt.Printf("Boot: %s\n", resp.Message)
	}

	return nil
}
